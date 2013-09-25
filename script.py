from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

from bs4 import BeautifulSoup
import time

URL = "http://www.racingpost.com/horses/result_home.sd?race_id=586097&r_date=2013-09-21&popup=yes#results_top_tabs=re_&results_bottom_tabs=ANALYSIS"

# Start the WebDriver and load page
webdriver = webdriver.Firefox()
webdriver.get(URL)

# Wait for the dynamically loaded elements to show up
WebDriverWait(webdriver, 10).until(
	EC.visibility_of_element_located((By.CLASS_NAME, "resultRaceShowPedigrees")))

html = webdriver.page_source
webdriver.close()

soup = BeautifulSoup(html)
headings_soup = soup.find("thead")
horses_soup = soup.find_all("tbody")

for horses in horses_soup:
	h

print horses_soup

