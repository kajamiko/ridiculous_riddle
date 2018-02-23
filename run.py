import os
from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    """Welcome page with a form to send username and start game"""
    if request.method == "POST":
        return redirect(request.form["username"])
    return render_template('index.html')
    
@app.route('/<username>')
def game(username):
    """The instance game page, where riddles and score will be displayed  """
    return render_template('game.html', username= username)

app.run(host=os.getenv('IP'), port=(int(os.getenv('PORT'))), debug=True)