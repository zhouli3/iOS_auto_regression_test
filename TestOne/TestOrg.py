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


class TestOrg(unittest.TestCase):
    """测试 org 相关接口"""

    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."

    def test_1_create_org(self):
        """POST /api/v1.0/meiqia"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        org_name = gl.new_org_name
        r = requests.post(gl.url + ":7010/api/"+gl.api_version+"/" + org_name,
                         headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json(), "create-org ok")
        result = json.loads(r.text)

    def test_2_update_org(self):
        """PUT /api/v1.0/meiqia"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        org_name = gl.new_org_name + "new"
        r = requests.put(gl.url + ":7010/api/"+gl.api_version+"/" + org_name,
                         headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json(), "update-org ok")
        result = json.loads(r.text)

    def test_3_delete_org(self):
        """put /api/v1.0/meiqia"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        org_name = gl.tenant_name + "new"
        r = requests.delete(gl.url + ":7010/api/"+gl.api_version+"/" + org_name,
                         headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json(), "delete-org ok")
        result = json.loads(r.text)


gl.suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestOrg))
