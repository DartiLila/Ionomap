import html
from ionoMapApp import app


colors = {
    'background': '#111111',
    'text': '#4F8A39'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children = [html.H1('IonoMap',
                               style={'color': colors['text'],
                                      'textAlign': 'center',
                                      'background': 'black'
                                    }),
                       html.Div(style={'backgroundColor': colors['background']}, children = [html.H1('IonoMap',
                               style={'color': colors['text'],
                                      'textAlign': 'center',
                                      'background': 'black'
                                    }),
                       html.Img(src=app.get_asset_url('Map.png'), height=600,
                                style={'position': 'fixed',
                                       })])])


if __name__ == '__main__':
    app.run_server(debug=True)
