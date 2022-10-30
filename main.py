import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import plotly.express as px
import plotly.graph_objects as go

import numpy as np
import pandas as pd

df = pd.read_csv("toDash.csv")

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL])

fig = px.bar(df, x='Usuário', y='Espaço Utilizado (MB)', barmode='group',
                   title="Espaço utilizado por Usuário",
                   template='plotly_dark')

config = {'responsive': True}

fig.update_layout(font_family='Rockwell', font_size=20)
fig.update_traces(marker_color='green')

fig.add_shape()

app.layout = html.Div(children=[

    dcc.Graph(
        id='grafico',
        figure=fig,
        style = {'paddingTop': "8%",'paddingLeft': '10%', 'paddingRight':'10%'}

    )
])

if __name__ == '__main__':
    app.run_server(debug=True)