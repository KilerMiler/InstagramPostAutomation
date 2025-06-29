import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from main import click
import time

def post_content(file_path, wait_driver, isVideo=False):
    create_btn_css_selector = 'svg[aria-label="New post"][role="img"]'
    create_btn = wait_driver.until(EC.element_to_be_clickable((By.CSS_SELECTOR, create_btn_css_selector )))
    create_btn.click()

    file_input_css_selector = "div[role='dialog'] input[type='file']"
    file_input = wait_driver.until(EC.presence_of_element_located((By.CSS_SELECTOR, file_input_css_selector)))
    file_input.send_keys(os.path.abspath(file_path))

    if isVideo:
        click.click_reel_ok(wait_driver)
    
    btn_xpath = "//div[@class='_ac7b _ac7d']/descendant::div[text()='{}']"
    next_btn_xpath = btn_xpath.format('Next')
    for _ in range(2):
        time.sleep(1)
        next_btn = wait_driver.until(EC.element_to_be_clickable((By.XPATH, next_btn_xpath)))
        next_btn.click()

    time.sleep(1)
    share_btn_xpath = btn_xpath.format('Share')
    share_btn = wait_driver.until(EC.element_to_be_clickable((By.XPATH, share_btn_xpath)))
    share_btn.click()