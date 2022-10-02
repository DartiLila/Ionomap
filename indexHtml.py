from threading import Thread
from ionoMapApp import app
from ionoMapApp import server
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from mapp import *
from PIL import Image


def convertImage():
    img = Image.open("assets/Map.png")
    img = img.convert("RGBA")

    datas = img.getdata()

    newData = []

    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save("assets/NewMap.png", "PNG")
    print("Successful")


convertImage()

background = Image.open("assets/MapOfWorld.png")
foreground = Image.open("assets/NewMap.png")

background.paste(foreground, (0, 0), foreground)

app.layout = html.Div([html.H1('IonoMap',
                               style={'color': 'white',
                                      'textAlign': 'center',
                                      'background': 'black'}),
                       html.Img(src=app.get_asset_url('MapOfWorld.png'),height = 600,
                                style={'margin-left': '335px',
                                       'margin-right': '100px',}),
                       html.Img(src=app.get_asset_url('Map.png'),height = 600,
                                style={'margin-left': '335px',
                                       'margin-right': '100px',})])

if __name__ == '__main__':
    app.run_server(debug=True)