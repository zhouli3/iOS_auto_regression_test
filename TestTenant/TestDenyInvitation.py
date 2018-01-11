# -*- coding: utf-8 -*-
import unittest
import json
import uuid
import requests
from GlobalVariables import gl

"""解决'ascii' codec can't decode byte 0xe6"""
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class TestDenyInvitation(unittest.TestCase):
    """测试Tenant创建邀请--拒绝流程"""

    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."

    def test_1_create_tenant_or_org(self):
        """Test POST /account/org"""
        print uuid.uuid1()
        data = {
            "name": "测试" + str(uuid.uuid1()),
            "primaryContact": {
                "name": "测试",
                "phone": "12345678999",
                "email": "test@qq.com"
            },
            "phone": "12345678999",
            "fax": "0592-88887777",
            "address": {
                "street": "ddddd",
                "city": "beijing",
                "state": "wanggujin",
                "post_code": "200",
                "country": "China",
                "country_code": "010"
            }
        }
        headers = {
            'authorization': gl.account_token,
            'Content-Type': 'application/json'
        }
        print "传入参数：" + json.dumps(data)
        r = requests.post(gl.url + ':7121/account/org', data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["creator_account_id"])
        gl.tenant_id = result["body"]["id"]

    def test_2_tenant_sign(self):
        """Test POST /account/signin"""
        data = "{\"source\":\"web\",\"tenant_id\":\"" + gl.tenant_id + "\"}"
        headers = {
            'Authorization': gl.account_token
        }
        print "传入参数：" + data
        r = requests.post(gl.url + ":7121/account/signin", data=data, headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["access_token"])
        gl.access_token = result["body"]["access_token"]
        gl.refresh_token = result["body"]["refresh_token"]
        print result["body"]["access_token"]

    def test_3_tenant_invitation(self):
        """Test Post /tenant/invitation"""
        data = "{\"name\":\"测试\",\"phone\":\"" + gl.invitation_phoneNo + "\"}"
        headers = {
            'X-Token': gl.access_token
        }
        print "传入参数：" + data
        r = requests.post(gl.url + ":7121/tenant/invitation", data=data, headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["id"])
        gl.invitation_id = result["body"]["id"]

    def test_4_sign_out(self):
        """Test api account/v1/sign_out"""
        headers = {
            'authorization': gl.account_token,
        }
        r = requests.post(gl.url + ':7130/account/v1/sign_out', headers=headers)
        print r, r.status_code
        self.assertEqual(r.status_code, 200)

    #用被邀请账号登录拒绝邀请
    def test_5_signin(self):
        """ Test api signin process """
        print "获取验证码token"
        r = requests.post(gl.url + ':7130/account/v1/get_captcha_token')
        print r, r.status_code, r.json()["captcha_token"], r.json()["message"], r.json()["code"]
        self.assertEqual(r.status_code, 200)
        ##self.assertEqual(r.json()["message"], "操作成功")
        self.assertEqual(r.json()["code"], 0)
        gl.captcha_token = r.json()["captcha_token"]
        self.assertIsNotNone(gl.captcha_token)

        print "获取验证码"
        r = requests.get(gl.url + ':7130/account/v1/get_captcha_image' + '?captcha_token=' + gl.captcha_token)
        print r, r.status_code, r.json()["captcha_value"]
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.json()["captcha_value"])
        gl.captcha_value = r.json()["captcha_value"]

        print "发送验证码"
        d = "{\"purpose\": \"signin\", \"phone\": \""+gl.invitation_phoneNo+"\", \"Source\": \"web\", \"captcha_token\":\"" + gl.captcha_token + "\",\"captcha_value\":\"" + gl.captcha_value + "\"}"
        print "传入参数：" + d
        r = requests.post(gl.url + ':7130/account/v1/send_verify_code', data=d)
        print r, "返回值：" + r.text
        self.assertEqual(r.status_code, 200)
        gl.verify_code = r.json()["verify_code"]
        self.assertIsNotNone(r.json()["verify_code"])

        print "验证码校验"
        d = "{\"purpose\": \"signin\", \"phone\": \""+gl.invitation_phoneNo+"\",\"Source\": \"web\", \"verify_code\":\"" + gl.verify_code + "\"}"
        print "传入参数：" + d
        r = requests.post(gl.url + ':7130/account/v1/check_verify_code', data=d)
        print r, "返回值：" + r.text
        self.assertEqual(r.status_code, 200)

        print "登录"
        d = "{\"password\": \""+gl.invitation_pwd+"\", \"phone\": \""+gl.invitation_phoneNo+"\",\"Source\": \"web\", \"captcha_token\":\"" + gl.captcha_token + "\",\"captcha_value\":\"" + gl.captcha_value + "\"}"
        print "传入参数：" + d
        r = requests.post(gl.url + ':7130/account/v1/sign_in', data=d)
        print r, "返回值：" + r.text
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.json()["token"])
        gl.account_token = r.json()["token"]

    def test_6_account_deny_invitation(self):
        """Test post /account/deny_invitation/:id"""
        headers = {
            'Authorization': gl.account_token
        }
        r = requests.post(gl.url + ":7121/account/deny_invitation/" + str(gl.invitation_id), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)

    def test_7_tenant_signout(self):
        """Test post /tenant/signout"""
        headers = {
            'X-Token': gl.access_token
        }
        data = '{"source":"web"}'
        r = requests.post(gl.url + ':7121/tenant/signout', data=data, headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)

gl.suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestDenyInvitation))