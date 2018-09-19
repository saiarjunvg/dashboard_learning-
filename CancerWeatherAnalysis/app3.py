import dash
import shutil
import dash_html_components as html
import dash_core_components as dcc
from dotenv import find_dotenv, load_dotenv
import os
import pandas as pd
from toolz import groupby, compose, pluck



from csv import DictReader

# pluck returns a generator, so compose it with list to materialize it.
listpluck = compose(list, pluck)


################################################################################
# PLOTS
################################################################################

def bigfoot_map(sightings):
    # groupby returns a dictionary mapping the values of the first field 
    # 'classification' onto a list of record dictionaries with that 
    # classification value.
    # classifications = groupby('classification', sightings)
    classifications = sightings.groupby('classification', as_index=False)
    return {
        "data": [
                {
                    "type": "scattermapbox",
                    "lat": class_sightings['latitude'],
                    "lon": class_sightings['longitude'],
                    "text": class_sightings['title'],
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
                    "lat": 40,
                    "lon": -98.5
                },
                "pitch": 0,
                "zoom": 2,
                "style": "outdoors"
            }
        }
    }








# fin = open('data/bfro_report_locations.csv', 'r')

df = pd.read_csv('data/bfro_report_locations.csv')
# print(df.head)

reader = DictReader(df)
BFRO_LOCATION_DATA = [
    line for line in reader
]


app = dash.Dash()

# Title the app.
app.title = "Bigfoot Sightings"


################################################################################
# LAYOUT
################################################################################

# Boostrap CSS.
app.css.append_css({
    "external_url": "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
})

# Extra Dash styling.
app.css.append_css({
    "external_url": 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

# JQuery is required for Bootstrap.
app.scripts.append_script({
    "external_url": "https://code.jquery.com/jquery-3.2.1.min.js"
})

# Bootstrap Javascript.
app.scripts.append_script({
    "external_url": "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"
})


app.layout = html.Div([
    # Column: Title + Map
    html.Div([
        # Row: Title
        html.Div([
            html.H1("Bigfoot Sightings", className="text-center")
        ], className="row"),
        # Row: Map
        html.Div([
            dcc.Graph(
                id="bigfoot-map",
                ############### NEW CODE #############
                # figure=bigfoot_map(BFRO_LOCATION_DATA)
                figure=bigfoot_map(df)
                ######################################    
            )
        ], className="row")
    ], className="col-md-12")
], className="container-fluid")



if __name__ == "__main__":
    app.run_server(debug=True)