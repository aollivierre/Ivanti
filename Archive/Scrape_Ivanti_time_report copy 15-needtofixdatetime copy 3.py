import json
import os
import argparse
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import traceback
import time

# Custom logging function
def log(message, color='[0m'):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'\033{color}{timestamp} - {message}\033[0m')

# Load credentials from secrets.json
def load_credentials():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    secrets_path = os.path.join(script_dir, 'secrets.json')
    with open(secrets_path, 'r') as file:
        return json.load(file)

credentials = load_credentials()

# Function to calculate the first Monday and last Friday of the current week
def calculate_week_dates():
    today = datetime.now()
    start_of_week = today - timedelta(days=today.weekday())  # Monday of the current week
    end_of_week = start_of_week + timedelta(days=4)  # Friday of the current week
    return start_of_week.strftime('%m/%d/%Y'), end_of_week.strftime('%m/%d/%Y')

start_date, end_date = calculate_week_dates()

# Initialize argument parser
parser = argparse.ArgumentParser(description="Script to automate browser interactions.")
parser.add_argument("--close-browser", action="store_true", help="Close the browser after the script is done.")
args = parser.parse_args()

# Initialize WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    log("Starting script execution", '[32m')  # Green for start
    driver.get("https://heat.novanetworks.com/HEAT/")
    log("Website loaded", '[34m')  # Blue for information
    
    # Login
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "UserName")))
    log("Login page loaded", '[34m')
    driver.find_element(By.ID, "UserName").send_keys(credentials['username'])
    driver.find_element(By.ID, "Password").send_keys(credentials['password'] + Keys.RETURN)
    log("Login attempt made", '[34m')

    # Wait for the next page to load
    log("Waiting for next page to load after login")
    time.sleep(15)
    log("Next page loaded", '[34m')
    
    # Navigating to 'My work tracking' tab by finding the button
    button = None
    for iframe in driver.find_elements(By.TAG_NAME, 'iframe'):
        driver.switch_to.frame(iframe)
        try:
            button = driver.find_element(By.ID, "ext-gen79")
            if button:
                log("Button found inside iframe", '[34m')
                break
        except NoSuchElementException:
            pass
        driver.switch_to.default_content()
    
    if button:
        button.click()
        log("'My work tracking' tab clicked", '[34m')
        time.sleep(15)
    else:
        log("Button not found in any iframe or the main document", '[31m')
    
    # Print out iframe contents to help locate the correct iframe and button
    log("Printing iframe contents to help locate the correct iframe and button")
    for index, iframe in enumerate(driver.find_elements(By.TAG_NAME, 'iframe')):
        driver.switch_to.frame(iframe)
        log(f"Iframe {index} HTML content:", '[34m')
        log(driver.page_source[:1000], '[34m')  # Print first 1000 characters of iframe content for brevity
        driver.switch_to.default_content()

    # Switch to the correct iframe containing the Employee Self Work and Absence Report_N button
    log("Switching to the iframe containing the Employee Self Work and Absence Report_N button")
    employee_button = None
    for iframe in driver.find_elements(By.TAG_NAME, 'iframe'):
        driver.switch_to.frame(iframe)
        try:
            # Locate the button using text content
            employee_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[text()='Employee Self Work and Absence Report_N']"))
            )
            if employee_button:
                log("Employee Self Work and Absence Report_N button found inside iframe", '[34m')
                break
        except (NoSuchElementException, TimeoutException):
            driver.switch_to.default_content()
    
    # Click the Employee Self Work and Absence Report_N button
    if employee_button:
        employee_button.click()
        log("'Employee Self Work and Absence Report_N' button clicked", '[34m')
        time.sleep(10)  # Wait for the new page to load
    else:
        log("Employee Self Work and Absence Report_N button not found", '[31m')
    
    # Print out the current page source to help debug the issue
    log("Current page HTML content after clicking the button:")
    log(driver.page_source[:1000], '[34m')  # Print first 1000 characters of page content for brevity
    
    # Check if the new page is inside an iframe
    log("Checking if new page is inside an iframe")
    for index, iframe in enumerate(driver.find_elements(By.TAG_NAME, 'iframe')):
        driver.switch_to.frame(iframe)
        try:
            driver.find_element(By.ID, "paramStartDate-date")
            log(f"Found date field iframe: Iframe {index}", '[34m')
            break
        except NoSuchElementException:
            driver.switch_to.default_content()
    
    # Fill out the start date and end date fields
    log("Filling out the start date and end date fields")
    WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.ID, "paramStartDate-date")))
    driver.find_element(By.ID, "paramStartDate-date").send_keys(start_date)
    driver.find_element(By.ID, "paramEndDate-date").send_keys(end_date)
    log(f"Start date ({start_date}) and end date ({end_date}) filled out", '[34m')
    
    # Further code to interact with the next page or perform other actions
    # ...

    # Add a delay to observe the actions
    time.sleep(30)  # Adjust the time as needed

except Exception as e:
    log("An error occurred:", '[31m')
    traceback.print_exc()

finally:
    if args.close_browser:
        log("Closing the browser", '[32m')
        driver.quit()
        log("Browser closed", '[32m')
    else:
        log("Keeping the browser open", '[32m')
    log("Script execution finished", '[32m')
