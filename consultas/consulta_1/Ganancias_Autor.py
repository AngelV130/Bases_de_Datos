from confs.ConcectionBD import ConnectionBD
from confs.Pandas import Pandas

def main():
    # connection = ConnectionBD(database='northwind', user='root', password='example', host='localhost')
    connection = ConnectionBD(database='pubs', user='root', password='example', host='localhost')
    # Consulta SQL combinada para obtener los datos básicos
    query = """
    SELECT
        t.title_id,
        t.title,
        t.price,
        s.qty,
        te.au_id,
        te.royaltyper
    FROM
        titles t
    LEFT JOIN
        titleauthor te ON t.title_id = te.title_id
    RIGHT JOIN
        sales s ON t.title_id = s.title_id;
    """
    connection.connect()
    df = connection.execute_query(query)
    connection.disconnect()
    #Create Pandas
    pd = Pandas('resources/xlsx', 'Ganancias_por_Autor.xlsx')
    # Ganancias de libros con autores
    ganancias_author = df
    ganancias_author['au_id'] = ganancias_author['au_id'].fillna('Anónimo')
    ganancias_author['royaltyper'] = ganancias_author['royaltyper'].fillna(100)
    ganancias_author = df.groupby('au_id').apply(lambda group: (group['qty'] * group['price'] * group['royaltyper'].fillna(100) / 100).sum()).reset_index(name='Ganancias')
    # Ganancias de autores Anónimos
    # Agrupar por title_id y eliminar duplicados de au_id
    grouped_df = df.drop_duplicates(subset=['title_id', 'au_id'])
    # Tratar los valores nulos antes de la suma
    grouped_df['royaltyper'] = grouped_df['royaltyper'].fillna(100)
    # Sumar los royaltyper agrupando por title_id
    titels_royaltyper = grouped_df.groupby('title_id')['royaltyper'].sum().reset_index()
    titels_royaltyper['royaltyper'] = 100 - titels_royaltyper['royaltyper']
    titels_royaltyper = titels_royaltyper[titels_royaltyper['royaltyper'] > 0]
    # Seleccionar las columnas solicitadas
    marge_ganacias = pd.join(df[['qty', 'price', 'title_id']], titels_royaltyper[['title_id', 'royaltyper']], left_on='title_id', right_on='title_id')
    marge_ganacias['qty'] = marge_ganacias['qty'].fillna(0)
    marge_ganacias['Ganancias'] = marge_ganacias['qty'] * marge_ganacias['price'] * marge_ganacias['royaltyper'] / 100.0
    ganancias_anonimo = pd.build({
        'au_id': ['Anónimo'],
        'Ganancias': [marge_ganacias['Ganancias'].sum() ]
    })

    # Juntar los resultados groupby au_id
    ganancias_author_result = pd.juntar([ganancias_author, ganancias_anonimo]).groupby('au_id').sum().reset_index().rename(columns={'au_id': 'Autor'})

    # Guardar el resultado en un archivo Excel
    pd.to_excel(ganancias_author_result)

    # Mostrar el resultado final
    print(ganancias_author_result)

    


if __name__ == '__main__':
    main()