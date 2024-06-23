from confs.ConcectionBD import ConnectionBD
from confs.Pandas import Pandas

def main():
    # connection = ConnectionBD(database='northwind', user='root',  password='example', host='localhost')
    connection = ConnectionBD(database='pubs', user='root',  password='example', host='localhost')
    #Query
    titles_query = f"""SELECT * FROM titles;"""
    sales_query = f"""SELECT * FROM sales;"""
    titleauthor_query = f"""SELECT * FROM titleauthor;"""
    connection.connect()
    titles = connection.execute_query(titles_query)
    sales = connection.execute_query(sales_query)
    titleauthor = connection.execute_query(titleauthor_query)
    connection.disconnect()

    pandas = Pandas('resources/xlsx', 'Ganancias_por_Autor.xlsx')
    # Primera consulta: Ganancias de libros con autores

    # Juntar las tablas title, sales y titleauthor
    merge_ganancias_author = sales.merge(titles, on='title_id').merge(titleauthor, on='title_id')

    # Calcular las ganancias
    merge_ganancias_author['Ganancia'] = merge_ganancias_author['price'] * merge_ganancias_author['royaltyper'] * merge_ganancias_author['qty'] / 100

    # Agrupar por el au_id
    ganancias_author = merge_ganancias_author.groupby(merge_ganancias_author['au_id'].rename('Autor'))['Ganancia'].sum().reset_index()

    # Sacar las regalías

    # Juntar las tablas title y titleauthor y agruparlos por el title_id
    marge_regalias = titles.merge(titleauthor, on='title_id', how='left').groupby(['title_id', 'price'], as_index=False).agg({'royaltyper': 'sum'})
    
    marge_regalias['Regalias'] = 100 - marge_regalias['royaltyper'].fillna(0)
    
    # Filtrar por las regalias mayores a cero
    marge_regalias = marge_regalias[marge_regalias['Regalias'] > 0]

    # Juntarlo con la tabla sales
    marge_regalias = sales.merge(marge_regalias, on='title_id')

    # Sacar las regalias
    marge_regalias['Ganancia'] = marge_regalias['Regalias'] * marge_regalias['qty'] * marge_regalias['price'] / 100.0
    ganancias_author_anonimo = pandas.build({
            'Autor': ['Anónimo'],
            'Ganancia': [marge_regalias['Ganancia'].sum()]
        })
    final_result = pandas.juntar([
        ganancias_author,
        ganancias_author_anonimo
    ])
    pandas.to_excel(final_result)
    print(final_result)
    return

if __name__ == '__main__':
    main()
