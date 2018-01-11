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

class TestMetaDepends(unittest.TestCase):
    """测试meta depends"""

    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."


    def test_1_get_meta_depends(self):
        """GET /api/v1.0/meiqia/car/meta/depends"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        r=requests.get(gl.url+":7020/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/meta/depends",headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])

    def test_2_create_meta_depends(self):
        """POST /api/v1.0/meiqia/car/meta/depends"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        r = requests.post(gl.url + ":7020/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/meta/depends",
                         headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])

    def test_3_update_meta_depends(self):
        """PUT /api/v1.0/meiqia/car/meta/depends/depend_id"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data=""
        r = requests.put(gl.url + ":7020/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/meta/depends"+data,
                         headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])

    def test_4_delete_meta_depends(self):
        """DELETE /api/v1.0/meiqia/car/meta/depends/depend_id"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = ""
        r = requests.delete(gl.url + ":7020/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/meta/depends" + data,
                         headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])

gl.suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMetaDepends))
