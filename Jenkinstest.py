from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options


def test_selenium():
    # PATH = "C:\Program Files (x86)\chromedriver.exe"
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')  # Run without GUI
    # chrome_options.add_argument('--no-sandbox')  # Required for some Jenkins environments
    # chrome_options.add_argument('--disable-dev-shm-usage')  # Avoid shared memory issues
    # chrome_options.add_argument('--disable-gpu')  # Disable GPU rendering
    # chrome_options.add_argument('--window-size=1920,1080')  # Set screen size
    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://talent.capgemini.com/in")
    time.sleep(15)
    print("Navigated to the talent page!")
    AboutUs = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, '39E9ECC5-558D-CBEF-B068-783BD9658D3D'))).click()
    print("About Us Clicked!")
    # driver.quit()
    time.sleep(15)
    # km3 = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="https://km3.capgemini.com/"]')))
    # replicon = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tools"]/div[3]/ul/li[6]/a')))
    # replicon.click()
    # time.sleep(15)
    driver.quit()
    # book_timeoff(driver)

    # driver.quit()\


def book_timeoff(driver):
    print("Inside the Book Timeoff function")
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    book_timeoff = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.cardAddBooking')))
    book_timeoff.click()
    time.sleep(20)

    elements = driver.find_elements(By.TAG_NAME, 'a')  # This will return a list of all 'input' tags
    n = len(elements)
    target_element = elements[n - 1]  # Access the nth element from the list
    target_element.click()

    # Locate all <li> tags that contain <a> tags
    dropdown_elements = driver.find_elements(By.XPATH, "//li/a")

    for option in dropdown_elements:
        if option.text == 'Family Get Together':
            # print(option.text)
            option.click()
            time.sleep(30)
            break

    # submit_for_approval = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'timeOffSubmit')))
    # submit_for_approval.click()

    cancel_request = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'timeOffCancel')))
    cancel_request.click()
    time.sleep(20)


test_selenium()