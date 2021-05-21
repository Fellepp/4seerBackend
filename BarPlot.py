from Strategy import Strategy
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

class ConcreteStrategyBar(Strategy):
    def getPlot(self, data, x_label, y_label, title, arg1):
        if data == "" or x_label == "" or y_label == "" or title == "":
            print("Missing values")
        else:
            df = pd.read_csv(data)
            if y_label == "Count" or y_label == "count" or y_label == "COUNT":
                df = df.groupby([x_label]).size().reset_index(name=y_label)



            df = df.head(20)
            #print(df)
            #for y_value in y_label:
                #ax = df.plot(x=x_label, y=y_value, kind='barh', ax=ax)

            plt.figure(figsize=(15,8))
            ax = sns.barplot(x=df[y_label], y=df.index, color='blue', orient='h')
            ax.set_yticklabels(df[x_label])
            plt.ylabel(x_label)
            plt.xlabel(y_label)
            plt.title(title)
            plt.grid()
            plt.savefig("bar.png", bbox_inches='tight')
            #plt.show()