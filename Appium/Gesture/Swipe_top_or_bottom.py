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

wait = WebDriverWait(driver, 30, poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])
finger = PointerInput( "touch", "finger")
actions = ActionChains(driver)
actions_w3c_actions = actions.w3c_actions  # just to be explicit

# Tap Activity element (Swipe Left to Right and Right to Left)

# ele_Btn = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
#         '.scrollIntoView(new UiSelector().text("DRAGANDDROP").instance(0));'))

def swipe_left(element):
    
    location = element.location
    size = element.size
    start_x1 =size['width']*0.8
    end_x1 = size['width']*0.1
    start_y1 = size['height']
    end_y1 = start_y1
    
    actions.w3c_actions = ActionBuilder(driver, mouse=finger)
    actions.w3c_actions.pointer_action.move_to_location(start_x1, start_y1)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.5)  # Hold for 0.5 seconds
    actions.w3c_actions.pointer_action.move_to_location(end_x1, end_y1)
    actions.w3c_actions.pointer_action.pause(0.5)  # Hold for 2 seconds
    actions.w3c_actions.pointer_action.pointer_up()
    actions.perform()
    
def swipe_right(element):
    
    location = element.location
    size = element.size
    strat_x1 =size['width']*0.1
    end_x1 = size['width']*0.8
    start_y1 = size['height']
    end_y1 = start_y1
    
    actions.w3c_actions = ActionBuilder(driver, mouse=finger)
    actions.w3c_actions.pointer_action.move_to_location(strat_x1, start_y1)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.5)  # Hold for 0.5 seconds
    actions.w3c_actions.pointer_action.move_to_location(end_x1, end_y1)
    actions.w3c_actions.pointer_action.pause(0.5)  # Hold for 2 seconds
    actions.w3c_actions.pointer_action.pointer_up()
    actions.perform()
    
def swipe_up():
    
    # location = element.location
    size = driver.get_window_size()
    start_x1 = size['width'] // 2
    end_x1 = start_x1
    start_y1 = size['height'] * 0.8
    end_y1 = size['height'] * 0.2
    actions.w3c_actions = ActionBuilder(driver, mouse=finger)
    actions.w3c_actions.pointer_action.move_to_location(start_x1, start_y1)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.5)  # Hold for 0.5 seconds
    actions.w3c_actions.pointer_action.move_to_location(end_x1, end_y1)
    actions.w3c_actions.pointer_action.pause(0.5)  # Hold for 2 seconds
    actions.w3c_actions.pointer_action.pointer_up()
    actions.perform()
    
def swipe_down():
    
    # location = element.location
    size = driver.get_window_size()
    # size = element.size
    start_x1 = size['width'] // 2
    end_x1 = start_x1
    start_y1 = size['height'] * 0.2
    end_y1 = size['height'] * 0.8
    actions.w3c_actions = ActionBuilder(driver, mouse=finger)
    actions.w3c_actions.pointer_action.move_to_location(start_x1, start_y1)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.5)   # Hold for 0.5 seconds      
    actions.w3c_actions.pointer_action.move_to_location(end_x1, end_y1)
    actions.w3c_actions.pointer_action.pause(0.5)  # Hold for 2 seconds
    actions.w3c_actions.pointer_action.pointer_up()
    actions.perform()   
    
ele_Btn = wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='Btn3']"))

ele_Btn.click()


# Get element HomeFragment

ele_btn9 = wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='BUTTON9']"))
# swipe_left(ele_home)

swipe_up()
time.sleep(2)

ele_btn16 = wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='BUTTON16']"))
swipe_down()

for i in range(2):
    driver.press_keycode(AndroidKey.BACK)  # Navigate back to the previous screen
    # driver.press_keycode(AndroidKey.BACK)
# driver.press_keycode(AndroidKey.TAB) 

# driver.press_keycode(AndroidKey.HOME)  
# Navigate to the recent tabs screen
driver.press_keycode(AndroidKey.APP_SWITCH)
time.sleep(1)
swipe_up()

time.sleep(5)
driver.quit()
# appium_service.stop()