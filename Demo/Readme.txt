To test:
1 - Install most recent version of Pycharm (or preferred IDE)
2 - Install most recent version of Selenium
3 - Install most recent version of Python
4 - Pull down repo to your local
5a - Open in your preferred IDE
5b - Or navigate to the directory in terminal
6a - In your IDE run login.py
6b - In terminal run 'py -m login'

Test Cases automated:
These test cases were automated because they are high priority due to high risk.
1 - happy path
2 - wrong username
3 - wrong password
4 - verify elements are present
5 - submitting with no password
6 - submitting with no username

The below I would create/check testcase for; however, I would not automate them:

7 - Spam clicking the `Log-In` button
    - while this is moderate risk area, we could cover this via monitoring and manual regression
8 - Logging in with 'Remember me' checked
    - this is a low risk as it's failure would not break core functionality of the app


If I had more time I would:
1 - Update structure to include step definitions for reuseability
2 - Separate each individual test case and create a script to run them as a "regression"
3 - Remove explicit waits
4 - Code refactor