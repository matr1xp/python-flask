from flask import Flask
app = Flask(__name__)

# Classic Hello World    
@app.route('/hello')
def hello_world():
    return 'Hello, World!'
    
# Routing  
@app.route('/')
def index():
    return 'Index Page'
    
@app.route('/about') # this one works on exact match
def about():
    return 'About Page'
    
@app.route('/projects/') # this works even without trailing /
def projects():
    return 'The project page'

    