# -*- coding: utf-8 -*-
import unittest
import requests
from GlobalVariables import gl

"""解决'ascii' codec can't decode byte 0xe6"""
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class TestAccountResetPwd(unittest.TestCase):
    """测试账号服务接口（重置密码）"""

    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."

    def test_resetpwd(self):
        """ Test api restpwd process """
        header = {'accept-language': 'en-US,en;q=0.8'}
        print "获取验证码token"
        # /api/v1.0/account     /account/v1
        r = requests.post(gl.url + ':7130/api/v1.0/account/get_captcha_token', headers=header)
        print r, r.status_code, r.json()["captcha_token"], r.json()["message"], r.json()["code"]
        print r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["message"], "OK")
        self.assertEqual(r.json()["code"], 0)
        gl.captcha_token = r.json()["captcha_token"]
        self.assertIsNotNone(gl.captcha_token)

        print "获取验证码"
        r = requests.get(gl.url + ':7130/api/v1.0/account/get_captcha_image' + '?captcha_token=' + gl.captcha_token,
                         headers=header)
        print r, r.status_code, r.json()["captcha_value"]
        print r.text
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.json()["captcha_value"])
        gl.captcha_value = r.json()["captcha_value"]

        print "发送验证码"
        d = "{\"purpose\": \"reset_password\", \"phone\": \"" + gl.login_username + "\", \"Source\": \"web\", \"captcha_token\":\"" + gl.captcha_token + "\",\"captcha_value\":\"" + gl.captcha_value + "\"}"
        print "传入参数：" + d
        r = requests.post(gl.url + ':7130/api/v1.0/account/send_verify_code', data=d,header = header)
        print r, "返回值：" + r.text
        self.assertEqual(r.status_code, 200)
        gl.verify_code = r.json()["verify_code"]
        self.assertIsNotNone(gl.verify_code)

        print "验证码校验"
        d = "{\"purpose\": \"reset_password\", \"phone\": \"" + gl.login_username + "\",\"Source\": \"web\", \"verify_code\":\"" + gl.verify_code + "\"}"
        print "传入参数：" + d
        r = requests.post(gl.url + ':7130/api/v1.0/account/check_verify_code', data=d,header = header)
        print r, "返回值：" + r.text
        self.assertEqual(r.status_code, 200)

        print "重置密码"
        d = "{\"new_password\": \"" + gl.login_username_new_password + "\", \"phone\": \"" + gl.login_username + "\",\"Source\": \"web\", \"verify_code\":\"" + gl.verify_code + "\"}"
        print "传入参数：" + d
        r = requests.post(gl.url + ':7130/api/v1.0/account/reset_password', data=d,header = header)
        print r, "返回值：" + r.text
        self.assertEqual(r.status_code, 200)


gl.suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAccountResetPwd))
