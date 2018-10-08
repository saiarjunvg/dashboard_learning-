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

#from app import app



app = dash.Dash()

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

df = pd.read_csv('data/weatherdata.csv')
available_station = df['station_name'].unique()

def bigfoot_map(sightings): 
    classifications = sightings.groupby('station_name', as_index=False)
    return {
        "data": [
                {
                    "type": "scattermapbox",
                    "lat": class_sightings['lat'],                    
                    "lon": class_sightings['long'],
                    "text": class_sightings['rainfall'],
                    "mode": "markers",
                    "name": classification,
                    "marker": {
                        "size": 3,
                        "opacity": 1.0                        
                    }
                }
                # for classification, class_sightings in classifications.items()
                for classification, class_sightings in classifications
            ],
        "layout": {
            "autosize": True,
            "hovermode": "closest",
            "mapbox": {
                "accesstoken": 'pk.eyJ1IjoiYWRpdHlhYW5hbHl0aWNzIiwiYSI6ImNqbG45bTE0eDFnd2wzd3M2MXpyem45c3MifQ.IMY_zeUjj3zdW-XM9fU_Nw',
                "bearing": 0,
                "center": {
                    "lat": -37.8221486,
                    "lon": 145.0367703
                },
                "pitch": 0,
                "zoom": 1.8,
                "style": "satellite-streets"
            }
        }
    }
def bigfoot_map1(sightings): 
    classifications = sightings.groupby('station_name', as_index=False)
    return {
        "data": [
                {
                    "type": "scattermapbox",
                    "lat": class_sightings['lat'],                    
                    "lon": class_sightings['long'],
                    "text": class_sightings['tmean'],
                    "mode": "markers",
                    "name": classification,
                    "marker": {
                        "size": 3,
                        "opacity": 1.0
                    }
                }
                # for classification, class_sightings in classifications.items()
                for classification, class_sightings in classifications
            ],
        "layout": {
            "autosize": True,
            "hovermode": "closest",
            "mapbox": {
                "accesstoken": 'pk.eyJ1IjoiYWRpdHlhYW5hbHl0aWNzIiwiYSI6ImNqbG45bTE0eDFnd2wzd3M2MXpyem45c3MifQ.IMY_zeUjj3zdW-XM9fU_Nw',
                "bearing": 0,
                "center": {
                    "lat": -37.8221486,
                    "lon": 145.0367703
                },
                "pitch": 0,
                "zoom": 1.8,
                "style": "satellite-streets"
            }
        }
    }

def bigfoot_map2(sightings): 
    classifications = sightings.groupby('station_name', as_index=False)
    return {
        "data": [
                {
                    "type": "scattermapbox",
                    "lat": class_sightings['lat'],                    
                    "lon": class_sightings['long'],
                    "text": class_sightings['tmax'],
                    "mode": "markers",
                    "name": classification,
                    "marker": {
                        "size": 3,
                        "opacity": 1.0
                    }
                }
                # for classification, class_sightings in classifications.items()
                for classification, class_sightings in classifications
            ],
        "layout": {
            "autosize": True,
            "hovermode": "closest",
            "mapbox": {
                "accesstoken": 'pk.eyJ1IjoiYWRpdHlhYW5hbHl0aWNzIiwiYSI6ImNqbG45bTE0eDFnd2wzd3M2MXpyem45c3MifQ.IMY_zeUjj3zdW-XM9fU_Nw',
                "bearing": 0,
                "center": {
                    "lat": -37.8221486,
                    "lon": 145.0367703
                },
                "pitch": 0,
                "zoom": 1.8,
                "style": "light"
            }
        }
    }

def bigfoot_map3(sightings): 
    classifications = sightings.groupby('station_name', as_index=False)
    return {
        "data": [
                {
                    "type": "scattermapbox",
                    "lat": class_sightings['lat'],                    
                    "lon": class_sightings['long'],
                    "text": class_sightings['tmin'],
                    "mode": "markers",
                    "name": classification,
                    "marker": {
                        "size": 3,
                        "opacity": 1.0
                    }
                }
                # for classification, class_sightings in classifications.items()
                for classification, class_sightings in classifications
            ],
        "layout": {
            "autosize": True,
            "hovermode": "closest",
            "mapbox": {
                "accesstoken": 'pk.eyJ1IjoiYWRpdHlhYW5hbHl0aWNzIiwiYSI6ImNqbG45bTE0eDFnd2wzd3M2MXpyem45c3MifQ.IMY_zeUjj3zdW-XM9fU_Nw',
                "bearing": 0,
                "center": {
                    "lat": -37.8221486,
                    "lon": 145.0367703
                },
                "pitch": 0,
                "zoom": 1.8,
                "style": "satellite-streets"
            }
        }
    }

layout = html.Div([ html.Div([                
        # Column: Heading    
        html.Div([html.H4("Cancer and Weather - Heat Map", className="text-center")
        ]),    
    ], className="row"),    
       html.Div([
            html.Div([html.H5("INPUT FIELDS", className="inputfields")
        ]),        
        html.Br(),
        html.Div([html.Label("Select Station:", className="subfields"),
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in available_station],
                value='ADELAIDE',className="subfieldscontrol")]),
        html.Br(),
        html.Br(),          
         html.Div([
            html.Div([html.Label("Select Year Range:", className="subfields"),  
            html.Br(),
        dcc.RangeSlider(
           id='year-slider',
           min=2004,
           max=df['year'].max(),
           step=0.1,
           marks={str(year): str(year) for year in df['year'].unique()},                        
           value=[2004, df['year'].max()])                         
        ])])  
    ], className="inputfieldsrow"), 
      html.Div([
        # Column: Map
        html.Div([html.Label("Temprature", className="subfields")        
        ], className="col-md-6"),     
        html.Div([html.Label("Rainfall", className="subfields")                   
        ], className="col-md-6"),
      ], className="row"),
      html.Div([
        # Column: Map
        html.Div([
            dcc.Graph(
                id="bigfoot-map",
                figure=bigfoot_map1(df))
        ], className="col-md-6"),     
        html.Div([
            dcc.Graph(
                id="bigfoot-map1",
                figure=bigfoot_map(df))
        ], className="col-md-6"),
      ], className="row"),
     html.Div([
        # Column: Map
        html.Div([
            dcc.Graph(
                id="bigfoot-map2",
                figure=bigfoot_map2(df))
        ], className="col-md-6"),     
        html.Div([
            dcc.Graph(
                id="bigfoot-map3",
                figure=bigfoot_map3(df))
        ], className="col-md-6"),
    ], className="row")])