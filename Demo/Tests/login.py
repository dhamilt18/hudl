import time
import sys
import os

# allows for running in terminal
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from Demo.Pages.loginPage import LoginPage

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

# enter in your username and password here
myusername = ""
mypassword = ""


# list of errors
list_of_failed_tests = []
list_of_failed_tests.clear()
list_of_passing_tests = []
list_of_passing_tests.clear()

# Happy path test
def test_login_valid():
    print("Executing testcase: Valid login")
    login = LoginPage(driver)
    driver.get("https://hudl.com/login")
    login.enter_username(myusername)
    login.enter_password(mypassword)
    time.sleep(1)
    login.click_login_btn()
    time.sleep(1)
    try:
        if driver.title != "Home - Hudl":
            assert driver.title == "Home - Hudl", "Test failed"
        else:
            list_of_passing_tests.append("Testcase: Valid login")
            print("")
    except AssertionError as error:
        print("")
        list_of_failed_tests.append("Testcase: Valid login")
    time.sleep(2)


def test_login_wrong_username():
    print("Executing testcase: Wrong username...")
    login = LoginPage(driver)
    driver.get("https://hudl.com/login")
    login.enter_username("abcdefg@gmail.com")
    login.enter_password(mypassword)
    time.sleep(1)
    login.click_login_btn()
    # assert that we see invalid msg
    time.sleep(2)
    message = driver.find_element("css selector", login.message_css).text
    try:
        if message != "We didn't recognize that email and/or password.Need help?":
            assert message == "We didn't recognize that email and/or password.Need help?", "Test failed"
        else:
            list_of_passing_tests.append("Testcase: Wrong username")
            print("")
    except AssertionError as error:
        print("")
        list_of_failed_tests.append("Testcase: Wrong username")

    time.sleep(2)


def test_login_wrong_password():
    print("Executing testcase: Wrong password...")
    login = LoginPage(driver)
    driver.get("https://hudl.com/login")
    login.enter_username(myusername)
    login.enter_password("asdf123")
    time.sleep(1)
    login.click_login_btn()
    # verify that we see invalid msg
    time.sleep(2)
    message = driver.find_element("css selector", login.message_css).text
    try:
        if message != "We didn't recognize that email and/or password.Need help?":
            assert message == "We didn't recognize that email and/or password.Need help?", "Test Failed"
        else:
            list_of_passing_tests.append("Testcase: Wrong password")
            print("")
    except AssertionError as error:
        print("")
        list_of_failed_tests.append("Testcase: Wrong password")
    time.sleep(2)


def test_login_page_elements_visible():
    print("Executing testcase: Find all elements...")
    login = LoginPage(driver)
    driver.get("https://hudl.com/login")
    time.sleep(2)
    try:
        if not login.check_elements():
            assert "Find all elements testcase FAILED"
        else:
            list_of_passing_tests.append("Testcase: Find all elements")
            print("")
    except NoSuchElementException as error:
        print("")
        list_of_failed_tests.append("Testcase: Find all elements")
        time.sleep(2)


def test_username_no_password():
    print("Executing testcase: Username with no password")
    login = LoginPage(driver)
    driver.get("https://hudl.com/login")
    login.enter_username(myusername)
    time.sleep(1)
    login.click_login_btn()
    time.sleep(1)
    message = driver.find_element("css selector", login.message_css).text
    try:
        if message != "We didn't recognize that email and/or password.Need help?":
            assert message == "We didn't recognize that email and/or password.Need help", "Test failed"
        else:
            list_of_passing_tests.append("Testcase: Username with no password")
            print("")
    except AssertionError as error:
        print("")
        list_of_failed_tests.append("Testcase: Username with no password")
        time.sleep(2)


def test_password_no_username():
    print("Executing testcase: Password with no username")
    login = LoginPage(driver)
    driver.get("https://hudl.com/login")
    login.enter_password(mypassword)
    time.sleep(1)
    login.click_login_btn()
    time.sleep(1)
    message = driver.find_element("css selector", login.message_css).text
    try:
        if message != "We didn't recognize that email and/or password.Need help?a":
            assert message == "We didn't recognize that email and/or password.Need help?a", "Test failed"
        else:
            list_of_passing_tests.append("Testcase: Password with no usernane")
            print("")
    except AssertionError as error:
        print("")
        list_of_failed_tests.append("Testcase: Password with no username")



# run these tests:
test_login_page_elements_visible()
test_login_wrong_username()
test_login_wrong_password()
test_login_valid()
test_username_no_password()
test_password_no_username()

driver.close()
driver.quit()
# display results of tests
print("ALL Tests are COMPLETED, summary of tests results: ")
print("...")
print("...")
print("...")
# report if any tests failed
print("Passing Tests:")
for i in list_of_passing_tests:
    print(i)

print("")
print("Failed Tests:")
for i in list_of_failed_tests:
    print(i)
