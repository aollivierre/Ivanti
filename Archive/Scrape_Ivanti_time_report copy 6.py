from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import time
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
    driver.get("https://heat.novanetworks.com/HEAT/")
    log("Website loaded", '[34m')  # Blue for information
    
    # Login
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "UserName")))
    log("Login page loaded", '[34m')
    driver.find_element(By.ID, "UserName").send_keys("someusername")
    driver.find_element(By.ID, "Password").send_keys("somepassword" + Keys.RETURN)
    log("Login attempt made", '[34m')

    # Wait for the next page to load
    log("Waiting for next page to load after login")
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "someElementAfterLogin")))
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ext-gen79"]')))
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

    # Further code to interact with the 'Employee Self Work and Absence Report_N'
    # ...

except Exception as e:
    log("An error occurred:", '[31m')
    traceback.print_exc()

finally:
    log("Closing the browser", '[32m')
    driver.quit()
    log("Script execution finished", '[32m')
