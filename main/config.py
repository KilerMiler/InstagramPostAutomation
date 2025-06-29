import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

def config_options():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)
    return options

def config_services():
    BASE_DIR = os.path.relpath(os.getcwd())
    driver_path = os.path.join(BASE_DIR, 'drivers','chromedriver-win64','chromedriver.exe')
    return Service(driver_path)

def get_driver():
    driver = webdriver.Chrome(service=config_services(), options=config_options())
    return driver

def get_wait_driver(driver):
    wait_driver = WebDriverWait(driver, 5*60)
    return wait_driver