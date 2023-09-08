from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd
import dash

app = Dash(__name__)
server = app.server

image_path = 'https://www.mmu.edu.my/wp-content/themes/mmu2018/assets/images/logo-mmu.png'
data_path = 'https://raw.githubusercontent.com/YeeJieYao/Project/main/population.csv'

df = pd.read_csv(data_path)
fig = px.pie(df,values='pop_60', names='state',title='Malaysia Population') .update_layout(xaxis_title="State", yaxis_title="Index")

colors = ["black", "blue", "red", "yellow", "pink", "orange"]

app.layout = html.Div(
    children=[html.H1("Data Visualization"),
    dcc.Dropdown(['Johor', 'Kedah', 'Kelantan','Melaka', 'Negeri Sembilan', 'Pahang', 'Pulau Pinang', 'Perak', 'Perlis', 'Selangor', 'Terengganu', 'Sabah', 'Sarawak', 'W.P. Kuala Lumpur', 'W.P. Labuan', 'W.P. Putrajaya'],
                 'Johor', id='my-dropdown'),
    html.Button(id='my-button', n_clicks=0, children="Show breakdown"),
    dcc.Graph(id='graph-output', figure ={})
    ]
)

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
        dff = df[df["fund_extended_name"].isin(val_chosen)]
        fig = px.pie(dff, values="ytd_return", names="fund_extended_name", title="Year-to-Date Returns")
        fig.update_traces(textinfo="value+percent").update_layout(title_x=0.5)
        return fig
    elif len(val_chosen) == 0:
        raise dash.exceptions.PreventUpdate



if __name__ == '__main__':
    app.run_server(debug=True)