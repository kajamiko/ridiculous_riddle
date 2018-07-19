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
                flash("This name has been used already.")
                break
        file.close() 
        with open("data/users.txt", "a") as file:
            if name_exists == False:

                file.write(request.form["username"] + "\n")
                return redirect(request.form["username"])
    return render_template('index.html')
    
@app.route('/<username>', methods=["GET","POST"])
def user(username):
    # user starting page, with an encouraging image and a simple form with start button
    
    if request.method == "POST":
        level="1"
        score="0"
        return redirect(url_for('game', username=username, level=level, score=score))
        
    return render_template('user.html', username = username)
    

@app.route("/game/<username>/<level>", methods=["GET","POST"])
def game(username, level):
    """ This function creates instance game page, where riddles are displayed.
    After clicking submit, the json file is being checked for riddle with specific number stored as level, then
    the data are copied to a 3-element list.
    """
    rlist = []
    # displaying riddle
    with open("data/riddles.json", "r") as json_data:
        riddle_data = json.load(json_data)
        for obj in riddle_data:
            if obj["level"] == level:
                # Finds proper riddle
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
                    return redirect(url_for('game', username=username, level=new_level)) # score = new_score
                else:
                    
                    return redirect(url_for('game_over', username=username)) # score = new_score
            else:
                flash("Oops! Wrong! The answer is not {}".format(request.form["answer"]))
                return redirect(url_for('game', username=username, level=new_level)) #score = score
                
    return render_template('game.html',
    riddle_text = rlist[0],
    riddle_image= rlist[2],
    username=username,
    level=level)       


@app.route('/game_over/<username>/<score>', methods=["GET"])
def game_over(username, score):
    """

    This function takes score as parameter, then reads the records file and checks if the score's been higher.
    If positive, re-writes file with new records (let's say 10).
    Version 1: just checking if it's writing to a file - fine, works
    Version 2 : check reading from file

    """
    #make a dictionary out of the data
    data = {}
    data.setdefault(username, score)
    lb_file = open("data/leaderboard.json", "r")
    lb_data = json.load(lb_file)
    lb_file.close()
    
    # if there's less than 10 records, dump into the file, whatever the score
    if(len(lb_data)<6):
        for name, points in lb_data.items():
            data[name] = points
        outfile = open("data/leaderboard.json", "w")
        json.dump(data, outfile)
        outfile.close()
    else:
    
        popout = int(min(lb_data.values()))
        #check if score isn't higher than any of the highest scores so far
        if int(score) >= popout:
           # if it is pop the lowest out
            pop = ""
            for name, points in lb_data.items():
                # just in case if there's many users with the same score
                #make sure only one, random record will be deleted
                if points == popout:
                    pop = name
                data[name] = points
            del data[pop]
               
            with open('data/leaderboard.json', 'w') as outfile:
                json.dump(data, outfile)
    return render_template('game_over.html', username=username)
    
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=(int(os.getenv('PORT'))), debug=True)