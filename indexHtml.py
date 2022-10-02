from threading import Thread
from ionoMapApp import app
from ionoMapApp import server
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from mapp import *

colors = {
    'background': '#111111',
    'background2': '#FF0',
    'text': 'green'
}

app.layout = html.Div([html.H1('IonoMap',
                               style={'color': 'white',
                                      'textAlign': 'center',
                                      'background': 'black'}),
                       html.Img(src='\GitHub\Ionomap\Map.png')])

if __name__ == '__main__':
    app.run_server(debug=True)