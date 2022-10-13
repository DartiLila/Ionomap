from dash import html
from ionoMapApp import app


colors = {
    'background': '#111111',
    'text': '#4F8A39'
}

app.layout = html.Div()


if __name__ == '__main__':
    app.run_server(debug=True)
