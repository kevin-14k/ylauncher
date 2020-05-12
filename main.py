import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
   
class YLauncher:
	web_driver_wait_time = 1200
	ad_sleep_time = 5.5

	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(self.driver, self.web_driver_wait_time)
		self.channel_name = "edsheeran"
		self.skip_ad_button_klass = ".ytp-ad-skip-button"
		self.video_ended_selector = "#movie_player.ended_mode"

	def process(self):
		self.driver.maximize_window()
		self.driver.get("https://www.youtube.com/user/" + self.channel_name + "/videos")
		first_result = self.wait.until(presence_of_element_located((By.ID, "video-title")))
		first_result.click()
		self.driver.find_element(By.CSS_SELECTOR, 'body').send_keys('F')
		skip_ad = self.wait.until(presence_of_element_located((By.CSS_SELECTOR, self.skip_ad_button_klass)))
		time.sleep(self.ad_sleep_time)
		skip_ad.click()
		self.wait.until(presence_of_element_located((By.CSS_SELECTOR, self.video_ended_selector)))		


with webdriver.Firefox() as driver:
	y_launcher = YLauncher(driver)
	y_launcher.process()
