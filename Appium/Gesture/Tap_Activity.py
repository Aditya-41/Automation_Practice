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
desired_caps['udid'] = 'emulator-5554'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['appPackage'] = 'com.code2lead.kwad'   
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'


options = UiAutomator2Options().load_capabilities(desired_caps)
options.set_capability("ignoreHiddenApiPolicyError", True)

driver = webdriver.Remote('http://127.0.0.1:4723', options=options,direct_connection=True)

wait = WebDriverWait(driver, 20, poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])
finger = PointerInput( "touch", "finger")
actions = ActionChains(driver)
actions_w3c_actions = actions.w3c_actions  # just to be explicit

# Select Element by Index value 
ele_id = wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='Btn4']"))

# Get element location and size for center point
location = ele_id.location
size = ele_id.size
center_x = location['x'] + size['width'] // 2
center_y = location['y'] + size['height'] // 2

# Create a long press (click and hold) action using PointerInput
actions = ActionChains(driver)
finger = PointerInput("touch", "finger")
for i in range(2):
    actions.w3c_actions = ActionBuilder(driver, mouse=finger)
    actions.w3c_actions.pointer_action.move_to_location(center_x, center_y)
    actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.pause(2)  # Hold for 2 seconds
    actions.w3c_actions.pointer_action.pointer_up()
    actions.perform()
    time.sleep(1)  # Wait for the action to complete

# time.sleep(5)
# ele_element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
#         '.scrollIntoView(new UiSelector().text("BUTTON13").instance(0));'))
# ele_element.click()


# ele1_id = wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//android.widget.Button[@resource-id='android:id/button2']"))
# ele1_id.click()
# time.sleep(5)
 
driver.quit()
# appium_service.stop()