from confs.ConcectionBD import ConnectionBD
from confs.Pandas import Pandas

def main():
    import pandas as pd

    # Configura la conexión a la base de datos
    connection = ConnectionBD(database='northwind', user='root', password='example', host='localhost')

    # Consulta para obtener los últimos 3 años con ventas
    query_years = """
    SELECT DISTINCT YEAR(OrderDate) AS Year
    FROM Orders
    ORDER BY Year DESC
    LIMIT 3
    """
    # Consulta base
    query_base = """
    SELECT 
        P.ProductName, 
        SUM(OD.Quantity * OD.UnitPrice) AS TotalVenta, 
        R.RegionDescription, 
        YEAR(O.OrderDate) AS Year,
        C.CustomerID
    FROM 
        Products P 
        LEFT JOIN `Order Details` OD ON OD.ProductID = P.ProductID 
        LEFT JOIN Orders O ON O.OrderID = OD.OrderID
        LEFT JOIN Employees E ON E.EmployeeID = O.EmployeeID
        LEFT JOIN EmployeeTerritories ET ON ET.EmployeeID = E.EmployeeID
        LEFT JOIN Territories T ON ET.TerritoryID = T.TerritoryID
        LEFT JOIN Region R ON R.RegionID = T.RegionID
        LEFT JOIN Customers C on C.CustomerID = O.CustomerID
    GROUP BY 
        C.CustomerID, P.ProductName, R.RegionDescription, YEAR(O.OrderDate)
    """
    pandas = Pandas('resources/xlsx', 'Producto_Mas_Vendido_Region_Ano_Cliente.xlsx')
    connection.connect()
    # Ejecuta la consulta y obtiene los años
    years_df = connection.execute_query(query_years)
    # Ejecuta la consulta base
    ventas_df = connection.execute_query(query_base)
    connection.disconnect()

    # Define los años en variables
    years = years_df['Year'].sort_values().tolist()
    last_year_1, last_year_2, last_year_3 = years

    # Crear tabla temporal para Productos Más Vendidos por Región y Año
    ranked_sales_df = ventas_df.groupby(['ProductName', 'RegionDescription', 'Year']).agg({'TotalVenta': 'sum'}).reset_index()
    ranked_sales_df['RowNum'] = ranked_sales_df.groupby(['RegionDescription', 'Year'])['TotalVenta'].rank(method='first', ascending=False)

    productos_mas_vendidos_df = ranked_sales_df[ranked_sales_df['RowNum'] == 1].sort_values(by=['RegionDescription', 'Year'])

    # Crear tabla temporal para Compras por Producto, Región, Cliente y Año
    ventas_por_cliente_df = ventas_df.groupby(['ProductName', 'RegionDescription', 'Year', 'CustomerID']).agg({'TotalVenta': 'sum'}).reset_index()

    max_ventas_df = ventas_por_cliente_df.groupby(['ProductName', 'RegionDescription', 'Year'])['TotalVenta'].transform(max) == ventas_por_cliente_df['TotalVenta']
    compras_por_producto_df = ventas_por_cliente_df[max_ventas_df].sort_values(by=['RegionDescription', 'Year', 'TotalVenta'], ascending=[True, True, False])

    # Combinar ambas tablas temporales para formar la matriz final
    datos_combinados_df = productos_mas_vendidos_df.merge(compras_por_producto_df, on=['ProductName', 'RegionDescription', 'Year'], suffixes=('', '_y'))
    datos_combinados_df['Datos'] = 'Prod: ' + datos_combinados_df['ProductName'] + ' | Cust: ' + datos_combinados_df['CustomerID']

    # Pivotear la tabla para obtener la matriz final con años dinámicos
    final_df = datos_combinados_df.pivot_table(index='RegionDescription', columns='Year', values='Datos', aggfunc='first')
    final_df.columns = ['Año_' + str(col) for col in final_df.columns]
    final_df.reset_index(inplace=True)

    pandas.to_excel(final_df)

    # Mostrar el resultado final
    print(final_df)



    


if __name__ == '__main__':
    main()