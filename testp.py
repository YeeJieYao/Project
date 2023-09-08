from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd

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
    dcc.Graph(id='graph-output', figure ={}),
    html.Div(id="sentence-output", children=["This is the color I love"], style={}),
        dcc.RadioItems(id='my-radioitem', value="black", options=[{'label': c, 'value': c} for c in colors]),
    ]
)





if __name__ == '__main__':
    app.run_server(debug=True)