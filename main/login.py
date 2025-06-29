from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

def login_account(username, password, wait_driver):
    username_element_name = "username"
    password_element_name = "password"
    
    username_element = wait_driver.until(EC.element_to_be_clickable((By.NAME, username_element_name)))
    
    password_element = wait_driver.until(EC.element_to_be_clickable((By.NAME, password_element_name)))

    username_element.send_keys(username)
    password_element.send_keys(password)

    password_element.send_keys(Keys.ENTER)