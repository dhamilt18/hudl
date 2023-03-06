import time
import sys
import os

# allows for running in terminal
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from selenium import webdriver
from Demo.Pages.loginPage import LoginPage

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

# enter in your username and password here
myusername = "dhamilt18@gmail.com"
mypassword = "DgqXw&E65q1q*!zp"

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
    if driver.title == "Home - Hudl":
        print("Testcase: Valid login PASSED")
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
    if message == "We didn't recognize that email and/or password.Need help?":
        print("Testcase: Wrong username PASSED")
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
    if message == "We didn't recognize that email and/or password.Need help?":
        print("Testcase: Wrong password PASSED")
    time.sleep(2)


def test_login_page_elements_visible():
    print("Executing testcase: Find all elements...")
    login = LoginPage(driver)
    driver.get("https://hudl.com/login")
    time.sleep(2)
    login.check_elements()
    print("Find all elements testcase PASSED")
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
    if message == "We didn't recognize that email and/or password.Need help?":
        print("Testcase: Username with no password PASSED")
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
    if message == "We didn't recognize that email and/or password.Need help?":
        print("Testcase: Password with no username PASSED")


# run these tests:
test_login_page_elements_visible()
test_login_wrong_username()
test_login_wrong_password()
test_login_valid()
test_username_no_password()
test_password_no_username()

driver.close()
driver.quit()
print("ALL Tests are completed")
