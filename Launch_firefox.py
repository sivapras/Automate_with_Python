"""
#sample script for launching firefox

from selenium import webdriver

#driver = webdriver.Firefox()

driver = webdriver.Firefox(executable_path=r'/home/srinivas/Django/Selenium_Python/geckodriver')
driver.get("http://nemo.thrymr.net:8090")
time.sleep(10)
# assert 'Google' in driver.title


from selenium import webdriver

# capabilities = webdriver.DesiredCapabilities().FIREFOX
# capabilities["marionette"] = True

driver = webdriver.Firefox(executable_path=r'/home/srinivas/Django/Selenium_Python/geckodriver')
driver.get("http://www.google.com")

# selenium script for launch firefox and search in Google with a keyword and print the result and quit the firefox browser
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import time

# Create a new instance of the Firefox driver
driver = webdriver.Firefox(executable_path=r'/home/srinivas/Django/Selenium_Python/geckodriver')

# go to the google home page
driver.get("http://www.google.com")

# t
# he page is ajaxy so the title is originally this:
print(driver.title)

# find the element that's name attribute is q (the google search box)
inputElement = driver.find_element_by_name("q")

# type in the search
inputElement.send_keys("seleniumhq")
time.sleep(5)

# submit the form (although google automatically searches now without submitting)
inputElement.submit()

try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(driver, 10).until(EC.title_contains("seleniumhq"))

    # You should see "seleniumhq - Google Search"
    print(driver.title)

finally:

    driver.quit()
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox(executable_path=r'/home/srinivas/Django/Selenium_Python/geckodriver')

driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to the application home page
driver.get("http://www.google.com")

# get the search textbox
search_field = driver.find_element_by_id("lst-ib")
search_field.clear()

# enter search keyword and submit
search_field.send_keys("Selenium WebDriver Interview questions")
search_field.submit()

# get the list of elements which are displayed after the search
# currently on result page using find_elements_by_class_name method
lists= driver.find_elements_by_class_name("_Rm")

# get the number of elements found
print ("Found " + str(len(lists)) + " searches:")

# iterate through each element and print the text that is
# name of the search

i=0
for listitem in lists:
   print (listitem.get_attribute("innerHTML"))
   i=i+1
   if(i>10):
      break

# close the browser window
driver.quit()
