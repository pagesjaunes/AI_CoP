
import plotly.offline as pyo
import plotly.graph_objs as go

import pandas as pd

def ex1():
    data = pd.read_csv('../data/gauss1.csv', header=None)
    pyo.plot([
        go.Scatter(
            x = data.iloc[:, 0],
            y = data.iloc[:, 1],
            mode = 'markers'
    )], filename="scatterplot-gauss1.html", auto_open=False)
