import os
import json
from flask import Flask, render_template, request, redirect, flash


app = Flask(__name__)
app.secret_key = "some_secrets"

@app.route('/', methods=["GET", "POST"])
def index():
    """Welcome page with a form to send username and start game"""
    if request.method == "POST":
        return redirect(request.form["username"])
    return render_template('index.html')
    
@app.route('/<username>', methods=["GET","POST"])
def user(username):
    # user starting page, with an encouraging image and a simple form with start button
    #score = 0
 
    if request.method == "POST":
        return redirect(username)
    return render_template('user.html', username = username)

@app.route("/<username>/<level>", methods=["GET","POST"])
def game(username, level):
    """ The instance game page, where riddles and score will be displayed  """
    # Opening file with our riddles
    riddle_text = ""
    with open("data/riddles.json", "r") as json_data:
        riddle_data = json.load(json_data)
        for obj in riddle_data:
            if obj["level"] == level:
                riddle_text = obj["riddle"]
                """
                if obj["answer"] == request.form["answer"]:
                    return redirect('game.html', username = username, level=level+1)
                else:
                    flash("<h2>Oops! Wrong! The answer is not<br>{}</h2>".format(request.form["answer"]))
                """
            
    return render_template('game.html',
    riddle_text = riddle_text,
    username = username,
    level=level,)       

app.run(host=os.getenv('IP'), port=(int(os.getenv('PORT'))), debug=True)