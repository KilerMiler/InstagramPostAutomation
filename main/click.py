from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def click_reel_ok(wait_driver):
    OK_btn_xpath = "//button[text()='OK']"
    try:
        OK_btn = wait_driver.until(EC.element_to_be_clickable((By.XPATH, OK_btn_xpath)))
    except TimeoutException:
        return False
    else:
        OK_btn.click()
        return True