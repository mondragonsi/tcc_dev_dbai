import dash
import plotly.express as px
import pandas as pd
from dash import html, dcc  # Importando dcc corretamente

app = dash.Dash(__name__)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div("Dash é legal!"),
    dcc.Graph(figure=fig)
])

# Adicionando a capacidade de executar o servidor
if __name__ == '__main__':
    app.run_server(debug=True, port=8051)
