from ionoMapApp import app
from ionoMapApp import server
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from map import *


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children = [html.H1('IonoMap',
                               style={'color': 'white',
                                      'textAlign': 'center',
                                      #'background': 'black'
                                    }),
                       html.Img(src=app.get_asset_url('Map.png'), height=600,
                                style={'margin-left': '335px',
                                       'position': 'fixed',
                                       'margin-right': '100px',
                                       'background': '#111111'})])

if __name__ == '__main__':
    app.run_server(debug=True)
