import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly
import os
import plotly.graph_objs as go
import plotly.offline as offline
import pandas as pd
from plotly.graph_objs import Layout, Scatter
from csv import DictReader
from app import app

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

dfAge = pd.read_csv('data/new.csv')

layout = html.Div([
        html.Div([                
        # Column: Heading    
        html.Div([html.H4("Cancer By Age Group - Pie Chart", className="text-center")
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
                        {'label': 'Incident Rate', 'value': 'i_crude_rate'},
                        {'label': 'Mortality Rate', 'value': 'm_crude_rate'}
                    ],
                    value='incident_count',className="subfieldscontrol")                        
        ])]),
        html.Br(),
        html.Br(),
        html.Br(),
         html.Div([
            html.Div([
            html.Div([html.Label("Select Age:", className="subfields"),
            dcc.Dropdown(
                    id='xaxis-column',
                    options=[
                        {'label': '0-4', 'value': '0-4-'},
                        {'label': '5-9', 'value': '5-9-'},
                        {'label': '10-14', 'value': '10-14-'},
                        {'label': '15-16', 'value': '15-19-'},
                        {'label': '20-24', 'value': '20-24-'},
                        {'label': '25-29', 'value': '25-29-'},
                        {'label': '30-34', 'value': '30-34-'},
                        {'label': '35-39', 'value': '35-39-'},
                        {'label': '40-44', 'value': '40-44-'},
                        {'label': '45-49', 'value': '45-49-'},
                        {'label': '50-54', 'value': '50-54-'},
                        {'label': '55-59', 'value': '55-59-'},
                        {'label': '60-64', 'value': '60-64-'},
                        {'label': '65-69', 'value': '65-69-'},
                        {'label': '70-74', 'value': '70-74-'},
                        {'label': '75-79', 'value': '75-79-'},
                        {'label': '80-84', 'value': '80-84-'},
                        {'label': '85', 'value': '85+'}
                    ],
                    value='0-4-',className="subfieldscontrol")           
                ])
        ])]),
        html.Br(),
        html.Br(),
        html.Br(),
             html.Div([
            html.Div([
            html.Div([html.Label("Select Cancer Type:", className="subfields"),
            dcc.Dropdown(
                    id='cancertype',
                    options=[
                        {'label': 'LIP', 'value': 'LIP'},
                        {'label': 'MOUTH', 'value': 'MOUTH'},
                        {'label': 'OESOPHAGEAL', 'value': 'OESOPHAGEAL'},
                        {'label': 'THYROID', 'value': 'THYROID'},
                        {'label': 'TONGUE', 'value': 'TONGUE'}                       
                    ],
                    value='MOUTH',className="subfieldscontrol")           
                ])
        ])])      
           
    ], className="inputfieldsrow"),        
        dcc.Graph(id='Gender-graphic1')
    ], className="row")

@app.callback(
    dash.dependencies.Output('Gender-graphic1', 'figure'),
    [dash.dependencies.Input('xaxis-column', 'value'),
        dash.dependencies.Input('yaxis-column', 'value'),
        dash.dependencies.Input('cancertype', 'value')])     
def bigfoot_class(xaxis_column_name,yaxis_column_name,cancertype):    
    #dff = dfAge[dfAge['cancer_stat'] == yaxis_column_name]
    dff1 = dfAge[dfAge['cancer_type'] == cancertype]
    return {
        "data": [
            {
                "type": "pie",
                "labels": dff1['Age'],
                "values": dff1[yaxis_column_name],
                #"hole": 0.4,
                'name':'Test'
            }            
        ],
        "layout": {
            "title": "% of Gender Incidence"
        }
    }   