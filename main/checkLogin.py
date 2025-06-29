from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def is_user_logged_in_successfully(driver):
    unable_to_login_xpath = "//div[text()='Sorry, your password was incorrect. Please double-check your password.']"
    
    try:
        driver.find_element(By.XPATH, unable_to_login_xpath)
    except NoSuchElementException:
        return True
    else:
        return False