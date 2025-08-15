from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
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
 


# Select Element by Index value 
ele_id = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='Btn1']")
time.sleep(5)
ele_id.click()

time.sleep(5)
ele_element = driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@resource-id='com.code2lead.kwad:id/Et1']")
ele_element.send_keys("Aditya Patil")


ele1_id = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.code2lead.kwad:id/Btn1']")
ele1_id.click()
time.sleep(5)
 
driver.quit()
# appium_service.stop()