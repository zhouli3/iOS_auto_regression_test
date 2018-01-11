# -*- coding: utf-8 -*-
import unittest
import json
import requests
import urllib
import uuid
from GlobalVariables import gl

"""解决'ascii' codec can't decode byte 0xe6"""
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class TestMetaValidations(unittest.TestCase):
    """测试meta validations"""

    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."

    def test_1_get_meta_all_validations(self):
        """GET /api/v1.0/meiqia/car/meta/validations"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        # data={}
        r = requests.get(gl.url + ":7020/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/meta/validations",
                         headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])

    def test_2_add_meta_validations(self):
        """POST /api/v1.0/meiqia/car/meta/validations"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = {
            "name": "at least 2",
            "validation":
                {
                    "expression": gl.meta_line_name + ">=2",
                    "is_valid": True,
                    "description": "Wheel数量大于等于2",
                    "error_message": "Wheel数量不能小于2！",
                    "position": ""
                }
        }
        print "请求参数：" + json.dumps(data)
        r = requests.post(gl.url + ":7020/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/meta/validations",
                          data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["validation"])
        gl.meta_validation_name = result["body"]["name"]

    def test_3_get_meta_validations_from_name(self):
        """GET /api/v1.0/meiqia/car/meta/validations/validation_name"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = gl.meta_validation_name
        print "请求参数：" + data
        r = requests.get(
            gl.url + ":7020/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/meta/validations/" + urllib.quote(
                data.encode("utf-8")), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])

    def test_4_update_meta_validations_from_name(self):
        """PUT  /api/v1.0/meiqia/car/meta/validations/validation_name"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = {
            "name": "at least 2",
            "validation":
                {
                    "expression": "sgk_test_line>=2",
                    "is_valid": False,
                    "description": "轮子数量大于等于2",
                    "error_message": "轮子数量不能小于2！",
                    "position": ""
                }
        }
        print "请求参数：" + data
        r = requests.put(
            gl.url + ":7020/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/meta/validations/" + urllib.quote(
                gl.meta_validation_name.encode("utf-8")), data=data, headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["validation"])

    def test_5_active_meta_validations_from_name(self):
        """PUT  /api/v1.0/meiqia/car/meta/validations/validation_name/active"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = urllib.quote(gl.meta_validation_name.encode("utf-8"))
        print "请求参数：" + data
        r = requests.put(
            gl.url + ":7020/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/meta/validations/" + data + "/active",
            headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["validation"])

    def test_6_close_meta_validations_from_name(self):
        """PUT  /api/v1.0/meiqia/car/meta/validations/validation_name/inactive"""
        headers = {
            'x-token': gl.access_token
        }
        data = urllib.quote(gl.meta_validation_name.encode("utf-8"))
        print "请求参数：" + data
        r = requests.put(
            gl.url + ":7020/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/meta/validations/" + data + "/active",
            headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["validation"])

    def test_7_delete_meta_validations_from_name(self):
        """DELETE  /api/v1.0/meiqia/car/meta/validations/validation_name"""
        headers = {
            'x-token': gl.access_token_test,
            'content-type': gl.content_type
        }
        data = urllib.quote(gl.meta_validation_name.encode("utf-8"))
        print "请求参数：" + data
        r = requests.delete(gl.url + ":7020/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/meta/validations/" + data,
                            headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])


gl.suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMetaValidations))
