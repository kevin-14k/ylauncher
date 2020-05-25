import sys, getopt, time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
   
class YLauncher:
	web_driver_wait_time = 1200
	ad_sleep_time = 5.5

	def __init__(self, driver, username):
		self.driver = driver
		self.wait = WebDriverWait(self.driver, self.web_driver_wait_time)
		self.username = username
		self.skip_ad_button_klass = ".ytp-ad-skip-button"
		self.video_ended_selector = "#movie_player.ended_mode"

	def process(self):
		self.play()

	def play(self):
		self.driver.maximize_window()
		self.driver.get("https://www.youtube.com/user/" + self.username + "/videos")
		self.click_on_lastest_video()
		self.driver.find_element(By.CSS_SELECTOR, 'body').send_keys('F')
		self.skip_ad()
		self.wait.until(presence_of_element_located((By.CSS_SELECTOR, self.video_ended_selector)))		

	def click_on_lastest_video(self):
		first_result = self.wait.until(presence_of_element_located((By.ID, "video-title")))
		first_result.click()

	def skip_ad(self):
		skip_ad_element = self.wait.until(presence_of_element_located((By.CSS_SELECTOR, self.skip_ad_button_klass)))
		time.sleep(self.ad_sleep_time)
		skip_ad_element.click()

def main(argv):
	username = "CHANNEL_NAME"

	try:
		opts, args = getopt.getopt(argv,"hu:",["username="])
	except getopt.GetoptError:
		print('test.py -u <username>')
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			print('test.py -u <username>')
			sys.exit()
		elif opt in ("-u", "--username"):
			username = arg

	with webdriver.Firefox() as driver:
		y_launcher = YLauncher(driver, username)
		y_launcher.process()

if __name__ == "__main__":
   main(sys.argv[1:])