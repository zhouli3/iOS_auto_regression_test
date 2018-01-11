# -*- coding: utf-8 -*-
import unittest
import requests
from GlobalVariables import gl

"""解决'ascii' codec can't decode byte 0xe6"""
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class TestAccountSignin(unittest.TestCase):
    """测试账号服务接口（登录）"""

    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."

    def test_1_signin(self):
        """ Test api signin process """
        print "获取验证码token"
        r = requests.post(gl.url + ':7130/account/v1/get_captcha_token')
        print r, r.status_code, r.json()["captcha_token"], r.json()["message"], r.json()["code"]
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["message"], "操作成功")
        self.assertEqual(r.json()["code"], 0)
        gl.captcha_token = r.json()["captcha_token"]
        self.assertIsNotNone(gl.captcha_token)

        print "获取验证码"
        r = requests.get(gl.url + ':7130/account/v1/get_captcha_image' + '?captcha_token=' + gl.captcha_token)
        print r.text
        print r, r.status_code, r.json()["captcha_value"]
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.json()["captcha_value"])
        gl.captcha_value = r.json()["captcha_value"]

        print "发送验证码"
        d = "{\"purpose\": \"signin\", \"phone\": \""+gl.login_username+"\", \"Source\": \"web\", \"captcha_token\":\"" + gl.captcha_token + "\",\"captcha_value\":\"" + gl.captcha_value + "\"}"
        print "传入参数：" + d
        r = requests.post(gl.url + ':7130/account/v1/send_verify_code', data=d)
        print r, "返回值：" + r.text
        self.assertEqual(r.status_code, 200)
        gl.verify_code = r.json()["verify_code"]
        self.assertIsNotNone(gl.verify_code)

        print "验证码校验"
        d = "{\"purpose\": \"signin\", \"phone\": \""+gl.login_username+"\",\"Source\": \"web\", \"verify_code\":\"" + gl.verify_code + "\"}"
        print "传入参数：" + d
        r = requests.post(gl.url + ':7130/account/v1/check_verify_code', data=d)
        print r, "返回值：" + r.text
        self.assertEqual(r.status_code, 200)

        print "登录"
        d = "{\"password\": \""+gl.login_user_password+"\", \"phone\": \""+gl.login_username+"\",\"Source\": \"web\", \"captcha_token\":\"" + gl.captcha_token + "\",\"captcha_value\":\"" + gl.captcha_value + "\"}"
        print "传入参数：" + d
        r = requests.post(gl.url + ':7130/account/v1/sign_in', data=d)
        print r, "返回值：" + r.text
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.json()["token"])
        gl.account_token = r.json()["token"]

    # 登出后，token将失效，后续流程中会用到该token，所以暂时不执行
    @unittest.skip("I don't want to run this case.")
    def test_2_sign_out(self):
        """Test api account/v1/sign_out"""
        headers = {
            'authorization': gl.account_token,
        }
        r = requests.post(gl.url + ':7130/account/v1/sign_out', headers=headers)
        print r, r.status_code
        self.assertEqual(r.status_code, 200)

    # 内部接口--验证access token
    @unittest.skip("I don't want to run this case.")
    def test_8_verify_token(self):
        """Test api account/v1/internal/verify_token"""
        token = 'AUQBAAoPwll4AEFRQUMxMmhTYktxR0tRQUFIMzZqRVMxYTRoUnZFd0FBMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAyMKxhVluIRewJcJcj75YiE0hU5i6c4aLqFINvuf4t7b_IMM8-j0p7zTASqd-Kq2xSYJEuCGmKBCJfF2g-Cei-'
        r = requests.get(gl.url + ':7130/account/v1/internal/verify_token?token=' + token)
        print r, r.status_code, r.text
        self.assertEqual(r.status_code, 200)

    # 内部接口--获取账户手机号码
    @unittest.skip("I don't want to run this case.")
    def test_9_get_phone(self):
        """Test api account/v1/internal/get_phone"""
        r = requests.get(gl.url + ':7130/account/v1/internal/get_phone?id=' + '1222')
        print r, r.status_code, r.text
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.json()["phone"])


gl.suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAccountSignin))
