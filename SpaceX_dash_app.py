# Import required libraries

import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import warnings
warnings.filterwarnings(
    "ignore",
    message="Parsing dates involving a day of month without a year specified")


# Read the airline data into pandas dataframe
spacex_df = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv')
max_payload = int(spacex_df['Payload Mass (kg)'].max())
min_payload = int(spacex_df['Payload Mass (kg)'].min())
site_launch = spacex_df['Launch Site'].unique()
dropdown_options = [{"label": "All Sites", "value": "ALL"}] + [{'label': site, 'value': site} for site in site_launch]


# Create a dash application
app = dash.Dash(__name__)
app.title = "SpaceX Launch Records Dashboard"
app.config.suppress_callback_exceptions = True

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                
                                dcc.Dropdown(id='site-dropdown',
                                             options=dropdown_options,
                                             value='ALL',
                                             placeholder="Select a Launch Site",
                                             searchable=True,
                                             clearable=False,
                                             style={'width': '80%', 'padding': '3px', 'font-size': '20px', 'text-align': 'center'}),
                                
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(id='payload-slider',
                                                 min=min_payload,
                                                 max=max_payload,
                                                 step=1000,
                                                 marks={i: str(i) for i in range(min_payload, max_payload + 1, 1000)},
                                                 value=[min_payload, max_payload],
                                                 pushable=True),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output

@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    
    if entered_site == 'ALL':
        df_all = spacex_df[spacex_df['class'] == 1]
        fig = px.pie(
            df_all,
            values='class',         
            names='Launch Site',
            title='Total Success Launches by Site'
        )
        return fig
    else:
        df_site = spacex_df[spacex_df['Launch Site'] == entered_site].copy()
        df_site['Outcome'] = df_site['class'].map({1: 'Success', 0: 'Failure'})
        fig = px.pie(
            df_site,
            names='Outcome',        
            title=f'Total Success vs. Failure for site {entered_site}'
        )
        return fig
# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'),
               Input(component_id='payload-slider', component_property='value')])
def get_scatter_chart(entered_site, payload_range):
    filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= payload_range[0]) & 
                            (spacex_df['Payload Mass (kg)'] <= payload_range[1])]
    
    if entered_site == 'ALL':
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', 
                         color='Booster Version Category', 
                         title='Correlation between Payload and Success for all Sites')
        return fig
    else:
        filtered_df = filtered_df[filtered_df['Launch Site'] == entered_site]
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', 
                         color='Booster Version Category', 
                         title=f'Correlation between Payload and Success for site {entered_site}')
        return fig


# Run the app
if __name__ == '__main__':
    app.run(port=8450, debug=True)
  
