from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
import time
 
# appium_service = AppiumService()
# appium_service.start()

def deviceDriver(device_ID, sysPort):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = 'pixel6a'
    desired_caps['systemPort'] = sysPort
    desired_caps['udid'] = device_ID
    # desired_caps['udid'] = 'emulator-5554'
    desired_caps['automationName'] = 'UiAutomator2'
    desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'   
    desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

    options = UiAutomator2Options().load_capabilities(desired_caps)
    options.set_capability("ignoreHiddenApiPolicyError", True)

    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    
    return driver

def enterText(driver):
    ele_id = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='Btn1']")
    ele_id.click()

    time.sleep(5)
    ele_element = driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@resource-id='com.skill2lead.appiumdemo:id/Et1']")
    ele_element.send_keys("Aditya Patil")
    time.sleep(5)

    ele1_id = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.skill2lead.appiumdemo:id/Btn1']")
    ele1_id.click()
    time.sleep(5)
    
    driver.quit()
    
def test_deviceTest():
    d1 = deviceDriver("emulator-5554", 8200)
    d2 = deviceDriver("7867dac1", 8201)
    
    enterText(d1)
    enterText(d2)