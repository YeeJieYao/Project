from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd

app = Dash(__name__)
server = app.server

image_path = 'https://www.mmu.edu.my/wp-content/themes/mmu2018/assets/images/logo-mmu.png'
data_path = 'https://raw.githubusercontent.com/YeeJieYao/Project/main/population.csv'

df = pd.read_csv(data_path)
df2= df.iloc[1:]

fig = px.pie(df2,values='pop', names='state',title='Malaysia Population') .update_layout(xaxis_title="State", yaxis_title="Index")

dcc.Graph(figure = fig)

app.layout = html.Div(
    [html.Img(src=image_path),
    html.H1("Data Visualization"),
    html.H2("Dashboard showing graphs"),
    dcc.Checklist(['Johor', 'Kedah', 'Kelantan','Melaka', 'Negeri Sembilan', 'Pahang', 'Pulau Pinang', 'Perak', 'Perlis', 'Selangor', 'Terengganu', 'Sabah', 'Sarawak', 'W.P. Kuala Lumpur', 'W.P. Labuan', 'W.P. Putrajaya'],
              'Johor', id='my-checklist')]
)




if __name__ == '__main__':
    app.run_server(debug=True)