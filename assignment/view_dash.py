import dash
from dash import dcc, html
import plotly.graph_objs as go
from process import Data

data = [r'C:\Users\97150\OneDrive\Desktop\APDP\Data.csv']
preprocessor = Data(data)

preprocessor.clean_data()
preprocessor.handle_missing_values()
preprocessor.scale_features()
preprocessor.encode_categorical_variables()


app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='visualisation-graph')
])

@app.callback(
    dash.dependencies.Output('visualisation-graph', 'figure'),
    []
)
def update_graph():
    feature_data = preprocessor.get_processed_data()
    '''product_line_counts = feature_data['PRODUCTLINE'].value_counts()'''
    order_numbers = feature_data['ORDERLINENUMBER']
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=order_numbers), row=2, col=1)
    fig.update_xaxes(title_text="Order Line Number", row=2, col=1)
    fig.update_yaxes(title_text="Frequency", row=2, col=1)


    fig.update_layout(title='Visualization of Product Line and Order Line Number',
                      height=800, width=1000, showlegend=False)
    return fig

#torun the app
if __name__ == '__main__':
    app.run_server(debug=True)
