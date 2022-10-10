import dash

external_stylesheets = ['C:/Users/User/Documents/GitHub/Ionomap/assets/Ionostyle.css']
# This is used to link the app to the server
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Ionomap"
server = app.server
app.config.suppress_callback_exceptions = True