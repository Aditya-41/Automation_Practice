from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from appium.webdriver.extensions.android.nativekey import  AndroidKey
import time
 
# appium_service = AppiumService()
# appium_service.start()

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'pixel6a'
desired_caps['udid'] = 'emulator-5554'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['appPackage'] = 'com.code2lead.kwad'   
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'


options = UiAutomator2Options().load_capabilities(desired_caps)
options.set_capability("ignoreHiddenApiPolicyError", True)

driver = webdriver.Remote('http://127.0.0.1:4723', options=options,direct_connection=True)
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
 
wait = WebDriverWait(driver, 20, poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])


# Select Element by Index value 
ele_id = wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='Btn1']"))

ele_id.click()

# time.sleep(5)
ele_element = wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//android.widget.EditText[@resource-id='com.code2lead.kwad:id/Et1']"))
ele_element.send_keys("Aditya Patil")
ele_element.click()


# ele1_id = wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.code2lead.kwad:id/Btn1']"))
# ele1_id.click()
# time.sleep(5)

for i in range(10):
    driver.press_keycode(67)

time.sleep(5)

for i in range(2):
    driver.press_keycode(4)  # Press Enter Back key
    time.sleep(2)
    
driver.press_keycode(AndroidKey.APP_SWITCH)  # Press Home key

# driver.press_keycode(3)  # Press Enter Home key
time.sleep(5)
size = driver.get_window_size()
width = size['width']
height = size['height']

start_x = width / 2        # middle horizontally
start_y = height * 0.95    # very bottom of screen
end_x = width / 2          # same horizontal
end_y = height * 0.05      # very top of screen         # near top


# swipe a few times to remove multiple apps

driver.swipe(start_x, start_y, end_x, end_y, duration=100)
time.sleep(5)
driver.press_keycode(AndroidKey.HOME)  # Press Home key
time.sleep(5)

driver.lock(5)
time.sleep(5)

driver.unlock()
time.sleep(5)
driver.quit()
# appium_service.stop()