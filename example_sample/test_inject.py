import pytest
from dash import Dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from visual import update_graph

@pytest.fixture
def sample_data():
    data = {
        "Retailer": ["Retailer1"],
        "Retailer ID": [1],
        "Invoice date": ["2023-01-01"],
        "Region": ["North"],
        "State": ["State1"],
        "City": ["City1"],
        "Product": ["Product1"],
        "Price per unit": [10],
        "Unit sold": [5],
        "Total sales": [50],
        "Operating Profit": [5],
        "Operating Margin": ["10%"],
        "Sales Method": ["Method1"]
    }
    return pd.DataFrame(data)

def test_update_graph(dash_duo, sample_data):
    # Setting up a Dash app for testing
    app = Dash(__name__)
    app.layout = html.Div([
        dcc.Dropdown(
            id='analysis-dropdown',
            options=[
                {'label': 'Total Sales By Region', 'value': 'total_sales_by_region'},
                {'label': 'Best Selling Product', 'value': 'best_selling_product'},
                {'label': 'Total Sales Per Week', 'value': 'total_sales_per_week'},
                {'label': 'Total Sales Per Month', 'value': 'total_sales_per_month'},
                {'label': 'Total Sales Per Year', 'value': 'total_sales_per_year'},
                {'label': 'Sales Method Each Month', 'value': 'sales_method_each_month'}
            ],
            value='total_sales_by_region'
        ),
        dcc.Graph(id='analysis-graph')
    ])

    app.callback(
        Output('analysis-graph', 'figure'),
        [Input('analysis-dropdown', 'value')]
    )(update_graph)

    dash_duo.start_server(app)

    # Simulate selecting an option from the dropdown
    dash_duo.select_dcc_dropdown('#analysis-dropdown', 'total_sales_by_region')
    dash_duo.wait_for_element('#analysis-graph')

    # Get the graph figure
    graph = dash_duo.find_element('#analysis-graph')
    fig = graph.get_property('figure')

    assert fig is not None
    assert 'data' in fig
    assert len(fig['data']) > 0
