import dash
from dash import html, dash_table, Input, Output, State, callback, callback_context
from dash import dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from datetime import date, timedelta
from pg1 import page1,makeRow,labelDict,side2side
from axn import makeCtrlData,makeCharts,ProCap
import time
import numpy as np
import math
from dash.exceptions import PreventUpdate



app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])
dff = pd.read_excel('dataplay.xlsx')

tabs = dbc.Tabs(
    [
        dbc.Tab(page1, label="Show Data",tab_id='tab-1'),

    ],id='tabs'
)
app.layout = tabs


@app.callback(
     Output("proc_cap", "children"),
      
    Input("cap-crv2","n_clicks"),
    [
        State("tol-input","value"),
        State("param-input","value"),
        State("qty-drpd-val1", "value")
    ],
    prevent_initial_call=True,
    

    )
def capIndices(btn2,tol,param,qty):

    if btn2 is None:
        raise PreventUpdate
    df3 = dff.copy()
    # return html.H1("wwwwww")
    return ProCap(df3[qty],param,tol)

@app.callback(
     [Output("loading-1", "children"),
      Output("procLabel", "children")],
      
    Input("ctrl-grph","n_clicks"),
    State("qty-drpd-val1", "value"),
    prevent_initial_call=True,

    )
def update_line_chart(btn,qty):

    findf = pd.DataFrame()
    df2 = dff.copy()
    for vall in df2.columns.to_list():
        if vall != "Proc":
            dfrmSet = df2.groupby('Proc')[vall].apply(list)
            intdf = pd.DataFrame(dfrmSet)
            findf = pd.concat([findf,intdf],axis=1,join='outer')


    figDfm,dta,mean,stdDev = makeCtrlData(findf,qty)

    chart1, chart2 = makeCharts(figDfm,qty)
    prmStrng = qty+" Val: "

    return [
            html.Div(
        
        id='countShit',
        style={'margin':'0  40px'},
        children=[
        dcc.Graph(id="graph",figure=chart1),
        html.Hr(),dcc.Graph(id="graph2",figure=chart2)
        ]
    ),
                    html.Hr(),
                    

    ], prmStrng



app.run_server(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
