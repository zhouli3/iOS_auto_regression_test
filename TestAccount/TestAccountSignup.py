# -*- coding: utf-8 -*-
import unittest
import requests
from GlobalVariables import gl

"""解决'ascii' codec can't decode byte 0xe6"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class TestAccountSignup(unittest.TestCase):
    """测试账号服务接口（注册）"""

    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."

    def test_signup(self):
        """ Test api signup process """
        header = {'accept-language': 'zh-CN,zh;q=0.8'}
        print "获取验证码token"
        r = requests.post(gl.url+':7130/account/v1/get_captcha_token',headers=header)
        print r,r.status_code,r.json()[ "captcha_token"],r.json()["message"],r.json()["code"]
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["message"], "操作成功")
        self.assertEqual(r.json()["code"], 0)
        gl.captcha_token=r.json()[ "captcha_token"]
        self.assertIsNotNone(gl.captcha_token)

        print "获取验证码"
        r = requests.get(gl.url+':7130/account/v1/get_captcha_image'+'?captcha_token='+gl.captcha_token,headers=header)
        print r,r.status_code,r.json()["captcha_value"]
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.json()["captcha_value"])
        gl.captcha_value=r.json()["captcha_value"]

        print "发送验证码"
        d = "{\"purpose\": \"signup\", \"phone\": \""+gl.login_username+"\", \"Source\": \"web\", \"captcha_token\":\""+gl.captcha_token+"\",\"captcha_value\":\""+gl.captcha_value+"\"}"
        print "传入参数："+d
        r = requests.post(gl.url+':7130/account/v1/send_verify_code',data=d,headers=header)
        print r,"返回值："+r.text
        self.assertEqual(r.status_code, 200)
        gl.verify_code = r.json()["verify_code"]
        self.assertIsNotNone(gl.verify_code)

        print "验证码校验"
        d = "{\"purpose\": \"signup\", \"phone\": \""+gl.login_username+"\",\"Source\": \"web\", \"verify_code\":\""+gl.verify_code+"\"}"
        print "传入参数："+d
        r = requests.post(gl.url+':7130/account/v1/check_verify_code',data=d,headers=header)
        print r,"返回值："+r.text
        self.assertEqual(r.status_code, 200)
    
        print "账户注册"
        d = "{\"password\": \""+gl.login_user_password+"\", \"phone\": \""+gl.login_username+"\",\"Source\": \"web\", \"verify_code\":\""+gl.verify_code+"\"}"
        print "传入参数："+d
        r = requests.post(gl.url+':7130/account/v1/sign_up',data=d,headers=header)
        print r,"返回值："+r.text
        self.assertEqual(r.status_code, 200)   

gl.suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAccountSignup))