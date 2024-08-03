import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

import traceback
from traceback import print_exc
import pdb


import logging
log = logging.getLogger()


class CustomException(Exception): pass


sleep_time = 5
num_retries = 1
for x in range(0, num_retries):

    def Get_RBC_eStatement():

        try:

            # ensure you install chromedriver binaries with pip or manually download and unzip in a folder like Programfiles then run the ADD-PATH_V2.ps1 to add the path to system env variables
            options = webdriver.ChromeOptions()

            # options.add_argument('--headless')
            # options.add_argument('headless')

            # options.add_argument('--window-size=1920x1080')
            # options.add_argument("--disable-gpu")

            options.add_argument('--ignore-certificate-errors')
            options.add_argument("--test-type")
            options.add_argument("--disable-popup-blocking")
            options.add_argument("--incognito")
            options.add_argument("--disable-extensions")
            options.add_argument("--start-maximized")
            options.add_argument("--disable-default-apps")
            options.add_argument("--auto-open-devtools-for-tabs")
            options.add_experimental_option('useAutomationExtension', False)

            # options.setExperimentalOption("useAutomationExtension", false)

            driver = webdriver.Chrome(options=options)
            driver.get(
                'https://www.rbcroyalbank.com/ways-to-bank/online-banking/index.html')

            # driver.implicitly_wait(10)

            # driver.find_element_by_xpath(
                # '//*[@id="ns_Z7_4P88H9G09OPJ50A49KEGA034Q7_divIdForTableBDAStmt1"]/table[1]/tbody/tr[45]/td[1]/a').click()
            
            driver.find_element_by_xpath('//*[@id="header-sign-in-btn"]').click()
            time.sleep(sleep_time)  # Let the user actually see something!

            # Enter Credentials and Sign In
            driver.find_element_by_id('K1').send_keys('username')
            driver.find_element_by_id('Q1').send_keys('password')
            driver.find_element_by_class_name('yellowBtnLarge').click()
            time.sleep(sleep_time)

            # click on Documents and Statements
            driver.find_element_by_xpath(
                '//*[@id="ns_Z7_H1541AS0G8CV60Q82CVP2K3823_EDocument"]/a/div/span').click()

            # Select from the drop down menu
            select = Select(driver.find_element_by_xpath(
                '//*[@id="ns_Z7_4P88H9G09OPJ50A49KEGA034Q7_AccountDropdown"]'))
            # select by visible text
            select.select_by_visible_text('Main Account')
            driver.find_element_by_xpath(
                '//*[@id="ns_Z7_4P88H9G09OPJ50A49KEGA034Q7_goAccButtonEnable"]/span/span/button').click()
            time.sleep(sleep_time)
            select2 = Select(driver.find_element_by_xpath(
                '//*[@id="ns_Z7_4P88H9G09OPJ50A49KEGA034Q7_StmntRangeBI"]'))
            # select by visible text
            select2.select_by_visible_text('Last 17 statements')
            driver.find_element_by_xpath(
                '//*[@id="ns_Z7_4P88H9G09OPJ50A49KEGA034Q7_AcceptButton"]/span/span/button').click()
            # the most recent estatement
            driver.find_element_by_xpath(
                '//*[@id="ns_Z7_4P88H9G09OPJ50A49KEGA034Q7_divIdForTableBDAStmt1"]/table[1]/tbody/tr[3]/td[1]/a').click()

            print('i am done the try')
        # except:
        # except NoSuchElementException as e:
        # except Exception, e:
        # except Exception as e:
        except Exception as ex:
        
            # print('i caught an error with your web scraping script !!!')
            # print('i am done the except')
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            
            # log.exception("Message for you, sir!")
            # print traceback.format_exc()
            # sys.exc_info()
            # pdb.post_mortem()
            # traceback.print_exc()
            # print('type is:', e.__class__.__name__)
            # print_exc()
            # sys.exit(1) # exit on all exceptions for now
        else:
            # switch to the new active window
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(sleep_time)

            # Click on Continue to download the file

            print('downloading the statement')
            driver.find_element_by_xpath(
                '//*[@id="ns_Z7_4P88H9G09OPJ50A49KEGA034I1_ContinueButton"]/form/span/span/button').click()
            time.sleep(sleep_time)
            time.sleep(sleep_time)
            time.sleep(sleep_time)
            driver.quit()
            # print('i am done the else')
        finally:
            driver.quit()
            # print('i am done the finally')

Get_RBC_eStatement()