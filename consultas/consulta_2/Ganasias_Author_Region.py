from confs.ConcectionBD import ConnectionBD
from confs.Pandas import Pandas

def main():
    # connection = ConnectionBD(database='northwind', user='root', password='example', host='localhost')
    connection = ConnectionBD(database='northwind', user='root', password='example', host='localhost')

    # Consulta para obtener los datos
    query = """
        SELECT c.CustomerID, c.CompanyName, YEAR(o.OrderDate) AS OrderYear, er.RegionDescription, od.Quantity, od.UnitPrice
        FROM Customers c
        INNER JOIN Orders o ON c.CustomerID = o.CustomerID
        INNER JOIN `Order Details` od ON o.OrderID = od.OrderID
        INNER JOIN (
            SELECT DISTINCT e.EmployeeID, r.RegionDescription
            FROM Employees e
            JOIN EmployeeTerritories et ON e.EmployeeID = et.EmployeeID
            JOIN Territories t ON et.TerritoryID = t.TerritoryID
            JOIN Region r ON t.RegionID = r.RegionID
        ) as er ON er.EmployeeID = o.EmployeeID;
    """

    # Leer los datos de la base de datos en un DataFrame de pandas
    connection.connect()
    df = connection.execute_query(query)
    connection.disconnect()

    #Create Pandas
    pd = Pandas('resources/xlsx', 'Maximo_Ganancias_Autor_Region.xlsx')

    # Limpiar espacios adicionales en los nombres de las regiones
    df['RegionDescription'] = df['RegionDescription'].str.strip()

    # Calcular el TotalPurchase
    df['TotalPurchase'] = df['Quantity'] * df['UnitPrice']

    # Agrupar y obtener el MaxTotalPurchase por OrderYear y RegionDescription
    max_purchases = df.groupby(['OrderYear', 'RegionDescription'])['TotalPurchase'].max().reset_index()
    max_purchases = max_purchases.rename(columns={'TotalPurchase': 'MaxTotalPurchase'})

    # Unir los dataframes para obtener los clientes con MaxTotalPurchase
    customer_purchases = pd.join(df, max_purchases, on=['OrderYear', 'RegionDescription'])
    customer_purchases = customer_purchases[customer_purchases['TotalPurchase'] == customer_purchases['MaxTotalPurchase']]

    # Crear columnas separadas para cada región
    regions = ['Eastern', 'Northern', 'Southern', 'Westerns']
    result = customer_purchases.pivot_table(index='OrderYear', columns='RegionDescription', values='CustomerID', aggfunc=lambda x: ', '.join(x.astype(str))).reindex(columns=regions)

    # Renombrar las columnas
    result.columns = ['Este', 'Norte', 'Sur', 'Oeste']

    # Reiniciar el índice para obtener el DataFrame final
    result = result.reset_index()

    # Guardar el resultado en un archivo Excel
    pd.to_excel(result)

    # Verificar el resultado final
    print("Resultado final:")
    print(result)


    


if __name__ == '__main__':
    main()