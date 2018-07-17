import os
import json
import re
from flask import Flask, render_template, request, redirect, flash, url_for


app = Flask(__name__)
app.secret_key = "ab5t5gdfnmk34322bum"



@app.route('/', methods=["GET", "POST"])
def index():
    """Welcome page with a form to send username and start game"""
    if request.method == "POST":
        
       
        name_exists = False
        
        file = open("data/users.txt", "r")
        for line in file:
            if request.form["username"] in line:
                name_exists = True
                flash("Choose a different username")
                break
        file.close() 
        with open("data/users.txt", "a") as file:
            if name_exists == False:

                file.write(request.form["username"] + "\n")
                return redirect(request.form["username"])
    return render_template('index.html')
    
@app.route('/<username>', methods=["GET","POST"])
def user(username, game_over=False):
    # user starting page, with an encouraging image and a simple form with start button
    
    if request.method == "POST":
        level="1"
        return redirect(url_for('game', username=username, level=level))
    if game_over :
        """
        
        """
        with open("data/users.txt", "r") as file:
            data = file.readlines()
            for line in data:
                words = line.split()
        return render_template('game_over', username=username, words=words)
    return render_template('user.html', username = username)
    



@app.route("/game/<username>/<level>", methods=["GET","POST"])
def game(username, level):
    """ This function creates instance game page, where riddles are displayed.
    After clicking submit, the json file is being checked for riddle with specific number stored as level, then
    the data are copied to a 3-element list.
    """
    rlist = []
    with open("data/riddles.json", "r") as json_data:
        riddle_data = json.load(json_data)
        for obj in riddle_data:
            if obj["level"] == level:
                """
                Finds proper riddle
                """
                rlist.append(obj["riddle"])
                rlist.append(obj["answer"])
                rlist.append(obj["img_source"])
        if request.method == "POST":
            if rlist[1].lower() == request.form["answer"].lower():
                """
                When the answer is correct...
                """
                if int(level) <= len(riddle_data):
                    """If the level value is still smaller or same as the number of riddle objects - if there are still 
                    any riddles to answer - then we get another view with the next riddle. Otherwise, gets back to user view with leaderboard"""
                    
                    new_level = str(int(level) + 1)
                    return redirect(url_for('game', username=username, level=new_level))
                else:
                    return render_template('user.html', username = username, game_over=True)
            else:
                flash("Oops! Wrong! The answer is not {}".format(request.form["answer"]))
                
    return render_template('game.html',
    riddle_text = rlist[0],
    riddle_image= rlist[2],
    username=username,
    level=level)       

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=(int(os.getenv('PORT'))), debug=True)