import math
import plotly.offline as pyo
import plotly.graph_objs as go

import numpy as np

def tickpos(n):
    return [2 * math.pi * k / n for k in range(n)]

def findpos(x):
    if 7 * math.pi / 4 <= x < 2 * math.pi or 0 <= x < math.pi / 4:
        return 'middle right'
    elif math.pi / 4 <= x < math.pi / 2:
        return 'top right'
    elif math.pi / 2 <= x < 3 * math.pi / 4:
        return 'top left'
    elif 3 * math.pi / 4 <= x < 5 * math.pi / 4:
        return 'middle left'
    elif 5 * math.pi / 4 <= x < 3 * math.pi / 2:
        return 'bottom left'
    elif 3 * math.pi / 2 <= x < 7 * math.pi / 4:
        return 'bottom right'
    else:
        return None
    
def table(p, n):
    return [(2 * math.pi * x / n, 2 * math.pi * int((x * p) % n) / n) for x in range(n)]

def go_dots(n):
    return go.Scatter(
        x = np.cos(tickpos(N)),
        y = np.sin(tickpos(N)),
        text = list(map(str, range(N))),
        textposition=list(map(findpos, tickpos(N))),
        mode = "markers+text",
        showlegend=False
    )

def go_circle(n):
    return go.Scatter(
        x = np.cos(np.linspace(0, 2 * math.pi, 1000)),
        y = np.sin(np.linspace(0, 2 * math.pi, 1000)),
        line = dict(color='black'),
        showlegend=False
    )

def go_lines(p, n, showlegend=True):
    return go.Scatter(
        x = sum([[np.cos(x[0]), np.cos(x[1]), None] for x in table(p, N)], []),
        y = sum([[np.sin(x[0]), np.sin(x[1]), None] for x in table(p, N)], []),
        mode = 'lines',
        name='%.2f mod %d' % (p, n),
        showlegend=showlegend,
        line=dict(width=1, color='rgba(0,0,0,0.25)')
    )

N = 50
fig = go.Figure(
    data = [
        go_circle(N),
        go_lines(2, N, showlegend=False),
        go_dots(N),
    ],
    layout = go.Layout(
        plot_bgcolor='white',
        height=700,
        yaxis=dict(
            scaleanchor="x",
            scaleratio=1,
            showgrid=False,
            zeroline=False,
            showticklabels=False
        ), xaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False
        ))
)

pyo.plot(fig, filename='table2mod50.html', auto_open=False)

N = 200
nframes = 500
fig = go.Figure(
    data = [
        go_lines(2, N, showlegend=False),
        go_circle(N),
    ],
    layout = go.Layout(
        plot_bgcolor='white',
        height=700,
        yaxis=dict(
            scaleanchor="x",
            scaleratio=1,
            showgrid=False,
            zeroline=False,
            showticklabels=False
        ), xaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False
        ),
        updatemenus=[dict(
            type="buttons",
            buttons=[
                dict(
                    label="Play",
                    method="animate",
                    args=[None, {
                        "frame": {
                            "duration": 10,
                            "redraw": False
                        },
                        "fromcurrent": True,
                        "transition": {
                            "duration": 0,
                            "easing": None
                        }
                    }]
                )
            ]
        )]
    ),
    frames = [
        go.Frame(
            data=[go_lines(x, N, showlegend=False)], name="%.2f mod %d" % (x, N) 
        ) for x in np.linspace(2, 10, nframes)
    ]
)

pyo.plot(fig, filename='table2to10mod50.html', auto_open=False)

N = 1000
p = 350
nframes = 500
fig = go.Figure(
    data = [
        go_lines(p, N, showlegend=False),
        go_circle(N),
    ],
    layout = go.Layout(
        plot_bgcolor='white',
        height=700,
        yaxis=dict(
            scaleanchor="x",
            scaleratio=1,
            showgrid=False,
            zeroline=False,
            showticklabels=False
        ), xaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False
        ),
        updatemenus=[dict(
            type="buttons",
            buttons=[
                dict(
                    label="Play",
                    method="animate",
                    args=[None, {
                        "frame": {
                            "duration": 10,
                            "redraw": False
                        },
                        "fromcurrent": True,
                        "transition": {
                            "duration": 0,
                            "easing": None
                        }
                    }]
                )
            ]
        )]
    ),
    frames = [
        go.Frame(
            data=[go_lines(x, N, showlegend=False)], name="%.2f mod %d" % (x, N) 
        ) for x in np.linspace(p, p + 20, nframes)
    ]
)
pyo.plot(fig, filename='table350to370mod50.html', auto_open=False)
