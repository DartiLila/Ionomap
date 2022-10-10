import dash
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# This is used to link the app to the server
app = dash.Dash("Ionomap", external_stylesheets=external_stylesheets)
server = app.server
app.config.suppress_callback_exceptions = True