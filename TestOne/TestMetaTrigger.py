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

class TestMetaTrigger(unittest.TestCase):
    """测试meta trigger"""
    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."

    def test_1_get_meta_trigger(self):
        """GET /api/v1.0/meiqia/car/meta/trigger"""
        headers={
            'x-token':gl.access_token,
            'content-type': gl.content_type
        }
        #data={}
        #r=requests.get(gl.url+":7020/api/"+gl.api_version+"/"+gl.tenant_name+"/"+gl.meta_name+"/meta/trigger",headers=headers)
        r=requests.get(gl.url+":7020/api/"+gl.api_version+"/"+gl.tenant_name+"/Account/meta/trigger",headers=headers)
        print r,r.text
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()["code"],0)
        result = json.loads(r.text)


    def test_2_create_meta_trigger(self):
        """POST /api/v1.0/meiqia/car/meta/trigger"""
        headers={
            'x-token':gl.access_token
        }
        data={"trigger": "if (event.IsBefore && event.IsInsert){"
                          "var obj = event.New "
                          "var now = NOW() "
                          "obj.OwnDate = now "
                          "var ensureTime = 60 * TIME_DAY "
                          "if (obj.Exist(\"Type\")) {"
                          "if (obj.Type == \"KA\") {"
                          "ensureTime = 90 * TIME_DAY}}"
                          "obj.TransferDate = DATETIME_ADD_DURATION(now, ensureTime)"
                          "}"
        }
        r=requests.post(gl.url+":7020/api/"+gl.api_version+"/"+gl.tenant_name+"/"+gl.meta_name+"/meta/trigger",data=json.dumps(data),headers=headers)
        print r,r.text
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()["code"],0)
        result = json.loads(r.text)

    def test_3_create_meta_trigger(self):
        """POST /api/v1.0/meiqia/car/meta/trigger"""
        headers={
            'x-token':gl.access_token
        }
        data={
            "trigger": None
        }
        r=requests.post(gl.url+":7020/api/"+gl.api_version+"/"+gl.tenant_name+"/"+gl.meta_name+"/meta/trigger",data=json.dumps(data),headers=headers)
        print r,r.text
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()["code"],0)
        result = json.loads(r.text)

gl.suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMetaTrigger))