import dash
from dash import dcc, html  # Updated import statements
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc  # Import dbc

from inject import SalesAnalyzer, TotalSalesByRegion, BestSellingProduct, TotalSales, SalesMethodEachMonth
from process import import_data, CsvImportFactory

# Load data
csv_factory = CsvImportFactory()
column_names = ["Retailer", "Retailer ID", "Invoice date", "Region", "State", "City", "Product", "Price per unit", "Unit sold", "Total sales", "Operating Profit", "Operating Margin", "Sales Method"]
csv_data = import_data(csv_factory, 'C:/Users/97150/OneDrive/Desktop/APDP/Data_new.csv', column_names)

# Initialize Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.H1("Sales Data Analysis Dashboard"),
    html.Div([
        html.Label("Select Analysis Type:"),
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
    ]),
    html.Div(id='additional-controls'),
    dcc.Graph(id='analysis-graph')
])

@app.callback(
    Output('analysis-graph', 'figure'),
    Output('additional-controls', 'children'),
    Input('analysis-dropdown', 'value')
)
def update_graph(selected_analysis):
    analyzer = SalesAnalyzer(TotalSalesByRegion(['Northeast', 'South', 'West', 'Midwest', 'Southeast']))
    additional_controls = []

    if selected_analysis == 'total_sales_by_region':
        analyzer.set_strategy(TotalSalesByRegion(['Northeast', 'South', 'West', 'Midwest', 'Southeast']))
        data = analyzer.analyze(csv_data)
        fig = px.bar(data, x='Region', y='Total sales', title='Total Sales by Region')
    elif selected_analysis == 'best_selling_product':
        analyzer.set_strategy(BestSellingProduct())
        data = analyzer.analyze(csv_data)
        fig = px.bar(data, x='Product', y='Unit sold', title='Best Selling Products')
    elif selected_analysis == 'total_sales_per_week':
        analyzer.set_strategy(TotalSales('W'))
        data = analyzer.analyze(csv_data)
        fig = px.line(data, x='Invoice date', y='Total sales', title='Total Sales Per Week')
    elif selected_analysis == 'total_sales_per_month':
        analyzer.set_strategy(TotalSales('M'))
        data = analyzer.analyze(csv_data)
        fig = px.line(data, x='Invoice date', y='Total sales', title='Total Sales Per Month')
    elif selected_analysis == 'total_sales_per_year':
        analyzer.set_strategy(TotalSales('Y'))
        data = analyzer.analyze(csv_data)
        fig = px.line(data, x='Invoice date', y='Total sales', title='Total Sales Per Year')
    elif selected_analysis == 'sales_method_each_month':
        analyzer.set_strategy(SalesMethodEachMonth())
        data = analyzer.analyze(csv_data)
        fig = px.line(data, x='Invoice date', y='Total sales', color='Sales Method', title='Sales Method Each Month')

    return fig, additional_controls

if __name__ == '__main__':
    app.run_server(debug=True)
