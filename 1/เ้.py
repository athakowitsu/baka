import pandas as pd
from pandas.io.parsers import read_csv
def readcsv(url):
    colums = ['sepal lenght','sepal width','petal lenght','petal width','class']
    data = pd.read_csv(url,name=colums)
    return data
def get_stats(df):
    a = pd.DataFrame(df)
    return a.describe()