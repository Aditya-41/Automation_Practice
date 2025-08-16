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
element = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='Btn1']")
time.sleep(1)
print("Text:", element.text)                           # visible text
print("Class:", element.get_attribute("className"))    # class of element
print("Content-desc:", element.get_attribute("contentDescription"))  
print("Enabled:", element.get_attribute("enabled"))    
print("Displayed:", element.is_displayed())            
print("Selected:", element.is_selected())              
print("Clickable:", element.get_attribute("clickable"))
print("Bounds:", element.get_attribute("bounds")) 
element.click()

time.sleep(5)
print("Element Chnages.")
ele_element = driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@resource-id='com.code2lead.kwad:id/Et1']")
ele_element.send_keys("Aditya Patil")
# print("Element found:", ele_id.text)
print("Text:", ele_element.text)                           # visible text
print("Class:", ele_element.get_attribute("className"))    # class of element
print("Content-desc:", ele_element.get_attribute("contentDescription"))  
print("Enabled:", ele_element.get_attribute("enabled"))    
print("Displayed:", ele_element.is_displayed())            
print("Selected:", ele_element.is_selected())              
print("Clickable:", ele_element.get_attribute("clickable"))
print("Bounds:", ele_element.get_attribute("bounds")) 
 
driver.press_keycode(3)  # Press Enter Home key
time.sleep(5)
driver.quit()
# appium_service.stop()