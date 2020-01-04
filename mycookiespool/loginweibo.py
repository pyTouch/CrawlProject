# coding:utf-8
# time:2020/1/4
# copy from https://github.com/Python3WebSpider/CookiesPool
# 源代码作者：崔庆才

import requests
from requests import RequestException
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from chaojiying import Chaojiying

# 超级鹰用户名、密码、软件ID、
CHAOJIYING_USERNAME = '用户名'
CHAOJIYING_PASSWORD = '密码'
CHAOJIYING_SOFT_ID = '软件ID'
CHAOJIYING_KIND = 1902


class LoginWeibo():
    def __init__(self, username, password, browser):

        self.url = 'https://www.weibo.com'
        # self.url = 'https://m.weibo.cn/'
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 20)
        self.username = username
        self.password = password
        self.chaojiying = Chaojiying(CHAOJIYING_USERNAME, CHAOJIYING_PASSWORD, CHAOJIYING_SOFT_ID)

    # def __del__(self):
    #     self.browser.close()

    def open(self):
        """
        打开网页输入用户名密码
        :return: None
        """
        self.browser.get(self.url)
        # 找到用户名和密码输入框
        '''
        <input id="loginname" type="text" class="W_input" maxlength="128" autocomplete="off" action-data="text=邮箱/会员帐号/手机号" action-type="text_copy" name="username" node-type="username" tabindex="1">
        '''
        username = self.wait.until(EC.presence_of_element_located((By.ID, 'loginname')))
        '''
        <input type="password" class="W_input" maxlength="24" autocomplete="off" value="" action-type="text_copy" name="password" node-type="password" tabindex="2">
        '''
        password = self.wait.until(EC.presence_of_element_located((By.NAME, 'password')))
        # 输入用户名和密码
        username.send_keys(self.username)
        password.send_keys(self.password)

    def get_click_button(self):
        '''
        找到登录按钮
        :return:
        '''

        '''
        <a href="javascript:void(0)" class="W_btn_a btn_32px " action-type="btn_submit" node-type="submitBtn" suda-data="key=tblog_weibologin3&amp;value=click_sign" tabindex="6"><span node-type="submitStates">登录</span></a>
        '''
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'W_btn_a')))
        return  button

    def login_successfully(self):
        """
        判断登陆是否成功
        :return:
        """
        '''
        登录成功才能看到
        <em class="W_ficon ficon_mail S_ficon">I</em>
        '''
        try:
            return bool(
                WebDriverWait(self.browser,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.ficon_mail')))
            )
        except TimeoutException:
            return False

    def get_click_image(self, name='captcha.jpg'):
        """
        获取验证码图片
        :param name:
        :return: 图片对象
        """
        try:
            '''
            <img width="95" height="34" action-type="btn_change_verifycode" node-type="verifycode_image" src="https://login.sina.com.cn/cgi/pin.php?r=88815771&amp;s=0&amp;p=gz-66c0488ef9191010d88bea8c9f3a09fdf3bf">
            '''
            element = self.wait.until(EC.presence_of_element_located((By.XPATH,'//img[@action-type="btn_change_verifycode"]')))
            image_url = element.get_attribute('src')
            image = get_html(image_url).content
            with open(name, 'wb') as f:
                f.write(image)
            return image
        except NoSuchElementException:
            print('')
        return  None

    def password_error(self):
        """
        判断是否密码错误
        :return:
        """
        try:
            element = WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located((By.XPATH, '//span[@node-type="text"]')))
            print(element.text)
            if element.text == '用户名或密码错误。查看帮助':
                return True
        except TimeoutException:
            return False

    def get_cookies(self):
        """
        获取Cookies
        :return:
        """
        print(self.browser.get_cookies())
        return self.browser.get_cookies()

    def login(self):
        # 打开网址 输入用户名和密码
        self.open()
        print('网址打开成功！')
        # 点击登录按钮
        button = self.get_click_button()
        button.click()
        if self.password_error():
            print('用户名或密码错误')
            return {
                'status': 2,
                'content': '用户名或密码错误'
            }
        if self.login_successfully():
            print('登录成功')
            # 获取帐号对应的cookies
            cookies = self.get_cookies()
            return {
                'status': 1,
                'content': cookies
            }
        else:
            # 有时会需要验证码

            # 方法一：超级鹰破解
            # 获取验证码图片
            image = self.get_click_image()
            # 识别验证码
            result = self.chaojiying.post_pic(image, CHAOJIYING_KIND)

            # 方法二：手动输入
            # 手动输入验证码
            # result = str(input('请输入验证码：'))

            # 输入验证码
            verifycode = self.wait.until(EC.presence_of_element_located((By.NAME, 'verifycode')))
            verifycode.send_keys(result['pic_str'])
            # verifycode.send_keys(result)

            # 点击登录按钮
            button = self.get_click_button()
            button.click()
            if self.login_successfully():
                print('登录成功')
                # 获取帐号对应的cookies
                cookies = self.get_cookies()
                return {
                    'status': 1,
                    'content': cookies
                }
            else:
                self.chaojiying.report_error(result['pic_id'])
                self.login()
                # return {
                #     'status': 3,
                #     'content': '登录失败'
                # }

def get_html(url):
    try:
        # 添加User-Agent，放在headers中，伪装成浏览器
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            return response
        return None
    except RequestException:
        return None


if __name__ == '__main__':
    chromedriver = 'I:\Program Files (x86)\chromedriver.exe'
    browser = webdriver.Chrome(executable_path=chromedriver)
    result = LoginWeibo('账号', '密码', browser).login()
