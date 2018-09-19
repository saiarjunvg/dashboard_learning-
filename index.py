import dash
import plotly
import dash_html_components as html
import dash_core_components as dcc
#from dotenv import find_dotenv, load_dotenv
import os
import plotly.graph_objs as go
import plotly.offline as offline
import pandas as pd
#from toolz import groupby, compose, pluck
from plotly.graph_objs import Layout, Scatter
#from toolz import countby, first
from csv import DictReader


################################################################################
# PLOTS
################################################################################
TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

def sighting_year(sighting):
    return dt.datetime.strptime(sighting['timestamp'], TIMESTAMP_FORMAT).year


def bigfoot_by_year(sightings):
    # Create a dict mapping the 
    # classification -> [(year, count), (year, count) ... ]    

    # Build the plot with a dictionary.    
    classifications = sightings.groupby('cancer_type', as_index=False)
    return {
        "data": [
            { 
                "type": "scatter",
                "mode": "lines+markers",
                "name": classification,
                "x": class_sightings['year'],
                "y": class_sightings['incident_count']
            }
            for classification, class_sightings in classifications            
        ],
        "layout": {
            "title": "Ploting of Incident Count,Year with CancerType",
            "showlegend": False
        }
    }

def bigfoot_map(sightings):
    # groupby returns a dictionary mapping the values of the first field 
    # 'classification' onto a list of record dictionaries with that 
    # classification value.
    # classifications = groupby('classification', sightings)
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
                "style": "outdoors"
            }
        }
    }

def bigfoot_dow(StateAnalysis):
           
    # Produces a dict dow => count.
      StateAnalysisCol = StateAnalysis.groupby('state', as_index=False)
      return {
        "data": [
                {
                    "type": "bar",
                    "x": StateData['state'],
                    "y": StateData['gender'],
                    #"text": StateData['incident_count'], 
                    "name": StateCol                           
                }
                # for classification, class_sightings in classifications.items()
                for StateCol,StateData in StateAnalysisCol
            ],       
        "layout": {
            "title": "Incidentcount in State Wise_Male_female_others"
        }
    }

def bigfoot_class(sightings):    
    sightings_by_class = sightings.groupby('year', as_index=False)

    return {
        "data": [
            {
                "type": "pie",
                "labels": genderdata['gender'],
                "values": genderdata['incident_count'],
                "hole": 0.4
            }
            for gendercol,genderdata in sightings_by_class
        ],
        "layout": {
            "title": "% of Gender Incidence"
        }
    }



# fin = open('data/bfro_report_locations.csv', 'r')

df = pd.read_csv('data/weatherdata.csv')
dfState = pd.read_csv('data/cancer_state.csv')
dfgender = pd.read_csv('data/cancer_gender.csv')



app = dash.Dash()

# Title the app.
app.title = "Australia Weather & Cancer Analysis"

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

################################################################################
# LAYOUT
################################################################################



# Boostrap CSS.
app.css.append_css({
    "external_url": 'assets/bootstrap/3.3.7/css/bootstrap.min.css'
})

# Extra Dash styling.
app.css.append_css({
   "external_url": 'assets/chriddyp/pen/bWLwgP.css'
})


# Boostrap CSS.
#app.css.append_css({
#    "external_url": "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
#})

# Extra Dash styling.
#app.css.append_css({
#   "external_url": 'https://codepen.io/chriddyp/pen/bWLwgP.css'
#})

# JQuery is required for Bootstrap.
app.scripts.append_script({
    "external_url": 'assets/bootstrap/3.3.7/js/jquery-3.2.1.min.js'
})

app.scripts.append_script({
    "external_url": 'assets/bootstrap/3.3.7/js/bootstrap.min.js'
})
# JQuery is required for Bootstrap.
#app.scripts.append_script({
 #   "external_url": "https://code.jquery.com/jquery-3.2.1.min.js"
#})

# Bootstrap Javascript.
#app.scripts.append_script({
 #   "external_url": "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"
#})


app.layout = html.Div([    
    # Row: Title         
    html.Div([
        # Column: Logo
        html.Div(
            className='collogo',
            children=[
            html.H1('', className='left')]),
       
    # Column: Heading
    html.Div([html.H2("INTELLIGENT DATA-ECOSYSTEM", className="text-center")
        ], className="colheader")
    ], className="row"),  

    # Row: Map + DOW
    html.Div([
        # Column: Map
        html.Div([
            dcc.Graph(
                id="bigfoot-map",
                figure=bigfoot_map(df))
        ], className="col-md-8"),

    # Column: Day of Week
    html.Div([
        dcc.Graph(
            id="bigfoot-dow",
            figure=bigfoot_dow(dfState))
        ], className="col-md-4")
    ], className="row"),

    # Row: Year + Class
    html.Div([
        # Column: Year
        html.Div([
            dcc.Graph(
                id="bigfoot-by-year",
                figure=bigfoot_by_year(dfgender))
        ], className="col-md-8"),

        # Column: Class
        html.Div([
            dcc.Graph(
                id="bigfoot-class",
                figure=bigfoot_class(dfgender))
        ], className="col-md-4")
    ], className="row")
], className="container-fluid")



if __name__ == "__main__":
    app.run_server(debug=True)