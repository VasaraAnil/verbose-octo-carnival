from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Specify the path to geckodriver
geckodriver_path = "C:/Selenium/Drivers/geckodriver.exe"

# Set up the WebDriver
options = webdriver.FirefoxOptions()
options.accept_insecure_certs = True  # Ignore SSL errors
driver = webdriver.Firefox(service=Service(geckodriver_path), options=options)

# Implicit wait (optional)
driver.implicitly_wait(10)  # Uncomment to enable implicit wait for 10 seconds

# Navigate to the login page
driver.get("http://issuetracker.ntc-us.com/redmine/login?back_url=http%3A%2F%2Fissuetracker.ntc-us.com%2Fredmine%2Fprojects%2Ftd-support-tickets%2Fissues%2Fnew")

# Find the username field and enter username
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("anilv")

# Find the password field and enter password
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("abcd1234")  # Replace with your actual password

# Find the login button and click it
login_button = driver.find_element(By.ID, "login-submit")
login_button.click()

time.sleep(1)  # Wait for the page to load (can be adjusted)

# Find and click the issues element
issues_element = driver.find_element(By.CSS_SELECTOR, ".issues.selected")
issues_element.click()

# Find the filter field and input the filter
filter_element = driver.find_element(By.ID, "add_filter_select")
filter_element.send_keys("au")

time.sleep(1)  # Wait for the filter to apply (can be adjusted)

# Find the author field and input the author
author_element = driver.find_element(By.ID, "values_author_id_1")
author_element.send_keys("anil")

# Find the apply button and click it
apply_button = driver.find_element(By.CSS_SELECTOR, ".icon.icon-checked")
apply_button.click()

time.sleep(1)  # Wait for the page to load (can be adjusted)

# Find and click the subject element
subject_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]/form[2]/div/table/tbody/tr[1]/td[7]/a")
subject_element.click()

time.sleep(1)  # Wait for the page to load (can be adjusted)

# Loop to edit and close issues
for _ in range(100):  # Loop 100 times (adjust as needed)
    # Use explicit wait for the edit button
    edit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon.icon-edit"))
    )
    edit_button.click()

    # Find the status element and enter "close"
    status_element = driver.find_element(By.ID, "issue_status_id")
    status_element.send_keys("close")

    time.sleep(1)  # Wait for status change (can be adjusted)

    # Find the submit button and click it
    submit_button = driver.find_element(By.CSS_SELECTOR, "#issue-form > input:nth-child(7)")
    submit_button.click()

    time.sleep(1)  # Wait for submission (can be adjusted)

    # Find the next button and click it
    next_button = driver.find_element(By.CSS_SELECTOR, ".next-prev-links > a:nth-child(2)")
    next_button.click()
