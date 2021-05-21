import pycountry
from Strategy import Strategy
import pandas as pd
import matplotlib
#import geopandas

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns


class ConcreteStrategyGeo(Strategy):
    def getPlot(self, data, x_label, y_label, title, arg1):
        df = pd.read_csv(data)
        print(df)


def alpha3code(column):
    CODE=[]
    for country in column:
        try:
            code=pycountry.countries.get(name=country).alpha_3
           # .alpha_3 means 3-letter country code
           # .alpha_2 means 2-letter country code
            CODE.append(code)
        except:
            CODE.append('None')
    return CODE

def alpha2code(column):
    CODE=[]
    for country in column:
        try:
            code=pycountry.countries.get(name=country).alpha_2
           # .alpha_3 means 3-letter country code
           # .alpha_2 means 2-letter country code
            CODE.append(code)
        except:
            CODE.append('None')
    return CODE



