from appium import webdriver
import unittest

class TestLaunchApp(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'YourDeviceName',
            'app': 'path/to/your/app.apk',
            'autoGrantPermissions': True
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test_app_launch(self):
        self.assertIsNotNone(self.driver)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()