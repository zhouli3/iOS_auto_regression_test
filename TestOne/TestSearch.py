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


class TestSearch(unittest.TestCase):
    """测试 搜索 相关接口"""

    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."

    def test_1_create_search_index(self):
        """POST /api/:ver/:org-name/service/search/index 
        创建索引"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        r = requests.post(
            gl.url + ":7020/api/"+gl.api_version+"/" + gl.tenant_name + "/service/search/index",
            headers=headers)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)

    def test_2_init_search_index_fields(self):
        """POST /api/:ver/:org-name/service/search/field
        初始化索引字段"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        r = requests.post(
            gl.url + ":7020/api/"+gl.api_version+"/" + gl.tenant_name + "/service/search/fields",
            headers=headers)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)

    def test_3_search_by_keywords(self):
        """GET /api/:ver/:org-name/service/search?keyword=xx:
        通过关键字进行全局搜索"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        keyword = gl.global_search_keyword
        print "请求参数KeyWord：" + keyword
        r = requests.get(
            gl.url + ":7020/api/"+gl.api_version+"/" + gl.tenant_name + "/service/search?keyword=" + keyword,
            headers=headers)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])

    def test_4_search_a_point_object(self):
        """GET /api/:ver/:org-name/service/obj-name?keyword=xx&limit=50&offset=0:
        搜索指定对象"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        object = gl.object_for_search
        keyword = gl.global_search_keyword
        limit = gl.limit_for_search
        offset = gl.offset_for_search
        print "请求参数KeyWord：" + keyword + "，Limit：" + limit + "，OffSet" + offset
        r = requests.get(
            gl.url + ":7020/api/"+gl.api_version+"/" + gl.tenant_name + "/service/search/" + object + "?keyword=" + keyword + "&limit=" + limit + "&offset=" + offset,
            headers=headers)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])


gl.suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestSearch))
