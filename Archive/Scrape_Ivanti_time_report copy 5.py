from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import traceback

# Custom logging function
def log(message, color='[0m'):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'\033{color}{timestamp} - {message}\033[0m')

# Initialize WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    log("Starting script execution", '[32m')  # Green for start

    # Navigate to the website
    log("Navigating to the website")
    driver.get("https://heat.novanetworks.com/HEAT/")
    log("Website loaded", '[34m')  # Blue for information

    # Wait for the login page to load
    log("Waiting for login page to load")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="UserName"]')))
    log("Login page loaded", '[34m')

    # Login
    log("Performing login")
    driver.find_element(By.XPATH, '//*[@id="UserName"]').send_keys("aollivierre")
    driver.find_element(By.XPATH, '//*[@id="Password"]').send_keys("pass")
    driver.find_element(By.XPATH, '//*[@id="Password"]').send_keys(Keys.RETURN)
    log("Login attempt made", '[34m')

    # Wait for the next page to load
    log("Waiting for next page to load after login")
    
    # Navigate to 'My work tracking' tab
    # iframe = driver.find_element_by_id("ext-gen118")
    # driver.switch_to.frame(iframe)
    
    # elem = driver.find_element_by_id("ext-gen79")
    
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ext-gen79"]')))
    log("Next page loaded", '[34m')
    
    
    log("Navigating to 'My work tracking' tab")
    # element = driver.find_element(By.XPATH, '//*[@id="ext-gen79"]')
    # driver.execute_script("arguments[0].scrollIntoView();", element)
    # driver.execute_script("arguments[0].click();", element)
    # element.click()
    
    # button = driver.find_element_by_xpath("//button[contains(text(), 'My Work Tracki')]")
    # button = driver.find_element(By.XPATH, "//button[contains(text(), 'My Work Tracki')]")
    # button.click()

    # button = driver.find_element_by_css_selector("button.x-btn-text.x-dashboard-toolbar-icon-small")
    # button.click()


    # wait = WebDriverWait(driver, 10)
    # button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'My Work Tracki')]")))
    # button.click()


    # button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'My Work Tracki')]")))
    # button.click()


    # driver.switch_to.default_content()
    
    wait = WebDriverWait(driver, 30)
    # work_tracking_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ext-gen79"]')))
    # work_tracking_tab.click()
    
    
    # wait = WebDriverWait(driver, 30)  # Increase the wait time
    # work_tracking_button = wait.until(EC.element_to_be_clickable((By.ID, 'ext-gen79')))
    # work_tracking_button.click()

    
    

    # Your existing setup code...

    # Attempt to switch to the iframe and find the button


# Your existing setup code...

    button = None  # Initialize the button variable

    try:
        # Loop through all iframes on the page
        for iframe in driver.find_elements(By.TAG_NAME, 'iframe'):
            # Switch to the iframe
            driver.switch_to.frame(iframe)
            
            # Try to find the button within the iframe
            try:
                button = driver.find_element(By.ID, "ext-gen79")
                # If the button is found, break out of the loop
                if button:
                    break
            except NoSuchElementException:
                # If not found, continue to the next iframe
                pass

            # Switch back to the main document before trying the next iframe
            driver.switch_to.default_content()
        
        # After checking all iframes, check if button was found
        if button:
            button.click()
        else:
            print("Button not found in any iframe or the main document.")

    except NoSuchElementException:
        print("No iframes found, or button not inside an iframe or the main document.")

    # Always switch back to the main content when done with iframes
    driver.switch_to.default_content()

# Your code to close the browser...



    
    
    # Wait for the element to be present and interactable
    # wait = WebDriverWait(driver, 10)
    # elem = wait.until(EC.element_to_be_clickable((By.ID, "ext-gen79")))
    log("'My work tracking' tab clicked", '[34m')
    


    # Wait and click on 'Employee Self Work and Absence Report_N'
    log("Waiting for 'Employee Self Work and Absence Report_N' to be clickable")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ext-comp-1253"]/div[1]'))).click()
    log("'Employee Self Work and Absence Report_N' clicked", '[34m')

    # Set the Start and End dates to today's date
    log("Setting Start and End dates")
    today_date = datetime.now().strftime("%Y-%m-%d")  # Format: YYYY-MM-DD
    driver.find_element(By.XPATH, '//*[@id="paramStartDate-date"]').send_keys(today_date)
    driver.find_element(By.XPATH, '//*[@id="paramEndDate-date"]').send_keys(today_date)
    log("Dates set", '[34m')

    # Set Start and End times
    log("Setting Start and End times")
    driver.find_element(By.XPATH, '//*[@id="paramStartDate-time"]').send_keys("12:00 AM")
    driver.find_element(By.XPATH, '//*[@id="paramEndDate-time"]').send_keys("11:45 PM")
    log("Times set", '[34m')

    # Click on 'View report' button
    log("Clicking on 'View report' button")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ext-gen30"]'))).click()
    log("'View report' button clicked", '[34m')

    # Wait for the report to generate (adjust time as necessary)
    log("Waiting for report generation (10 minutes)")
    time.sleep(600)
    log("Wait completed", '[32m')  # Green for successful completion

# In your exception handling block
except Exception as e:
    log("An error occurred:", '[31m')
    traceback.print_exc()  # This prints the full traceback

finally:
    # Close the browser
    log("Closing the browser", '[32m')
    time.sleep(5)
    driver.quit()
    log("Script execution finished", '[32m')
