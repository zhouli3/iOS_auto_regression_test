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


class TestAcceptInvitation(unittest.TestCase):
    """测试Tenant创建邀请--接受流程"""

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

    def test_4_tenant_invitation(self):
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

    def test_5_sign_out(self):
        """Test api account/v1/sign_out"""
        headers = {
            'authorization': gl.account_token,
        }
        r = requests.post(gl.url + ':7130/account/v1/sign_out', headers=headers)
        print r, r.status_code
        self.assertEqual(r.status_code, 200)

    #用被邀请账号登录接受邀请
    def test_6_signin(self):
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
        r = requests.post(gl.url + ':7130/api/v1.0/account/check_verify_code', data=d)
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

    def test_7_account_accept_invitation(self):
        """Test Post /account/accept_invitation/id"""
        print "invitation:"+str(gl.invitation_id)
        self.assertIsNotNone(gl.invitation_id)
        data = "{\"name\":\"测试\",\"phone\":\"" + gl.invitation_phoneNo + "\"}"
        headers = {
            'Authorization': gl.account_token
        }
        print "传入参数：" + data
        r = requests.post(gl.url + ":7121/account/accept_invitation/" + str(gl.invitation_id), data=data, headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)

    #获取该企业下的user_id  为后面的User相关 用户Delete做准备
    def test_8_1_get_tenant_relations(self):
        """Test get /tenant/relations"""
        headers = {
            'X-Token': gl.access_token
        }
        r = requests.get(gl.url + ':7121/tenant/relations', headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["items"])
        gl.user_id = result["body"]["items"][0]["user_id"]

    #接受邀请的 才能删除user 需要企业管理员来操作，删除的userId必须要在该企业下
    def test_8_tenant_user_delete(self):
        """Test delete /tenant/user/:userId"""
        self.test_5_sign_out()
        #再用一开始的管理员账号登录 当前登录方法传值为邀请账号，因此再赋值为原始账号值登录
        gl.invitation_phoneNo = gl.login_username
        gl.invitation_pwd = gl.login_user_password
        self.test_6_signin()
        headers = {
            'X-Token': gl.access_token
        }
        r = requests.delete(gl.url + ':7121/tenant/user/' + gl.user_id , headers=headers)
        print "删除User",r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)

    def test_9_tenant_signout(self):
        """Test post /tenant/signout"""
        headers = {
            'X-Token': gl.access_token,
        }
        data = "{'source':'web'}"
        r = requests.post(gl.url + ':7121/tenant/signout', data=data, headers=headers)
        print r, r.status_code
        self.assertEqual(r.status_code, 200)

gl.suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAcceptInvitation))