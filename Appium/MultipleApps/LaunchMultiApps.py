from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
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
# desired_caps['noReset'] = True  # Set noReset to True

options = UiAutomator2Options().load_capabilities(desired_caps)
options.set_capability("ignoreHiddenApiPolicyError", True)

driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
 
# driver.execute_script(
#     "mobile: startActivity",
#     {
#         "appPackage": "com.android.vending",
#         "appActivity": "com.android.vending.AssetBrowserActivity"
#     }
# )
# time.sleep(5)
driver.execute_script(
    "mobile: startActivity",
    {
        "appPackage": "com.android.chrome",
        "appActivity": "com.google.android.apps.chrome.Main"
    }
)
time.sleep(5)
 
 
driver.execute_script(
    "mobile: startActivity",
    {
        "appPackage": "com.code2lead.kwad",
        "appActivity": "com.code2lead.kwad.MainActivity"
    }
)
time.sleep(5)




# driver.start_activity("com.android.vending", "com.android.vending.AssetBrowserActivity")
# time.sleep(5)

# driver.start_activity("com.android.chrome", "com.google.android.apps.chrome.Main")
# time.sleep(5)
# driver.start_activity(
#     app_package='com.code2lead.kwad',
#     app_activity='com.code2lead.kwad.MainActivity'
# ) 

time.sleep(5)

 
driver.quit()
# appium_service.stop()