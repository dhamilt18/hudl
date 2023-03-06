class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.login_button_css = "button[data-qa-id=login-btn]"
        self.username_email_css = "input[data-qa-id=email-input]"
        self.password_css = "input[data-qa-id=password-input]"
        self.sso_button_css = "button[data-qa-id=log-in-with-organization-btn]"
        self.message_css = "p[data-qa-id=error-display]"
        self.signup_button_text = "Sign up"
        self.remember_me_checkbox_css = "label[data-qa-id=remember-me-checkbox-label]"
        self.need_help_css = "a[data-qa-id=need-help-link]"

    def click_login_btn(self):
        self.driver.find_element("css selector", self.login_button_css).click()

    def enter_username(self, username):
        # clear the input first then send email
        self.driver.find_element("css selector", self.username_email_css).clear()
        self.driver.find_element("css selector", self.username_email_css).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element("css selector", self.password_css).clear()
        self.driver.find_element("css selector", self.password_css).send_keys(password)

    def signup_button(self):
        self.driver.find_element("link text", self.signup_button_text)

    def check_elements(self):
        signup_element = self.driver.find_element("link text", self.signup_button_text)
        if signup_element:
            print("Signup element displayed!")

        username_element = self.driver.find_element("css selector", self.username_email_css)
        if username_element:
            print("Username element displayed!")
        password_element = self.driver.find_element("css selector", self.password_css)

        if password_element:
            print("Password element displayed!")

        login_button_element = self.driver.find_element("css selector", self.login_button_css)
        if login_button_element:
            print("Login button element displayed!")

        remember_checkbox_element = self.driver.find_element("css selector", self.remember_me_checkbox_css)
        if remember_checkbox_element:
            print("Remember checkbox element displayed!")

        help_link_element = self.driver.find_element("css selector", self.need_help_css)
        if help_link_element:
            print("Need help link element displayed!")

        sso_link_element = self.driver.find_element("css selector", self.sso_button_css)
        if sso_link_element:
            print("Log in with organization link element displayed!")
