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


class TestMetaSelectFilter(unittest.TestCase):
    """测试 meta selectfilter"""

    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."

    def test_1_create_meta_selectfilter(self):
        """POST /api/v1.0/meiqia/car/meta/select-filters"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        # name字段值需要用前面查询出来的schema中的lookup/master类型的字段名
        # expressions下的field字段值可以使用任何字段
        data = {
            "name": "created_by",
            "select_filter": {
                "filter": {
                    "expressions": [{
                        "field": "sgk_test_line",
                        "operator": ">=",
                        "operands": ["10"]
                    }],
                    "logical_relation": "1"
                },
                "is_valid": False,
                "strict_obey": True,
                "help_text": "this is 帮助文档",
                "error_message": "this is 错误信息",
                "result_help_text": "this is 结果信息"
            }
        }
        r = requests.post(gl.url + ":7020/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/meta/select-filters",
                          data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["select_filter"])
        gl.meta_selectfilter_name = result["body"]["name"]

    def test_2_get_meta_selectfilter(self):
        """GET /api/v1.0/meiqia/car/meta/select-filters"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        r = requests.get(gl.url + ":7020/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/meta/select-filters",
                         headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["select_filter"])

    def test_3_get_meta_selectfilter_by_name(self):
        """GET /api/v1.0/meiqia/car/meta/select-filters/selectfilter_name"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = gl.meta_selectfilter_name
        r = requests.get(
            gl.url + ":7020/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/meta/select-filters" + data,
            headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["filter"])

    def test_4_update_meta_selectfilter_by_name(self):
        """PUT /api/v1.0/meiqia/car/meta/select-filters/selectfilter_name"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = {
            "filter": {
                "expressions": [{
                    "field": "sgk_test_line",
                    "operator": ">=",
                    "operands": ["10"]
                }],
                "logical_relation": "1"
            },
            "is_valid": False,
            "strict_obey": True,
            "help_text": "this is 帮助 text",
            "error_message": "this is 错误 msg",
            "result_help_text": "this is 结果 msg"
        }
        r = requests.put(
            gl.url + ":7020/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/meta/select-filters" + gl.meta_selectfilter_name,
            data=json.dumps(data),headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["select_filter"])

    def test_5_delete_meta_selectfilter_by_name(self):
        """DELETE /api/v1.0/meiqia/car/meta/select-filters/selectfilter_name"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = gl.meta_selectfilter_name
        r = requests.delete(
            gl.url + ":7020/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/meta/select-filters/" + data,
            headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["name"])

gl.suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMetaSelectFilter))