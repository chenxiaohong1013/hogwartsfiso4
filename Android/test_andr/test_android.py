##android手机自动化，相同步骤搜索不同的内容

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *


class Testandr:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName']='android'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.main.view.MainActivity'
        desired_caps['noReset'] = True
        desired_caps['skipServerInstallation'] = True
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)
    def teardown(self):
        pass
    @pytest.mark.parametrize('a,b,expect_price',[('alibaba','BABA',211.13),('xiaomi','01810',27.85)])
    def test_login(self,a,b,expect_price):
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/home_search").click()
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/search_input_text").send_keys(a)
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/name").click()
        current_price = self.driver.find_element(MobileBy.XPATH,f"//*[@text='{b}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        ##expect_price = 211.13
        assert_that(current_price,expect_price)