from dash import html, dash_table, Input, Output, State, callback
from dash import dcc
import dash_bootstrap_components as dbc
from datetime import date
import pandas as pd
# from models import Work,Worker,Leave,read_workers,read_works
# df = pd.DataFrame(read_works())

labelDict = {   

    # 'margin':'0 10px 10px',
    'text-shadow':'1px 1px 1px blue',
    'font-size':'25px'
    }
labelDict2 = {   

    # 'margin':'0 10px 10px',
    'text-shadow':'1px 1px 1px green',
    'font-size':'45px'
    }
def makeRow(itmArray):
    wew = list()
    for ea in itmArray:
        # print(ea)
        for ee in ea:
            wew.append(ee)
    return dbc.Row(wew)

def side2side(itm1,itm2):

    return dbc.Col(itm1),dbc.Col(itm2)

page1 = html.Div(
    children=[
    html.H1('Statistical Process Control Data Analysis', style={'textAlign':'center'}),

    html.H4('Takudzwa Mutsatsa: N0237739Y', style={'textAlign':'right','color':'red'}),
    html.Hr(),
    # INPUT SETTINGS
html.Div(
        children=[
                        makeRow([
                side2side(html.Label("Quality Parameter: ",style=labelDict),
        dcc.Dropdown(['servingTime', 'friability', 'disintergration Time', 'hardness','thickness', 'meanweight', 'granulation Time', 'granulation Moisture','compression Force', 'compression Speed'], 'meanweight', id='qty-drpd-val1'),
                    ),
                    
                    ])
                    
        ],
        style={'margin':'0  40px'}
    ),

    
        # ],
#         style={"flex-direction":"row","display":"flex","justify-content":"center"}

    # ),
    

    html.Hr(),

html.Div(
        children=[
                    dbc.Col(dbc.Button("Control Chart",id="ctrl-grph"))
                    
        ],
        style={'margin':'0  40px'}
    ),
    html.Hr(),
      dcc.Loading(
            id="loading-1",
            type="default",
            children=    [
                
    
    ]
    ),
 

    # html.Div(
        
    #     id='countShit',
    #     style={'margin':'0  40px'}
    # ),
    makeRow(
    [
        
                side2side(
                    html.Label(style=labelDict,id='procLabel'),
              dbc.Input(id="param-input", placeholder="Value", type="number")
                    ),
                side2side(
                html.Label("Tolerance(+-): ",style=labelDict),
        dbc.Input(id="tol-input", placeholder="Tolerance for Value", type="number"),
                    )                   
                    ]
    ),
    html.Hr(), 
    dbc.Row([
           dbc.Col(dbc.Button("Find Capability Curves",id="cap-crv2"))
                    ]

    ),
    html.Hr(),

    dbc.Row([
        html.Div(
        id="proc_cap",
        style={"margin-left":"3%","margin-right":"2%",'border':'3px solid green'}
    ),
    ]),
     # dbc.Alert(id="tbl_out")
],
style={'background':'linear-gradient(90deg, rgba(113,14,14,1) 0%, rgba(84,84,88,1) 35%, rgba(9,9,121,1) 100%)'})

