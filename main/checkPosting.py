from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def is_posted_successfully(wait_driver):
    post_shared_xpath =  "//h3[text()='Your post has been shared.']"
    try:
        wait_driver.until(EC.presence_of_element_located((By.XPATH, post_shared_xpath)))
    except TimeoutException:
        return False
    else:
        return True