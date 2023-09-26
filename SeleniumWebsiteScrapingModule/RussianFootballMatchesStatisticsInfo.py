from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import time


# define the website to scrape infrormation about football matches
website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
#choose chromewebdriver and launch it
driver = webdriver.Chrome()
driver.get(website)

# find necessary element on website
all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
# click on a button
all_matches_button.click()

# using the "box" section as a reference to help us locate an element inside
box = driver.find_element(By.CLASS_NAME, 'panel-body')
# select dropdown and select element inside by visible text
dropdown = Select(box.find_element(By.ID, 'country'))
dropdown.select_by_visible_text('Russia')
# implicit wait
time.sleep(5)
# select elements in the table
matches = driver.find_elements(By.CSS_SELECTOR, 'tr')

# storage it in a list
all_matches = [match.text for match in matches]

#quit scribing driver after all actions
driver.quit()

#Create Dataframe about all Russian football matches during last season in Pandas and export to CSV (Excel)
df = pd.DataFrame({'goals': all_matches})
print(df)
df.to_csv('RusFootballMatchStats.csv', index=False)
