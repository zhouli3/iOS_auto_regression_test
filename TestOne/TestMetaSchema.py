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


class TestMetaSchema(unittest.TestCase):
    """测试meta schema"""
    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."


    def test_1_get_meta_schema(self):
        """GET /api/v1.0/meiqia/car/meta/schema"""
        headers={
            'x-token':gl.access_token,
            'content-type': gl.content_type
        }
        r=requests.get(gl.url+":7010/api/"+gl.api_version+"/"+gl.tenant_name+"/"+gl.meta_name+"/meta/schema",headers=headers)
        print r,r.text
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()["code"],0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["id"])
        self.assertIsNotNone(result["body"]["created_at"])

    def test_2_update_meta_schema(self):
        """PUT /api/v1.0/meiqia/car/meta/schema"""
        headers={
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data={"name":gl.meta_line_name,
              "display_name":"Wheel",
              "type":"integer",
              "nullable":False,
              "index":False,
              "unique":False,
              "default_value":{
                  "value":"4",
                  "dynamic":False
              }
        }
        r=requests.put(gl.url+":7020/api/"+gl.api_version+"/"+gl.tenant_name+"/"+gl.meta_name+"/meta/schema",
                       data = json.dumps(data),headers=headers)
        print r,r.text
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()["code"],0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["name"])
        self.assertIsNotNone(result["body"]["column"])

gl.suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMetaSchema))





