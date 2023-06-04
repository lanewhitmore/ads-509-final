import csv
import time
import random
from chromedriver_py import binary_path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# global variables
book_url = 'https://www.amazon.com/Best-Sellers-Books/zgbs/books'
time_rand = random.randint(2,5)
top_50 = 50
fp = "data/book_list.csv"

# initialize driver
driver = webdriver.Chrome(service=Service(binary_path))
driver.implicitly_wait(10)

# configure window & visit page
driver.maximize_window()
time.sleep(time_rand)
driver.get(book_url)
driver.refresh()
time.sleep(time_rand)

# get text
book_list = []

try:
    for i in range(1, top_50+1):
        book_title = driver.find_element(By.XPATH, f'//*[text()="#{i}"]/../../../div[2]/div/a[2]/span/div')
        if "Summer Bridge Activities" in book_title.text:
            book_list.append((book_title.text, 'Summer Bridge Activities'))
            continue
        if "Brown Bear, Brown Bear, What Do You See?" in book_title.text:
            book_list.append((book_title.text, 'Bill Martin Jr.'))
            continue
        book_author = driver.find_element(By.XPATH, f'//*[text()="#{i}"]/../../../div[2]/div/div/a/div')
        driver.execute_script("arguments[0].scrollIntoView();", book_author)
        book_list.append((book_title.text, book_author.text))

except Exception as e:
    print(str(e))
    driver.quit()

# write results to file
with open(fp, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(book_list)

# clean up driver resources
driver.quit()

