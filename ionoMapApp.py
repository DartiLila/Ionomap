import dash
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# This is used to link the app to the server
server = app.server
app.config.suppress_callback_exceptions = True