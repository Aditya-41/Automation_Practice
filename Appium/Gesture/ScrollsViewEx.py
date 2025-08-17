from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
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

wait = WebDriverWait(driver, 20, poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])


# Select Element by Index value 
ele_id = wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='Btn3']"))

ele_id.click()

time.sleep(5)
ele_element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
        '.scrollIntoView(new UiSelector().text("BUTTON13").instance(0));'))
ele_element.click()


# ele1_id = wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.code2lead.kwad:id/Btn1']"))
# ele1_id.click()
time.sleep(5)
 
driver.quit()
# appium_service.stop()