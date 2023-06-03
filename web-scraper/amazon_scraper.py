from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path

driver = webdriver.Chrome(service=Service(binary_path))

driver.get("http://selenium.dev")

driver.quit()

