from Strategy import Strategy
import pandas as pd
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns


class ConcreteStrategyLine(Strategy):
    def getPlot(self, data, x_label, y_label, title, arg1):
        if (data == "" or y_label == "" or title == ""):
            return ("Missing values")

        else:
            time2 = 'season'
            time1 = 'Year'
            groupby = 'id'
            hue = 'Player'

            df = pd.read_csv(data)
            plt.figure(figsize=(15,8))

            if len(x_label) == 1:
                if x_label[0] == "":
                    df = df.groupby([time1])[y_label].sum()
                    plt.plot(df)
                    plt.title(title)
                    plt.ylabel(y_label)
                    plt.xlabel(x_label)
                    plt.grid()
                    # plt.show()
                    plt.savefig("line.png", bbox_inches='tight')
                else:
                    df = df[df.Player == x_label[0]].sort_values(time1)
                    df[time1] = df[time1].apply(lambda x: str(int(x)))
                    df = df[[time1, y_label]]

                    plt.plot(df[time1], df[y_label])
                    plt.title(title)
                    plt.ylabel(y_label)
                    plt.xlabel(x_label)
                    plt.grid()
                    # plt.show()
                    plt.savefig("line.png", bbox_inches='tight')
            else:
                compareDf = df.head(0)
                for player in x_label:
                    newDf = df[df.Player == player].sort_values(time1)
                    compareDf = pd.concat([newDf, compareDf])

                new_y_label = "Total " + y_label + "s"

                compareDf[new_y_label] = compareDf[[y_label, groupby]].groupby(groupby).cumsum()
                sns.lineplot(x=time2, y=new_y_label, hue=hue, data=compareDf)
                # plt.show()
                plt.savefig("line.png", bbox_inches='tight')

