from Strategy import Strategy
import pandas as pd
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns


class ConcreteStrategyDist(Strategy):
    def getPlot(self, data, x_label, y_label, title, arg1):
        if (data == "" or y_label == "" or title == ""):
            return ("Missing values")

        df = pd.read_csv(data)
        plt.clf()

        plt.title(title)
        df = df[df[y_label] > 10]
        sns.distplot(df[y_label], kde=True, norm_hist=False)
        plt.savefig("dist.png", bbox_inches='tight')
