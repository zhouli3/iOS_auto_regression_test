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


class TestCancelInvitation(unittest.TestCase):
    """测试Tenant创建邀请--取消流程"""

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

    def test_6_tenant_cancel_invitation(self):
        """Test post /tenant/cancel_invitation/:id"""
        headers = {
            'X-Token': gl.access_token
        }
        r = requests.post(gl.url + ":7121/tenant/cancel_invitation/" + str(gl.invitation_id), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)

    def test_7_tenant_signout(self):
        """Test post /tenant/signout"""
        headers = {
            'X-Token': gl.access_token,
        }
        data = "{'source':'web'}"
        r = requests.post(gl.url + ':7121/tenant/signout', data=data, headers=headers)
        print r, r.status_code
        self.assertEqual(r.status_code, 200)

gl.suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCancelInvitation))