from selenium import webdriver
import re

# Set the URL you want to webscrape from

site = ""
driver = webdriver.Chrome()
driver.get(site)
source = driver.page_source
regex = "[\w\.-]+@[\w\.-]+"
emails = re.findall(regex, source)
for n, m in enumerate(emails):
    print(n, ') ', m)

driver.close()
