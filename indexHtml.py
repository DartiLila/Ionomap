from ionoMapApp import app
from ionoMapApp import server
from dash import html
from dash import dcc

app.layout = html.Div([html.H1('IonoMap',
                                style={'color': 'white',
                                'textAlign': 'center',
                                "background": "black"}),
                       html.Img(id='Map')])

if __name__ == '__main__':
    app.run_server(debug=True)