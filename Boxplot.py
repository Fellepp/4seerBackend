from Strategy import Strategy
import pandas as pd
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns


class ConcreteStrategyBox(Strategy):
    def getPlot(self, data, x_label, y_label, title, arg1):
        if (data == "" or y_label == "" or title == ""):
            return ("Missing values")

        df = pd.read_csv(data)
        compare_df = df.head(0)

        for player in x_label:
            new_df = df[df.Player == player]
            compare_df = pd.concat([new_df, compare_df])
        compare_df

        plt.clf()
        plt.title(title)
        plt.figure(figsize=(15, 8))
        sns.boxplot(x='Player', y=y_label, data=compare_df)
        sns.stripplot(x='Player', y=y_label, data=compare_df, marker="o")
        plt.savefig("box.png", bbox_inches='tight')

