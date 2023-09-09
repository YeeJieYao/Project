import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server

# Declare DataFrame and File Paths
df = pd.read_csv("https://raw.githubusercontent.com/YeeJieYao/Project/main/population.csv")
image_path = 'https://www.mmu.edu.my/wp-content/themes/mmu2018/assets/images/logo-mmu.png'

# Declare Data Fields
stateSelected = ["Johor", "Perak", "Melaka"]
colors = ["Black", "Blue", "Red", "Yellow", "Pink", "Orange"]

# HTML Layout
app.layout = html.Div(
    children=[
    html.Img(src=image_path),	                
    html.H1("Data Visualization"),
    html.H2("Dashboard showing graphs"),
    html.H1('Dash Tabs component demo'),
    dcc.Tabs(id="tabs-example-graph", value='tab-1-example-graph', children=[
    dcc.Tab(label='Tab One', value='tab-1-example-graph'),
    dcc.Tab(label='Tab Two', value='tab-2-example-graph'),
    ]),
    html.Div(id='tabs-content-example-graph')
    ]
)

# Graph and Color Function
@app.callback(
    [Output('graph-output', 'figure'), Output('sentence-output', 'style')],
    [Input(component_id='my-radioitem', component_property='value'),
    Input(component_id='my-dropdown', component_property='value'),],
    prevent_initial_call=False
)

def update_graph(color_chosen, val_chosen):
    if len(val_chosen) == 0:
        return dash.no_update, {"color": color_chosen}
    else:
        dff = df[df["state"].isin(val_chosen)]
        fig = px.pie(dff, values="pop", names="state", title="Malaysia Population")
        fig.update_traces(textinfo="value+percent").update_layout(title_x=0.5)
        return fig, {"color": color_chosen}

# Download CSV Function
@app.callback(
    Output("download-dataframe-csv", "data"),
    Input("btn_csv", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_data_frame(df.to_csv, "malaysiapopulation.csv")

# Tab Function
@app.callback(Output('tabs-content-example-graph', 'children'), Input('tabs-example-graph', 'value'))

def render_content(tab):
    if tab == 'tab-1-example-graph':
        return html.Div([
            html.Br(),
            html.H1(id="sentence-output", children=["Malaysia Population by State"], style={}),
            dcc.Dropdown(id='my-dropdown', multi=True, options=[{'label': x, 'value': x} for x in sorted(df.state.unique())], value=stateSelected),
            dcc.Graph(id='graph-output', figure={}),
            html.H2(children=["Choose a color for the title"], style={}),
            dcc.RadioItems(id='my-radioitem', value="black", options=[{'label': c, 'value': c} for c in colors]),
        ])
    elif tab == 'tab-2-example-graph':
        return html.Div([
            html.Br(),
            html.H1(id="sentence-output2", children=["Download the CSV File"], style={}),
            html.Button("Download CSV", id="btn_csv"),
            dcc.Download(id="download-dataframe-csv"),
        ])   

# Main    
if __name__ == '__main__':
    app.run_server(debug=True)