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

app.layout = html.Div(
    children=[
        dcc.Dropdown(id='my-dropdown', multi=True,
                     options=[{'label': x, 'value': x} for x in sorted(df.state.unique())],
                     value=["Johor", "Kedah",
                            "Kelantan"]),
        html.Button(id='my-button', n_clicks=0, children="Show breakdown"),
        dcc.Graph(id='graph-output', figure={}),

        html.Div(id="sentence-output", children=["This is the color I love"], style={}),
        dcc.RadioItems(id='my-radioitem', value="black", options=[{'label': c, 'value': c} for c in colors]),
    ]
)


# Single Input, single Output, State, prevent initial trigger of callback, PreventUpdate
@app.callback(
    Output(component_id='graph-output', component_property='figure'),
    [Input(component_id='my-dropdown', component_property='value')],
    # [Input(component_id='my-button', component_property='n_clicks')],
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



# Multiple Input, multiple Output, dash.no_update
#@app.callback(
#     [Output('graph-output', 'figure'), Output('sentence-output', 'style')],
#    [Input(component_id='my-radioitem', component_property='title'),
#    Input(component_id='my-dropdown', component_property='value'),
#    Input(component_id='my-button', component_property='n_clicks')],
#     prevent_initial_call=False
# )
#def update_graph(color_chosen, val_chosen):
#    if len(val_chosen) == 0:
#        return dash.no_update, {"color": color_chosen}
#    else:
#        dff = df[df["state"].isin(val_chosen)]
#        fig = px.pie(dff, values="pop", names="state", title="Malaysia Population")
#        fig.update_traces(textinfo="value+percent").update_layout(title_x=0.5)
#        return fig, {"color": color_chosen}


if __name__ == '__main__':
    app.run_server(debug=True)