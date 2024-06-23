import pandas as pd
import os

class Pandas:
    def __init__(self, path = 'resources/xlsx', file='file.xlsx'):
        self.path = path
        self.file = file
    def build(self,data, columns = None):
        return pd.DataFrame(data, columns=columns)
    def to_excel(self,df):
        ruta = os.path.join(self.path, self.file)
        return df.to_excel(ruta, index=False)
    def format(self, df): 
        return df.to_dict(orient='records')
    def juntar(self, dataDF = []) -> pd.DataFrame:
        return pd.concat(dataDF, ignore_index=True)
    def join(self, df1, df2, right_on=None, left_on=None):
        return pd.merge(df1, df2, left_on=left_on,right_on=right_on)