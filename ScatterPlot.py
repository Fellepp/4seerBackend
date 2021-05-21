from Strategy import Strategy
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class ConcreteStrategyScatter(Strategy):
    def getPlot(self, data, x_label, y_label, title, arg1):
        if data == "" or x_label == "" or y_label == "" or title == "":
            print("Missing values")
        else:
            df = pd.read_csv(data)

            plt.scatter(df[x_label], df[y_label])
            plt.ylabel(y_label)
            plt.xlabel(x_label)
            plt.grid()
            #plt.show()
            plt.savefig("scatter.png", bbox_inches='tight')