# -*- coding: utf-8 -*-
import unittest
import json
import requests
import uuid
from GlobalVariables import gl

"""解决'ascii' codec can't decode byte 0xe6"""
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class TestJudgeProfile(unittest.TestCase):
    """常用工具方法集合"""

    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."

    def test_001_add_profile_OLA(self):
        """添加meta权限到profile，标准对象授权"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = {
            "ent_id": "00000000000000000000000000000000",
            "profile_id": "AQACd5VVkc56EgAAlRN1m4BW0BQBAAAA",
            "access":{
                "object_name": gl.meta_name,
                "creatable": True,
                "updatable": True,
                "readable": True,
                "deletable": True,
                "view_all": True,
                "modify_all": True
            }
        }
        r = requests.put(
            gl.url + ":7111/acl_admin/profile/AQACd5VVkc56EgAAlRN1m4BW0BQBAAAA/object_level_access",
            data=json.dumps(data), headers=headers, verify=False)
        print gl.url + ":7111/acl_admin/profile/AQACd5VVkc56EgAAlRN1m4BW0BQBAAAA/object_level_access"
        print r, r.text

    def test_002_add_profile_FLA(self):  # 字段授权
        headers = {
            # 'x-token': gl.access_token_lt_166,
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        r = requests.get(
            gl.url + ":7010/api/v1.0/" + gl.tenant_name + "/" + gl.meta_name + "/meta/schema",
            headers=headers, verify=False)
        print r, r.text
        result = json.loads(r.text)
        gl.clonum_dict = result["body"]
        keys = list(gl.clonum_dict.keys())
        for key in keys:
            print key
            data = {
                "ent_id": "00000000000000000000000000000000",
                "profile_id": "AQACd5VVkc56EgAAlRN1m4BW0BQBAAAA",
                "access": {
                    "object_name": gl.meta_name,
                    "field_name": key,
                    "updatable": True,
                    "readable": True
                }
            }
            headers = {
                # 'x-token': gl.access_token_lt_166,
                'x-token': gl.access_token,
                'content-type': gl.content_type
            }
            r = requests.put(
                gl.url + ":7111/acl_admin/profile/AQACd5VVkc56EgAAlRN1m4BW0BQBAAAA/field_level_access",
                data=json.dumps(data), headers=headers, verify=False)
            print gl.url + ":7111/acl_admin/profile/AQACd5VVkc56EgAAlRN1m4BW0BQBAAAA/field_level_access"
            print r, r.text

    def test_003_assign_profile_to_point_user(self):
        """授权到指定用户"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = {
            "ent_id": "00000000000000000000000000000000",
            "profile_id": "AQACd5VVkc56EgAAlRN1m4BW0BQBAAAA",
            "user_id": "AQACd5VVkc7RCAAALgrgmrnF6BSWKwAA"
            # AQACd5VVkc7RCAAALgrgmrnF6BSWKwAA   AQACd5VVkc7RCAAAucWwesDL7BR7QAAA
        }
        r = requests.post(
            gl.url + ":7111/acl_admin/profile/AQACd5VVkc7RCAAA1sIDurnF6BSXKwAA/user",
            data=json.dumps(data), headers=headers, verify=False)
        print gl.url + "/acl/acl_admin/profile/AQACd5VVkc7RCAAA1sIDurnF6BSXKwAA/user"
        print r, r.text




gl.suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestJudgeProfile))