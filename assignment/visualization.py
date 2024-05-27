import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from process import Data

data_path = r'C:\Users\97150\OneDrive\Desktop\APDP\Data.csv'
preprocessor = Data(data_path)

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Sales Data Dashboard'),
    dcc.Dropdown(id='sales-dropdown',
                 options=[{'label': i, 'value': i} for i in preprocessor.unique_values('PRODUCTLINE')],
                 value='Motorcycles'),
    dcc.Graph(id='sales-graph')
])

@app.callback(
    Output(component_id='sales-graph', component_property='figure'),
    [Input(component_id='sales-dropdown', component_property='value')]
)
def update_graph(selected_sales):
    filtered_data = preprocessor.filter(lambda record: record['PRODUCTLINE'] == selected_sales)
    line_fig = px.line(filtered_data,
                       x='Order Line Number', y='Frequency',
                       color='type',
                       title=f'Sales graph in {selected_sales}')
    return line_fig


if __name__ == '__main__':
    app.run_server(debug=True)




