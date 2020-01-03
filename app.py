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
Blog post page
'''
@server.route('/blog', methods=['GET'])
def blog():
    return render_template('blog.html')

@server.route('/post-1', methods=['GET'])
def post1():
    post_dict = {'id':1,
                "title": "Blogging about Blogging",
                "content1": "I blame blogs (and Pinterest) for every creative skill I have acquired. I could call a lot of these skills 'self-taught', but 'blog-taught' is a far more accurate claim. Because so many of my hobbies are particularly bloggable, I have considered starting a blog many times before. I have always talked myself out of it, thinking there was never enough content, or I couldn't pick just one subject, or that no one would read it.",
                "content2": "Honestly, none of those thoughts have changed much. Rather, they no longer seem like reasons not to blog. Perhaps I have reached an age that I accept that I will not always remember how to do something just because I did it once before. Alas, I'll blog for myself. If you happen to be reading this, and if you are not me, then I guess I'll blog for you, too.",
                "category": "Miscellany",
                "img1": "static/images/work_stock5.jpg",
                "cred1": "Photo by Lisa Fotios on Unsplash",
                "img2": "static/images/write1.jpg",
                "cred2": "Photo by Aaron Burden on Unsplash",
                "tags": ["hobbies", "interests"],
                "len":2}
    return render_template('post.html', **post_dict)

@server.route('/post-2', methods=['GET'])
def post2():
    post_dict = {'id': 2,
                'title': "Blogging about Tech Blogging",
                'content1': " My recent transition into the tech industry has made me more grateful than ever for folks who document and share their learning experiences. Data science is particularly rich in community resources and support. I have come to discover that the best explanations aren't always from the most senior contributors. I want to make a habit of contributing my own perspective while I still vividly recall the experience of being a new coder. ", 
                'content2': "The first learning experience worth noting is the making of this website. I am not a web developer, so this is likely to be a work in long-term progress. I am currently working on expanding the blog component of my site, as it was one of my main motivations for creating this site. Soon, I will add posts about the process of making my website, among other topics. In the meantime, I have expanded on a number of my interests as a handy excuse to broaden my knowledge of crafting websites.",
                'category': "Miscellany",
                'img1': "static/images/work_stock2.jpg",
                'cred1': "Image by Ken Tomita on Pexels",
                'img2': "static/images/work_stock6.jpg",
                'cred2': "Image by Pixabay on Pexels",
                'tags': ["blog", "data science", "interests"],
                'len': 3 }
    return render_template('post.html', **post_dict)

@server.route('/post-3', methods=['GET'])
def post3():
    post_dict = {'id': 3,
                'title': "An Introvert's Guide to Networking (Part 1)",
                'content1': "Just the thought of 'Networking' makes me uncomfortable. I (unfairly) associate it with huge crowds of schmoozers having disingenuous interactions motivated by self-interest. Coming from the nonprofit/government sector, where I got interviews for 80 percent of online applications I submitted, I have never felt so much pressure to network. As the title implies, I plan to write a series of posts with suggestions for anyone else who fears networking, but is determined to do it anyway. I am not an expert in networking, but I have 30 years of experience in introverting. Perhaps these will balance out to yield some practical advice. If not, tell me what you think!", 
                'content2': "So… Meetups.  I have been actively exploring Seattle's tech meetups for three months, since mid-September 2019. I've heard the same advice from several different people, so it's probably worth noting. 'It's better to attend a few groups regularly than to attend many different groups once.' I'd rate this as 95 percent accurate. I follow the spirit of the advice. I am a regular at PuPPy & Data Circles, which is the new name of Seattle Women in Data Science (SeaWiDS). However, I follow 56 tech groups on the Meetup app. I've also been to events hosted by at least 12 of them. Some of the best events I've attended have been by groups that haven't hosted anything else since. I could (and will) write a blog about what factors I think contribute to a 'great' event, but current point is that there are a number of advantages to casting a wide net when looking for events to attend.", 
                'category': "Miscellany",
                'img1': "static/images/introvert.png",
                'cred1': "Photo by Urban Threads",
                'img2': "static/images/work_stock12.jpg",
                'cred2': "Image by Александар Цветановић on Pexels",
                'tags': ["blog", "data science", "community"] ,
                'len': 3}
    return render_template('post3.html', **post_dict)

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
