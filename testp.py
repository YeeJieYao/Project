import pandas as pd
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

df = pd.read_csv("https://raw.githubusercontent.com/YeeJieYao/Project/main/population.csv")

colors = ["black", "blue", "red", "yellow", "pink", "orange"]

app = dash.Dash(__name__)
server = app.server

image_path = 'https://www.mmu.edu.my/wp-content/themes/mmu2018/assets/images/logo-mmu.png'

app.layout = html.Div(
    children=[
    html.Img(src=image_path),	                
    html.H1("Data Visualization"),
    html.H2("Dashboard showing graphs"),

        dcc.Dropdown(id='my-dropdown', multi=True,
                     options=[{'label': x, 'value': x} for x in sorted(df.state.unique())],
                     value=["Johor"]),
        html.Button(id='my-button', n_clicks=0, children="Show all"),
        dcc.Graph(id='graph-output', figure={}),

        html.Div(id="sentence-output", children=["This is the color I love"], style={}),
        dcc.RadioItems(id='my-radioitem', value="black", options=[{'label': c, 'value': c} for c in colors]),
    ]
)

# Single Input, single Output, State, prevent initial trigger of callback, PreventUpdate
@app.callback(
    Output(component_id='graph-output', component_property='figure'),
    [Input(component_id='my-dropdown', component_property='value'),
    Input(component_id='SELECT_ALL_STATES_BUTTON', component_property='n_clicks')],
    # [State(component_id='my-dropdown', component_property='value')],
    prevent_initial_call=False
)
def update_my_graph(val_chosen):
    if len(val_chosen) > 0:
        # print(n)
        print(f"value user chose: {val_chosen}")
        print(type(val_chosen))
        dff = df[df["state"].isin(val_chosen)]
        fig = px.pie(dff, values="pop", names="state", title="Malaysia Population")
        fig.update_traces(textinfo="value+percent").update_layout(title_x=0.5)
        return fig
    elif len(val_chosen) == 0:
        raise dash.exceptions.PreventUpdate

if __name__ == '__main__':
    app.run_server(debug=True)