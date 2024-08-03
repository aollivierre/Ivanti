from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Replace 'your_path_to_webdriver' with the path to your WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)



# Replace 'your_path_to_webdriver' with the path to your WebDriver
# driver = webdriver.Chrome(executable_path='your_path_to_webdriver')

try:
    # Navigate to the website
    driver.get("https://heat.novanetworks.com/HEAT/")

    # Wait for the login page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="UserName"]'))
    )

    # Login
    print("Attempting to interact with the element login page")
    driver.find_element(By.XPATH, '//*[@id="UserName"]').send_keys("aollivierre")
    driver.find_element(By.XPATH, '//*[@id="Password"]').send_keys("pass")
    driver.find_element(By.XPATH, '//*[@id="Password"]').send_keys(Keys.RETURN)

    # Wait for the next page to load
    print("Attempting to interact with the element My work tracking")
    # your interaction code

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ext-gen79"]'))
    )

    # Navigate to 'My work tracking' tab
    driver.find_element(By.XPATH, '//*[@id="ext-gen79"]').click()

    # Wait and click on 'Employee Self Work and Absence Report_N'
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="ext-comp-1253"]/div[1]'))
    ).click()

    # Set the Start and End dates to today's date
    today_date = datetime.now().strftime("%Y-%m-%d")  # Format: YYYY-MM-DD
    driver.find_element(By.XPATH, '//*[@id="paramStartDate-date"]').send_keys(today_date)
    driver.find_element(By.XPATH, '//*[@id="paramEndDate-date"]').send_keys(today_date)

    # Set Start and End times
    driver.find_element(By.XPATH, '//*[@id="paramStartDate-time"]').send_keys("12:00 AM")
    driver.find_element(By.XPATH, '//*[@id="paramEndDate-time"]').send_keys("11:45 PM")

    # Click on 'View report' button
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="ext-gen30"]'))
    ).click()

    # Wait for the report to generate (adjust time as necessary)
    time.sleep(600)  # Waits for 10 minutes; adjust based on your needs

    # Additional steps to download the report can be added here

except Exception as e:
    print(f"An error occurred: {e}")
    # Optionally, keep the browser open for inspection
    # input("Press Enter to quit...")
    # driver.quit()

finally:
    # Close the browser
    time.sleep(60)
    driver.quit()
    
