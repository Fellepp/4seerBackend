import pandas as pd
from DataVisualizer import DataVisualizer as dv
from Lineplot import ConcreteStrategyLine
from BarPlot import ConcreteStrategyBar
from ScatterPlot import ConcreteStrategyScatter


def getColumns(csvFile):
    df = pd.read_csv(csvFile)
    return df.iloc[:, 1:].columns.tolist()


def dataPrep(data, UPLOAD_FOLDER):
    defaultInputs = {
        "csv": UPLOAD_FOLDER,
        "x_label": "",
        "y_label": "",
        "title": "",
        "start": "",
        "end": "",
        "time1": "",
        "time2": "",
        "groupby": "",
        "hue": "",
        "sort": "",
        "head": ""
    }

    for key in data:
        if key == 'csv':
            defaultInputs[key] += data[key]
        elif key == "start" or key == "end" or key == "head":
            defaultInputs[key] = int(data[key])
        else:
            defaultInputs[key] = data[key]

    return defaultInputs

def dataVisualizerCommunicator(input):
    print(input)
    name = ""
    cs = ""
    if input['plot'] == 'scatter':
        cs = ConcreteStrategyScatter()
        name = "scatter.png"
        print("scatter")
    if input['plot'] == 'line':
        cs = ConcreteStrategyLine()
        name = "line.png"
        print("line")
    if input['plot'] == 'bar':
        cs = ConcreteStrategyBar()
        name = "bar.png"
        print("bar")

    dvv = dv(cs)
    dvv.getPlots(input['csv'], input['x_label'], input['y_label'], input['title'], input['arg1'])
    return name

