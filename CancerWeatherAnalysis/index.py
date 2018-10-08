import dash
import plotly
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input,Output
import os
import plotly.graph_objs as go
import plotly.offline as offline
import pandas as pd
from plotly.graph_objs import Layout, Scatter
from csv import DictReader
from app import app
from apps import mapplot,cancerperstate,weather,cancerbyagegroup,cancerbyagegroupnew

# Title the app.
#app = dash.Dash()
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

    html.Div([
    html.Br(),
    html.Br()    
    ], className="row"),    
    # Row: Title         
    html.Div([
        # Column: Logo
        html.Div(
            className='collogo',
            children=[
            html.H1('', className='text-center')]),
       
    # Column: Heading
    
    html.Div([html.H3("INTELLIGENT DATA-ECOSYSTEM", className="text-center")
        ], className="colheader"),    
    ]),
    
    html.Div([
    html.Br(),
    html.Br()    
    ], className="row"),
    html.Div([
        # Column: Logo
        html.Div([
            html.Nav([
                html.Div([                    
                    html.Ul([                        
                        html.A('Cancer Per State',href='/apps/cancerperstate',className='navbar-brand'),
                        html.A('Weather',href='/apps/weather',className='navbar-brand'),
                        html.A('Cancer By Age Group',href='/apps/cancerbyagegroupnew',className='navbar-brand'),
                        html.A('Map',href='/apps/mapplot',className='navbar-brand')                                                
                        ], className='nav navbar-nav')
                    ]
                    , className='container-fluid')]
                    ,className='navbar navbar-inverse')]
                    )  
    ], className="row"),
    
    # Column: Menu

    html.Div([ 
    # For Navigation
    dcc.Location(id='url', refresh=False),               
    html.Div(id='page-content')    
    ], className="row")    
], className="container-fluid")

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/mapplot':
         return mapplot.layout
    elif pathname == '/apps/cancerperstate':
         return cancerperstate.layout
    elif pathname == '/apps/weather':
         return weather.layout
    elif pathname == '/apps/cancerbyagegroupnew':
         return cancerbyagegroupnew.layout
    else:
        return 'Cancer Data Analysis'

if __name__ == "__main__":
    app.run_server(debug=True)