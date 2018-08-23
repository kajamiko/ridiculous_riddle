
# Ridiculous Riddle Quiz


Ridiculous Riddle is an online quiz application, testing user's knowledge about coding in Python and Flask.

On each question page, it counts down points for user to score, from 10 downwards.
 
## UX
 
Website is created for everyone looking to check they're coding knowledge

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user type, I want to perform an action, so that I can achieve a goal.

This section is also where you would share links to any wireframes, mockups, diagrams etc.

## Features

Index page - welcomes user and allows him to choose a username.

Next page is a user page, describing shortly app's functionality.

Game page, where all the magic happens.

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
- [Python](https://www.python.org/)
    - The project's back-end was written in **Python** .
- [Flask](http://flask.pocoo.org/)
    - project was built **flask** microframework due to its simplicity.



## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

The back end has been tested thoroughly using unitttest. I have tested views to see if functions give desired results.

M

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](ht

### Media
- The photos used in this site were obtained from [Pixabay](https://pixabay.com/)

### Acknowledgements

- I received inspiration for this project from X