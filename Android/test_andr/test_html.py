##安卓系统的浏览器自动化

from time import sleep

from appium import webdriver
class Testhtm:
    def setup(self):
        des_caps = {
        'platformName':'android',
       'deviceName': '127.0.0.1:62001',
        'browserName': 'Browser',
        'noReset': True,

        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",des_caps)
        self.driver.implicitly_wait(20)
    def teardown(self):
        self.driver.quit()
    def test_baidu(self):
        self.driver.get("https://m.baidu.com")
        sleep(20)