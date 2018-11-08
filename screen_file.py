import unittest
from selenium import webdriver
import ddt
import HTMLTestRunner
import time
from selenium.webdriver.support import expected_conditions as EC


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        url = "https://passport.cnblogs.com/user/signin"
        self.driver.get(url)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test01(self):
        try:
            self.driver.find_element_by_id("input1").send_keys("jiuan")
            self.driver.find_element_by_id("input2").send_keys("123456")
            self.driver.find_element_by_id("sign1").click()
            locator = ("id", "lnk_current_user")
            result = EC.text_to_be_present_in_element(locator, "久安")(self.driver)
            self.assertTrue(result)
        except Exception as msg:
            print(u"异常原因%s" % msg)
            nowtime = time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file('%s.png' % nowtime)


if __name__ == '__main__':
    unittest.main()
