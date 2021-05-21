from Strategy import Strategy
import pandas as pd
import matplotlib
import numpy as np
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

class ConcreteStrategyLin(Strategy):
    def getPlot(self, data, x_label, y_label, title, arg1):
        if (data == "" or y_label == "" or title == ""):
            return ("Missing values")

        df = pd.read_csv(data)
        place_to_beat = 0
        stat = y_label
        Player = x_label


        all_time = df[['Player', stat, 'id']].groupby(['id', 'Player']).sum()
        all_time = all_time.reset_index()
        all_time.columns = ['id', 'Player', stat]
        all_time = all_time.sort_values(by=stat, ascending=False)

        list_all_time = all_time['id'].tolist()
        all_time_full = df[df.id.isin(list_all_time)]
        all_time_full[title] = all_time_full[[stat, 'id']].groupby('id').cumsum()

        topdf = all_time.iloc[place_to_beat][stat]
        playerdf = all_time_full[all_time_full.Player == Player]

        X = playerdf['season'].values.reshape(-1, 1)
        y = playerdf[title].values

        reg = LinearRegression().fit(X, y)
        player_season = playerdf.loc[playerdf['season'].idxmax()]['season']
        X_test = np.array(range(player_season + 1, player_season + 15)).reshape(-1, 1)
        y_pred = reg.predict(X_test)

        title = Player, "will pass", all_time.iloc[place_to_beat]['Player'], "on the total", stat, "list in %sth season" % X_test[np.where(y_pred > topdf)][0][0]


        plt.clf()
        plt.axhline(y=topdf, color='red')
        plt.scatter(X, y)
        plt.scatter(X_test, y_pred)
        plt.title(title)
        plt.plot(X_test, y_pred, linewidth=2)
        plt.savefig("lin.png", bbox_inches='tight')






