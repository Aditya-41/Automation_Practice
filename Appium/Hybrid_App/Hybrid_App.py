from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
# from selenium.webdriver.common.touch_action import TouchAction
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.action_chains import ActionChains



import time


# appium_service = AppiumService()
# appium_service.start()


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'pixel6a'
desired_caps['udid'] = '7867dac1'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['appPackage'] = 'com.android.chrome'   
desired_caps['appActivity'] = 'com.google.android.apps.chrome.Main'
# desired_caps['fullReset'] = True


options = UiAutomator2Options().load_capabilities(desired_caps)
options.set_capability("ignoreHiddenApiPolicyError", True)

driver = webdriver.Remote('http://127.0.0.1:4723', options=options,direct_connection=True)

wait = WebDriverWait(driver, 20, poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])


# Select Element by Index value 
ele1 = wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.android.chrome:id/terms_accept']"))
ele1.click()

print(" 1st Click")
print(driver.session_id)

# time.sleep(2000)
ele2 = wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.android.chrome:id/negative_button']"))
ele2.click()

print(" 2st Click")

time.sleep(5)

ele3 = wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.android.chrome:id/negative_button']"))
ele3.click()
print(" 3st Click")

ele4 = wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='More options']"))
ele4.click()
print(" 4st Click")

time.sleep(2)
ele5 = wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//android.widget.TextView[@content-desc='New tab']"))
ele5.click()
print(" 5st Click")

ele6 = wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//android.widget.EditText[@resource-id='com.android.chrome:id/search_box_text']"))
ele6.click()
print(" 6st Click")

ele7 = wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//android.widget.EditText[@resource-id='com.android.chrome:id/url_bar']"))
ele7.click()
ele7.send_keys("https://github.com/Aditya-41")
time.sleep(5)
# ele5.clear()
# ele5.send_keys("https://github.com/Aditya-41")

driver.press_keycode(AndroidKey.ENTER)

# wait = WebDriverWait(driver, 30, poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])
time.sleep(5)
driver.quit()
# appium_service.stop()
