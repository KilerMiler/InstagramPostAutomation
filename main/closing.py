from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def close_shared_sub_window(wait_driver):
    cross_xpath = "//svg[contains(@aria-label, 'Close')]"
    close_btn = wait_driver.until(EC.element_to_be_clickable((By.XPATH, cross_xpath)))
    close_btn.click()