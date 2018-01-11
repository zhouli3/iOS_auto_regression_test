# -*- coding: utf-8 -*-
import unittest
import json
import requests
import uuid
import random
from GlobalVariables import gl

"""解决'ascii' codec can't decode byte 0xe6"""
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class TestTerritoryHttp(unittest.TestCase):
    """测试 海 相关接口"""

    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."

    def test_1_get_territory_model_list(self):
        """GET /api/:ver/:org-name/service/territory/model?offset=0&limit=50"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        limit = gl.territory_limit
        offset = gl.territory_offset
        print "请求参数Limit：" + limit + "，OffSet：" + offset
        r = requests.get(
            gl.url + ":7010/api/"+gl.api_version+"/" + gl.tenant_name + "/service/territory/model?limit=" + limit + "&offset=" + offset,
            headers=headers)
        print gl.url + ":7010/api/"+gl.api_version+"/" + gl.tenant_name + "/service/territory/model?limit=" + limit + "&offset=" + offset
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        model_list = result["body"]["model_list"]
        gl.territory_model_id = model_list[random.randint(0, len(model_list) - 1)]["model_id"]

    def test_2_get_territory_id_by_model_id(self):
        """GET  /api/:ver/:org-name/service/territory/model/:model_id
        返回model对应根territory_id及其后代节点"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = gl.territory_model_id
        print "请求参数model_id：" + data
        r = requests.get(
            gl.url + ":7010/api/"+gl.api_version+"/" + gl.tenant_name + "/service/territory/model/" + data,
            headers=headers)
        print gl.url + ":7010/api/"+gl.api_version+"/" + gl.tenant_name + "/service/territory/model/" + data
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        territory_list = result["body"]["territory_list"]
        gl.territory_id = territory_list[random.randint(0, len(territory_list) - 1)]["territory_id"]

    def test_3_get_territory_record_list_by_territory_id(self):
        """GET /api/:ver/:org-name/service/territory/territory-node/:territory_id/record?offset=0&limit=10
        通过海节点id，获取海节点对应的Record list"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = gl.territory_id
        limit = gl.territory_limit
        offset = gl.territory_offset
        print "请求参数territory_id：" + data + ",territory_limit：" + limit + "，territory_offset：" + offset
        r = requests.get(
            gl.url + ":7010/api/"+gl.api_version+"/" + gl.tenant_name + "/service/territory/territory-node/" + data + "/record?limit=" + limit + "&offset=" + offset,
            headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["objects"])
        record_list = result["body"]["objects"]
        gl.territory_record_id = record_list[random.randint(0, len(record_list) - 1)]["id"]

    def test_4_claim_territory_record_by_record_id(self):
        """PUT /api/:ver/:org-name/service/territory/object/:object_id/claim
        通过record id领取Record"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = gl.territory_record_id
        print "请求参数territory_record_id：" + data
        r = requests.put(
            gl.url + ":7010/api/"+gl.api_version+"/" + gl.tenant_name + "/service/territory/object/" + data + "/claim",
            headers=headers)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)

    def test_5_allocate_record_to_territory(self):
        """PUT /api/:ver/service/territory/object/allocate
        退入Record到公海(支持批量)"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }

    def test_6_check_record_whether_entrust_territory(self):
        """GET api/v1.0/meiqia/service/territory/object/check/:object-name/object-id
        检测Record是否由海托管"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }


gl.suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestTerritoryHttp))
