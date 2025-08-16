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
 


print("Current Package:", driver.current_package)
print("Current Activity:", driver.current_activity)
print("Current Context:", driver.current_context)
print("Available Contexts:", driver.contexts)
print("Device Loked:", driver.is_locked())
print("Device Orientation:", driver.orientation)
print("Device Time:", driver.device_time)
print("Device Country:", driver.location)
# print("Device Name:", driver.)
device_name = driver.capabilities.get("deviceName")
print("Device Name:", device_name)

# Get Locale (Country + Language)
locale = driver.capabilities.get("locale")
language = driver.capabilities.get("language")

print("Language:", language)
print("Locale (Country):", locale)

 
driver.quit()
# appium_service.stop()