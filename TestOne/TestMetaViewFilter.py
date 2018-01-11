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


class TestMetaViewFilter(unittest.TestCase):
    """测试 meta viewfilter"""

    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."

    def test_1_create_view_filter(self):
        """POST /api/v1.0/meiqia/car/view-filters"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = {
            "display_name": "sgk_view_filter",
            "visible_to": "personal",
            "filter_from": "all",
            "filter": {
                "expressions": [{
                    "display_name": "sgk_test_line大于10",
                    "field": "sgk_test_line",
                    "operator": ">",
                    "operands": ["10"]
                }],
                "logical_relation": "1"
            }
        }
        print "请求参数：" + json.dumps(data)
        r = requests.post(gl.url + ":7020/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/view-filters", data=json.dumps(data),
                          headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["view_filter"])
        gl.view_filter_id = result["body"]["id"]
        gl.view_filter_user = result["body"]["view_filter"]["user"]

    def test_2_get_all_view_filter(self):
        """GET /api/v1.0/meiqia/car/view-filters"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        r = requests.get(gl.url + ":7020/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/view-filters",
                         headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["view_filter"])

    def test_3_get_view_filter_by_id(self):
        """GET /api/v1.0/meiqia/car/view-filters/viewfilter_id"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        viewfilter_id = gl.view_filter_id
        print "请求参数viewfilter_id：" + viewfilter_id
        r = requests.get(
            gl.url + ":7020/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/view-filters" + viewfilter_id,
            headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["filter"])

    def test_4_update_view_filter_by_id(self):
        """PUT /api/v1.0/meiqia/car/view-filters/viewfilter_id"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        viewfilter_id = gl.view_filter_id
        data = {
            "filter": {
                "expressions": [{
                    "display_name": "sgk_test_line大于9",
                    "field": "sgk_test_line",
                    "operator": ">=",
                    "operands": [
                        "9"
                    ]
                }],
                "logical_relation": "1"
            },
            "display_name": "sgkvf9",
            "visible_to": "personal",
            "filter_from": "all",
            "user": gl.view_filter_user,
            "meta_name": "sgk_meta"
        }
        print "请求参数viewfilter_id：" + viewfilter_id
        print "请求参数data：" + json.dumps(data)
        r = requests.put(
            gl.url + ":7020/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/view-filters" + viewfilter_id,
            data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["view_filter"])

    def test_5_set_default_view_filter(self):
        """PUT /api/v1.0/meiqia/car/view-filters/viewfilter_id/default"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        viewfilter_id = gl.view_filter_id
        print "请求参数viewfilter_id：" + viewfilter_id
        r = requests.put(
            gl.url + ":7020/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/view-filters" + viewfilter_id + "default",
            headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["id"])
        self.assertEqual(result["body"]["default_view_filter"], viewfilter_id)

    def test_6_delete_view_filter_by_id(self):
        """DELETE /api/v1.0/meiqia/car/view-filters/viewfilter_id"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        viewfilter_id = gl.view_filter_id
        print "请求参数viewfilter_id：" + viewfilter_id
        r = requests.delete(
            gl.url + ":7020/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/view-filters" + viewfilter_id,
            headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["id"])
        self.assertEqual(result["body"]["id"], viewfilter_id)

gl.suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMetaViewFilter))
