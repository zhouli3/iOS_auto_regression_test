# -*- coding: utf-8 -*-
import unittest
import json
import requests
from GlobalVariables import gl

"""解决'ascii' codec can't decode byte 0xe6"""
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
requests.packages.urllib3.disable_warnings()


class TestAccountSignup_online(unittest.TestCase):
    """测试账号服务接口（登录）"""

    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."

    def test_1_signinup(self):
        """ Test api signin process """
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type,
            'authorization':''
        }
        data = {
            "phone": "+86 15201173781",
            "email": "Shangguan123@Meiqia.com",
            "media_type": "email",
            "source": "internal",
            "password": "abcd12345",
            "verify_code": "93379"
        }
        r = requests.post(
            "http://10.100.250.164:7130/account/v1/internal/signup",
            data=json.dumps(data),headers=headers, verify=False)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        #result = json.loads(r.text)
        #self.assertIsNotNone(result["body"]["FieldList"])
