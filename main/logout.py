from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def logout(wait_driver):
    more_options_xpath = "//svg[contains(@aria-label, 'Settings')]"
    log_out_xpath = "//div[@class='xq9evs9']/descendant::span[text()='Log out']"
    
    more_options_element = wait_driver.until(EC.element_to_be_clickable((By.XPATH, more_options_xpath)))
    more_options_element.click()   

    log_out_element = wait_driver.until(EC.element_to_be_clickable((By.XPATH, log_out_xpath)))
    log_out_element.click()
