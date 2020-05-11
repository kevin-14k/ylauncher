import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

# This example requires Selenium WebDriver 3.13 or newer
with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 1200)
    driver.maximize_window()
    driver.get("https://www.youtube.com/user/PassiveAggressions/videos")
    first_result = wait.until(presence_of_element_located((By.ID, "video-title")))
    first_result.click()
    driver.find_element(By.CSS_SELECTOR, 'body').send_keys('F')
    skip_ad = wait.until(presence_of_element_located((By.CSS_SELECTOR, ".ytp-ad-skip-button")))
    time.sleep(5.5)
    skip_ad.click()

    wait.until(presence_of_element_located((By.CSS_SELECTOR, "#movie_player.ended_mode")))
