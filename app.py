from flask import Flask, request, render_template
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

server = Flask(__name__)

''' 
4 main pages
'''

@server.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@server.route('/career', methods=['GET'])
def career():
    return render_template('career.html')

@server.route('/hobbies', methods=['GET'])
def hobbies():
    return render_template('hobbies.html')

@server.route('/travel', methods=['GET'])
def interests():
    return render_template('travel.html')

''' 
Resume page
'''

@server.route('/resume', methods=['GET'])
def resume():
    return render_template('resume.html')

''' 
Picture gallery pages.
'''

@server.route('/hobbies_sewing', methods=['GET'])
def sew_pics():
    return render_template('sew_pics.html')

@server.route('/hobbies_embroidery', methods=['GET'])
def emb_pics():
    return render_template('emb_pics.html')

@server.route('/hobbies_vinyl', methods=['GET'])
def vinyl_pics():
    return render_template('vinyl_pics.html')

@server.route('/hobbies_crochet', methods=['GET'])
def crochet_pics():
    return render_template('crochet_pics.html')

@server.route('/hobbies_baking', methods=['GET'])
def baking_pics():
    return render_template('baking_pics.html')

@server.route('/hobbies_misc', methods=['GET'])
def misc_pics():
    return render_template('misc_pics.html')

# @server.route('/pets', methods=['GET'])
# def pets():
#     return render_template('petsitting.html')

app = dash.Dash(    __name__,
    server=server,
    routes_pathname_prefix='/dash/')

df = pd.read_csv('world_travel.csv')

data = [ go.Scattergeo(
        lon = df[df.reason == i]['long'],
        lat = df[df.reason == i]['lat'],
        text = df[df.reason == i]['text'],
        mode = 'markers',
        marker = dict(
            size = 5,
            opacity = 1,
            reversescale = True,
            autocolorscale = False,
            # symbol = 'square',
            line = dict(width=.5, 
                        color='white')),
            name = str(i)
        ) for i in df.reason.unique() ]

layout = dict(
        title=go.layout.Title(text=""),
        colorbar = True,
        margin = dict(t = 0, b = 0, l = 0, r = 0),
        legend=go.layout.Legend(x=.2,y=-.05,
                                traceorder="normal",
                                orientation='h',
                                font=dict(family="times-new-roman",
                                          size=12,
                                          color="black")
                                ),
        geo = dict(
            scope='world',
            projection=dict( type='natural earth' ),
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5
        ))

# assigning the annotations to the layout
# layout['annotations'] = annotations

fig = dict( data=data, layout=layout )    
# fig.update_layout(legend_orientation="h")

app.layout  = html.Div([
    dcc.Graph(id='graph', figure=fig)
])

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=80, debug=True)
