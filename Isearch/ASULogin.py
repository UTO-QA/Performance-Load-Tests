# -*- coding: utf-8 -*-t
from selenium import webdriver
import platform
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from _codecs import decode
class ASULoginPythonScript:

    def _a_s_u_login_python_script(self,username,password,url):
        print("reached here")


        self.driver = webdriver.Chrome("/home/bhaddy-linux/chromedriver")
        self.driver.set_window_size(1200,960)
        driver = self.driver
        driver.get(url)

        driver.find_element_by_id("asu_hdr_ssi").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(username)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_css_selector("input.submit").click()
        cookies = driver.get_cookies()
        return cookies

