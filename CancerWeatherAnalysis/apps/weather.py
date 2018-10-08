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

dfweather = pd.read_csv('data/weatherdata.csv')

available_weather = dfweather['station_name'].unique()

layout = html.Div([
        html.Div([                
        # Column: Heading    
        html.Div([html.H4("Weather Stats Per State - Line Graph", className="text-center")
        ]),    
    ], className="row"),    
       html.Div([
            html.Div([html.H5("INPUT FIELDS", className="inputfields")
        ]),        
        html.Br(),
        html.Div([
            html.Div([html.Label("Select Weather Stat:", className="subfields"),
            dcc.Dropdown(
                    id='yaxis-column',
                    options=[
                        {'label': 'Temperature - Mean', 'value': 'tmean'},
                        {'label': 'Temperature - Maximum', 'value': 'tmax'}, 
                        {'label': 'Temperature - Minimum','value': 'tmin'},
                        {'label': 'Rainfall', 'value': 'rainfall'}
                    ],
                    value='tmean',className="subfieldscontrol")                        
        ])]),
        html.Br(),
        html.Br(),
        html.Br(),
         html.Div([
            html.Div([                                        
            html.Div([html.Label("Select Station:", className="subfields"),
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in available_weather],
                value='ADELAIDE',className="subfieldscontrol")])
        ])]),
        html.Br(),
        html.Br(),        
         html.Div([
            html.Div([html.Label("Select Year Range:", className="subfields"),  
           html.Br(),                           
           dcc.RangeSlider(
           id='year-slider',
           min=2004,
           max=dfweather['year'].max(),
           step=0.1,
           marks={str(year): str(year) for year in dfweather['year'].unique()},                        
           value=[2004, dfweather['year'].max()])          
        #dcc.Slider(
        #id='year-slider',
        #min=2004,
        #max=dfweather['year'].max(),
        #value=dfweather['year'].max(),
        #step=None,        
        #marks={str(year): str(year) for year in dfweather['year'].unique()}
    #)         
        ])])  
    ], className="inputfieldsrow"),
        dcc.Graph(id='Weather-graphic')
    ], className="row")

@app.callback(
    dash.dependencies.Output('Weather-graphic', 'figure'),
    [dash.dependencies.Input('xaxis-column', 'value'),
        dash.dependencies.Input('yaxis-column', 'value'),                  
     dash.dependencies.Input('year-slider', 'value')])     
def update_graph(xaxis_column_name,yaxis_column_name,year_value):     
    dff = dfweather[dfweather['station_name'] == xaxis_column_name]                      
    return {
        'data': [go.Scatter(                
            x=dff['year'],
            y=dff[yaxis_column_name],
            text=dff['station_name'],
            mode='lines+markers',      
            marker={
                'size': 15,
                'opacity': 0.5                               
            }            
        )
        ],
        'layout': go.Layout(
            xaxis={
                'title': 'Year',
                'type': 'linear',
                'range': [year_value[0],year_value[1]]
            },
            yaxis={
                'title': 2015,
                'type': 'linear'
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }