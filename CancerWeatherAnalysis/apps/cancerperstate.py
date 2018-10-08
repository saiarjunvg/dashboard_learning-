import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly
import os
import plotly.graph_objs as go
import plotly.offline as offline
import pandas as pd
#from toolz import groupby, compose, pluck
from plotly.graph_objs import Layout, Scatter
#from toolz import countby, first
from csv import DictReader

from app import app
#app = dash.Dash()
#app.config.suppress_callback_exceptions = True

# Boostrap CSS.
app.css.append_css({
    "external_url": 'assets/bootstrap/3.3.7/css/bootstrap.min.css'
})

# Extra Dash styling.
app.css.append_css({
    "external_url": 'assets/chriddyp/pen/bWLwgP.css'
})


# JQuery is required for Bootstrap.
app.scripts.append_script({
    "external_url": 'assets/bootstrap/3.3.7/js/jquery-3.2.1.min.js'
})

app.scripts.append_script({
    "external_url": 'assets/bootstrap/3.3.7/js/bootstrap.min.js'
})

dfState = pd.read_csv('data/cancer_state.csv')

available_state = dfState['state'].unique()

layout = html.Div([
        html.Div([                
        # Column: Heading    
        html.Div([html.H4("Cancer Stats Per State - Line Graph", className="text-center")
        ]),    
    ], className="row"),    
       html.Div([
            html.Div([html.H5("INPUT FIELDS", className="inputfields")
        ]),        
        html.Br(),
        html.Div([
            html.Div([html.Label("Select Cancer Stat:", className="subfields"),
            dcc.Dropdown(
                    id='yaxis-column',
                    options=[
                        {'label': 'Incident Count', 'value': 'incident_count'},
                        {'label': 'Mortality Count', 'value': 'mortality_count'}, 
                        {'label': 'Incident Rate', 'value': 'i_asr'},
                        {'label': 'Mortality Rate', 'value': 'm_asr'}
                    ],
                    value='incident_count',className="subfieldscontrol")                        
        ])]),
        html.Br(),
        html.Br(),
        html.Br(),
         html.Div([
            html.Div([#html.Label("Select Cancer Type/s:", className="subfields"),
            #dcc.Dropdown(
            #        id='xaxis-column',
            #        options=[
            #            {'label': 'LIP', 'value': 'LIP'},
            #            {'label': 'MOUTH', 'value': 'MOUTH'},
            #            {'label': 'OESOPHAGEAL', 'value': 'OESOPHAGEAL'},
            #            {'label': 'THYROID', 'value': 'THYROID'},
            #            {'label': 'TONGUE', 'value': 'TONGUE'}
            #        ],
            #        value='LIP',className="subfieldscontrol")                        
            #dcc.Checklist(
            #    id='xaxis-column1',
            #    options=[
            #        {'label': 'LIP', 'value': 'LIP', 'className' : 'radioctrl'},
            #        {'label': 'MOUTH', 'value': 'MOUTH','className' : 'radioctrl'},
            #        {'label': 'OESOPHAGEAL', 'value': 'OESOPHAGEAL','className' : 'radioctrl'},
            #        {'label': 'THYROID', 'value': 'THYROID','className' : 'radioctrl'},
            #        {'label': 'TONGUE', 'value': 'TONGUE','className' : 'radioctrl'}
            #    ],
            #    values=[],
            #    labelStyle={'display': 'table-cell'},
            #    className="cancertypelbl"),
            html.Div([html.Label("Select State:", className="subfields"),
            dcc.Dropdown(
                    id='xaxis-column',
                    options=[
                        {'label': 'All', 'value': 'All'},
                        {'label': 'Australian Capital Territory', 'value': 'Australian Capital Territory'},
                        {'label': 'New South Wales', 'value': 'New South Wales'}, 
                        {'label': 'Northern Territory', 'value': 'Northern Territory'},
                        {'label': 'South Australia', 'value': 'South Australia'},
                        {'label': 'Tasmania', 'value': 'Tasmania'},
                        {'label': 'Victoria', 'value': 'Victoria'},
                        {'label': 'Western Australia', 'value': 'Western Australia'}
                    ],
                    value='All',className="subfieldscontrol")
            #dcc.Dropdown(
            #    id='xaxis-column',
            #    options=[{'label': i, 'value': i} for i in available_state],
            #    value='New South Wales',className="statectrl"
            #    )
                ])
        ])]),
        html.Br(),
        html.Br(),        
         html.Div([
            html.Div([html.Label("Select Year Range:", className="subfields"),  
            html.Br(),
        dcc.RangeSlider(
           id='year-slider',
           min=2004,
           max=dfState['year'].max(),
           step=0.1,
           marks={str(year): str(year) for year in dfState['year'].unique()},                        
           value=[2004, dfState['year'].max()])            
        #dcc.Slider(
        #id='year-slider',
        #min=2004,
        #max=dfState['year'].max(),
        #value=dfState['year'].max(),
        #step=None,
        #marks={str(year): str(year) for year in dfState['year'].unique()}
    #)         
        ])])  
    ], className="inputfieldsrow"),


        # Column: bar chart for state
        #html.Div([
        # dcc.Graph(
        #     id="bigfoot-dow",
        #     figure=bigfoot_by_year(dfState,dash.dependencies.Input('yaxis-column', 'value')))
         
        #], className="col-md-8")
        dcc.Graph(id='indicator-graphic')
    ], className="row")



#@app.callback(
#    dash.dependencies.Output('indicator-graphic', 'figure'),
#    [dash.dependencies.Input('yaxis-column', 'value'),
#     dash.dependencies.Input('year--slider', 'value')])

@app.callback(
    dash.dependencies.Output('indicator-graphic', 'figure'),
    [dash.dependencies.Input('xaxis-column', 'value'),
        dash.dependencies.Input('yaxis-column', 'value'),          
     dash.dependencies.Input('year-slider', 'value')])     
def update_graph(xaxis_column_name,yaxis_column_name,year_value):
    html.Label("Fucntion Call")
    #dff = dfState[dfState['year'] == year_value]
    if xaxis_column_name == "All":
       dfStatecol = dfState.groupby('state', as_index=False)   
    else:
       dff = dfState[dfState['state'] == xaxis_column_name]   
       dfStatecol = dff.groupby('state', as_index=False)
    #dff = dfState[dfState['state'] == xaxis_column_name]   
            
    return {
        'data': [go.Scatter(
            #x=dff[dff['cancer_type'] == xaxis_column_name]['year'],
            #y=dff[dff['incident_count']] == yaxis_column_name]['incident_count'],
            x=dfStateOne['year'],
            y=dfStateOne[yaxis_column_name],
            text=dfStateOne['state'] + '  ' + dfStateOne['cancer_type'],
            mode='lines+markers',
            name=dfStateTest,
            marker={
                'size': 15,
                'opacity': 0.5
               # 'line': {'width': 0.5, 'color': 'white'}
            }            
        )for dfStateTest, dfStateOne in dfStatecol
        ],
        'layout': go.Layout(
            xaxis={
                'title': 'Year',
                'type': 'linear',
                'range': [year_value[0],year_value[1]]
            },
            yaxis={
                'title': yaxis_column_name,
                'type': 'linear'
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }    