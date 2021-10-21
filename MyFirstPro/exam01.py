import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
class error00001(Exception):
    pass

class Login():
    def __init__(self, driver):
        self.dr = driver
        print("----初始化成功----")

    def findElement(self, locator):#如果写*locator表示不定长参数
        a = WebDriverWait(self.dr, 5).until(lambda x: x.find_element(*locator))
        #注意传参方式，参数是list，要用*（传字典键对值用**）
        return a
    def senkeys(self, locator, text):
        self.findElement(locator).send_keys(text)
    def click01(self,locator):
        self.findElement(locator).click()
    def switch01(self, locator):
        a = self.findElement(locator)#查找iframe
        self.dr.switch_to_frame(a)

class Case02(unittest.TestCase):

    def setUp(self):
        self.dr = webdriver.Firefox()
        self.dr.get("https://mail.163.com/")
        self.lg = Login(self.dr)
        #print("登录前标题%s" % (self.dr.title))

    def tearDown(self):
        self.dr.quit()
    def loginWYYX(self,account ,psw):
        sw = ("css selector", "#loginDiv>iframe")
        self.lg.switch01(sw)
        self.lg.senkeys(("name", "email"), account)
        self.lg.senkeys(("name", "password"), psw)
        dl = ("id", "dologin")
        self.lg.click01(dl)
        time.sleep(10)
        try:
            hand = self.dr.current_window_handle  # 跳转新页面之后记得重新获取句柄
            self.dr.switch_to.window(hand)
            sw = ("css selector", "#loginDiv>iframe")
            self.lg.switch01(sw)
            self.dr.find_element("css selector", ".ferrorhead")#查找密码错误提示
            print("登录失败，失败用例通过")
            return False
        except Exception as msg:
            hand = self.dr.current_window_handle  # 跳转新页面之后记得重新获取句柄
            self.dr.switch_to.window(hand)
            try:
                self.dr.find_element("css sellector", ".nui-ipt-placeholder")
                print("登录成功，成功用例通过")
                return True
            except Exception as msg:
                print("找不到登录成功元素'.nui-ipt-placeholder'")

            #print("找不到登录失败元素'.ferrorhead'")

    def test01(self):
        u'''登录用例；失败'''
        a = self.loginWYYX("xuxuxutest1", "qwe")
        self.assertFalse(a, msg="测试不通过")
    def test02(self):
        u'''登录用例：成功'''
        a = self.loginWYYX("xuxuxutest1", "qwe123456")
        self.assertTrue(a, msg="不符合失败条件，暂不确定是否登录成功")




#a = dr.find_element("css selector", "#loginDiv>iframe")
#dr.switch_to_frame(a)
#dr.find_element("name", "email").send_keys("noonehere")
#dr.find_element("name", "password").send_keys("qwe123456")

#dr.switch_to.default_content()
#nnn = dr.find_element_by_css_selector("#spnUid")
#noone = ("id", "spnUid")
#n = EC.text_to_be_present_in_element((noone), u"xuxu")(dr)
#print(n)
#m = dr.title
#print("登录后标题：%s" %m)
