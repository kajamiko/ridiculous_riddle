import os
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello! I'm working! Yay!"
    
    

app.run(host=os.getenv('IP'), port=(int(os.getenv('PORT'))), debug=True)