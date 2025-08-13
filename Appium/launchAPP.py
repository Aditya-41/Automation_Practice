# from appium import webdriver
from appium import webdriver
from appium.options.android import UiAutomator2Options
import time
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.appium_service import AppiumService

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ...existing code...

# wait = WebDriverWait(driver, 10)  # 10 seconds timeout

# # Step 3 : "Click on the App"
# ele_id = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.skill2lead.appiumdemo:id/EnterValue")))
# # ...existing code...


appium_service = AppiumService()
appium_service.start()
# caps = {
#     "platformName": "Android",
#     "deviceName": "Pixel 6a (VR)",
#     "udid": "emulator-5554",
#     "appPackage": "com.code2lead.kwad",
#     "appActivity": "com.code2lead.kwad.MainActivity",
#     "automationName": "UiAutomator2",
#     "app": "D:\CHROME DOWNLOAD\Android_Demo_App.apk",    # Full path to your APK file
#     "platformVersion": "13",
# }
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'pixel6a'
desired_caps['udid'] = 'emulator-5554'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['appPackage'] = 'com.code2lead.kwad'   
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'
# desired_caps['app'] =("D:\CHROME DOWNLOAD\Android_Demo_App.apk")

# driver = webdriver.Remote(
#     command_executor='http://127.0.0.1:4723/wd/hub', 
#     desired_capabilities = caps
# )

# ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
# ele_id.click()

# {
#   "appium:appPackage": "com.code2lead.kwad",
#   "appium:appActivity": "com.code2lead.kwad.MainActivity",
#   "platformName": "Android",
#   "appium:deviceName": "Pixel 6a (VR)",
#   "appium:udid": "emulator-5554",
#   "automationName": "UiAutomator2"
# }

 
# Step 1 : Create "Desired Capabilities"

 
options = UiAutomator2Options().load_capabilities(desired_caps)
options.set_capability("ignoreHiddenApiPolicyError", True)

driver = webdriver.Remote('http://127.0.0.1:4723', options=options,direct_connection=True)
wait = WebDriverWait(driver, 10)
 
# Step 3 : "Click on the App"
# ele_id = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.Button[@content-desc="Btn1"])))
ele_id = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='Btn1']")
# ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue"))
# ele_id = driver.find_element(AppiumBy.ID, "com.skill2lead.appiumdemo:id/EnterValue")
ele_id.click()
 
# Step 4 : Wait for 2 seconds
time.sleep(5)
 
# Step 5 : Close the driver object
# driver.quit()



# options = UiAutomator2Options()
# options.set_capability("platformName", "Android")
# options.set_capability("deviceName", "Pixel 6a (VR)")
# options.set_capability("udid", "FMQSV8WO5H5LY9AQ")  # or your device name from `adb devices`
# options.set_capability("appPackage", "com.code2lead.kwad")  # replace with your actual package
# options.set_capability("appActivity", "com.code2lead.kwad.MainActivity")  # replace with main activity
# options.set_capability("newCommandTimeout", 300)

# driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
# ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
# ele_id.click()

# time.sleep(100)

driver.quit()
appium_service.stop()