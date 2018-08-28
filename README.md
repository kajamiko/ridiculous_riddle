
# Ridiculous Riddle Quiz


Ridiculous Riddle is an online quiz application, testing user's knowledge and speed in reading and typing.
On each question page, it counts down points for user to score, from 10 downwards.
Questions are read form JSON format file. Any set of questions and links to images can be loaded. For demonstration purposes, I have used set questions about Python and Flask 
 
## UX
 
Website is created for everyone looking to check their knowledge and have fun in the same time.

- As a quiz designer, I want to have a possibility to keep questions, answers and links to images in one file. 

- As a quiz user, I want to see how quickly I answer questions to improve my knowledge and speed.

## Features

Index page - welcomes user and allows him to choose a username.

Next page is a user page, describing shortly app's functionality.

Game page, where the questions and images are displayed, and uesr can answer.

End of the game page, showing detailed scoring.

Leaderboard is a page displaying 6 best results.

Cheating prevention page is showing only if user enters unallowed values in the browser bar.

Error page may happen to be displayed, as the app's functionality relies on session cookie.
 
### Existing Features


1. Index page - user can choose username, that is posted to the next view. It also has basic validation, both javascript-based and in the back-end.

2. User page - shows a paragraph describing game's functionality, but under the bonnet it is also initializing important user data, which are level, score and session dictionary.

3. Game [python part] - is reading proper question from file ('static/data/riddles.json'). It puts the data ( question, answer, image source and level number) into a python list, that is later passed to a template to parse.
After user submits answer, it is checking if it's correct.
The function is also processing initial score, and adding new points that are posted along with the answer. Points earned for each level are stored in session. If points argument doesn't match expectations, it redirects to another view.
If there is no more questions left in the riddles.json file, page is redirected to the 'game_over' function.

4. Game [javascript part] - javascript function in ('static/js/score_counter.js') is counting down time for user to answer. Page may be reloaded when a wrong answer is submitted, and in this case user has another chance to answer.

5. End of the game feature - it checks the overall score again, including redirecting if cheated, and then, if it's one of the highest so far, writes it in the leaderboard file.

6. Leaderboard page is displaying the content of the leaderboard.json file.

7. Cheating prevention feature - if the app detects some inconsistency in scoring, it redirects to a separate page, where user is offered to choose either go back to where he was.

8. Restarting feature - it simply clears session from particular user's data. 

9. Error handling - in case of an error, it displays custom page. 

### Features removed

There was also a possibility of putting username on a banned users list, but it was impractical.

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- HTML and CSS
    - project uses **HTML** and **CSS** to build webpages.
-  [Bootstrap](https://getbootstrap.com/)
    -project uses **Bootstrap** for webpages' layout.
- [Javascript](https://www.javascript.com/) 
    -The project uses **Javascript** to enhance pages functionality.
- [JQuery](https://jquery.com)
    - The project is using Bootstrap's **JQuery** for responsiveness.
- [JSON](https://www.json.org/)
    - **JSON** was used to organise data in files.
- [Python](https://www.python.org/)
    - The project's back-end was written in **Python** .
- [Flask](http://flask.pocoo.org/)
    - project was built **flask** microframework due to its simplicity.
    - project uses **flask.session** for session functionality. 

## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

The back end has been tested thoroughly using unitttest. I have tested views to see if functions give desired results. For each of them, I' ve tested:
- urls responsiveness
- response's status code, as sometimes it proves functionality - depending on scenario, it would refresh or redirect
- post request, where relevant - by mocking form submission and then checking response (status_code and location)
- templates used, however not straightforward in flask without installing some libraries, was checked by testing 'response.data' (asserting some strings typical to the exected template)
- following changes in files, when expected ('leaderboard' view)

However, after adding session to avoid cheating on scoring, my automated tests for some views are not working anymore, probably due to bad configuring. I could not find solution for this problem.
For all views accessing session, I can only provide manual tests scenarios.
Therefore, I kept all the working code with no session functionality and with a full test file, on 'older_tested' branch. All the automated tests can only be run on this branch.

Deployed verrsion (the one with session functionality) of the app is on master branch, with not every automated test working. 

### Automated tests for deployed version:

1. 'index' view:
    - `test_homepage(self)` -  GET request tested for status code and template
    - `test_homepage_post(self)` POST request tested for posting data, 'status_code'if redirecting
    
2. 'user' view:
    - `test_user_page_for_loading(self)` -  GET request tested for status code and template
    - `test_user_page_posting(self)` -  POST request tested for posting data, 'status_code'if redirecting, and response.location for where is redirected

3. 'Game' view:
    - `test_game_page_for_loading(self):` - GET request tested for status code and template. Returns None and redirects to error page
    - `test_game_page_for_responding(self):` - POST request tested for posting data, 'status_code'if redirecting, and response.location for where is redirected. Returns None

4. 'Game_over' view:
    -`test_game_over_for_responding(self)` - GET request tested for status code and template. Returns None

5. 'Leaderboard' view:
    - `test_leaderboard(self)` - GET request tested for status code and template

6. 'Cheating_prevent' view:
    - `test_cheating_prevention(self)` - GET request tested for status code and template. Returns None

All tests can be found in test.py file.
Note: all of the views, that cannot be tested automatically, rely heavily on session. Please see next section

### Manual tests for deployed version:
1. 'Game' view:
    1. After submitting username and starting the actual game, the game page will load. Please verify that overall score at the top of the page is currently 0.
    2. The progress bar and info right under will show how many points will be scored if answer is submitted .
    3. Try to type an incorrect answer to a question displayed and submit it, to verify that the page will be reloaded with wrong answer message. If that is not a first
        question, please note that no points were added for the answer.
    4. Try to submit nothing - it should do the same as above.
    5. Try to submit a right answer. New question should appear and points should be added to the overall score displayed at the top of the page.
    6. When all the answers has been submitted, the page should be redirected to the 'game_over' view.

2. 'Game_over' view:
    1. It should be displaying user's points for each question.
    2. Try to hit 'Go back to your questions' button. Verify that it redirected to the first question with information about points and overall scoring.
    3. Try to move back and forward through answered questions.
    4. The 'Reset' button will clear the session and this functionality won't be available anymore.
    5. Try to access your questions again through the browser bar. It will throw an exception and so redirect to 'page_gone' view.

3. 'Cheating_prevent' view:
    1. At any point of the game, either when question is loaded, or the game finished already, try to access question by typing too large value into the browser bar.Verify 
        that a page with a sleeping cat image will be displayed and you'll be offered to resume thee game with correct score.
    
4. 'Restart' view:
    1. When hitting 'Restart' button, the session will be cleared.

The project has been tested on various browsers, including Chrome, Edge, Opera, and Safari. 

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- All Python questions used in application are copied from [Python Prograzmiz Quizes](https://www.programiz.com/python-programming/quiz).

### Media
- The photos used in this site were obtained from [Pixabay](https://pixabay.com/).
- Icons used in the project were obtained from [Font Awesome](https://fontawesome.com/icons).
- The favicon was obtained from [Flaticon.com](https://www.flaticon.com/).

#### All image files are stored in static/media.
### Acknowledgements