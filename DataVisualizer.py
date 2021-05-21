from Strategy import Strategy
#from Lineplot import ConcreteStrategyLine
#from BarPlot import ConcreteStrategyBar
#from ScatterPlot import ConcreteStrategyScatter

class DataVisualizer():
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def strategy(self) -> Strategy:
        return self._strategy

    def getPlots(self, data, x_label, y_label, title, arg1) -> None:
        self._strategy.getPlot(data, x_label, y_label, title, arg1)



#dvl = ConcreteStrategyLine()
#dvb = ConcreteStrategyBar()
#dvs = ConcreteStrategyScatter()
#dv1 = DataVisualizer(dvl)
#dv2 = DataVisualizer(dvb)
#dv3 = DataVisualizer(dvs)
#dv1.getPlots(data="../Lab1/stats.csv", x_label=["Stephen Curry", "Ray Allen", "Reggie Miller", "Klay Thompson", "Kobe Bryant"], y_label="3P", title="Comparison of 3 point evolution", start=1965, end=2021, time1='Year', time2='season', groupby='id', hue='Player', sort="", head=0)
#dv2.getPlots(data="../Lab1/stats.csv", x_label="Player", y_label="3P", title="3P in a season", start="", end="", time1="Year", time2="", groupby="", hue="", sort=False, head=10)
#dv3.getPlots(data="../Lab1/stats.csv", x_label="BLK", y_label="TRB", title="Size chart", start="", end="", time1="", time2="", groupby="", hue="Player", sort="", head="")

#dv1.getPlots(data="../Aleks/laps_races.csv", x_label="", y_label="milliseconds", title="Lap time evolution", start="", end="", time1='year', time2='', groupby='', hue='', sort="", head="")
#dv2.getPlots(data="../Aleks/circuits.csv", x_label='country', y_label='Count', title='Which countries have had the most circuits?', start="", end="", time1="", time2="", groupby="", hue="", sort=False, head=20)
#dv3.getPlots(data="../Aleks/results.csv", x_label="position", y_label="milliseconds", title="Starting position and final position", start="", end="", time1="", time2="", groupby="", hue="", sort="", head=70)