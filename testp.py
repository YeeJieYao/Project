from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd
import dash

app = Dash(__name__)
server = app.server

image_path = 'https://www.mmu.edu.my/wp-content/themes/mmu2018/assets/images/logo-mmu.png'
data_path = 'https://raw.githubusercontent.com/YeeJieYao/Project/main/population.csv'

df = pd.read_csv(data_path)
fig = px.pie(df,values='pop', names='state',title='Malaysia Population') .update_layout(xaxis_title="State", yaxis_title="Index")

app.layout = html.Div([
        html.Div([
            html.Pre(children= "Population",
            style={"text-align": "center", "font-size":"100%", "color":"black"})
        ]),

        html.Div([
            dcc.Graph(id='the_graph')
        ])

])





if __name__ == '__main__':
    app.run_server(debug=True)