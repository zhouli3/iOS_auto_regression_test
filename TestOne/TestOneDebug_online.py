# -*- coding: utf-8 -*-
import unittest
import json
import requests
import urllib
import random
import time
import uuid
from GlobalVariables import gl

"""解决'ascii' codec can't decode byte 0xe6"""
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
requests.packages.urllib3.disable_warnings()


class TestOneDebug(unittest.TestCase):
    """测试 one 服务添加的 debug 接口"""

    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."

    def test_1_get_internal_debug(self):
        """GET /internal/debug 获取 debug 服务状态"""
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type
        }
        # data={}
        r = requests.get(gl.url_online + "/dml/internal/debug", headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        self.assertEqual(result["body"]["debug_is_opened"], True)

    def test_2_open_internal_debug(self):
        """GET /internal/debug/open 开启 debug 服务状态"""
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type
        }
        # data={}
        r = requests.put(gl.url_online + "/dml/internal/debug/open", headers=headers,verify=False)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        self.assertEqual(result["body"]["debug_is_opened"], True)

    def test_3_check_internal_debug_pprof(self):
        """ip:7011/internal/debug/pprof"""
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type
        }
        # data={}
        r = requests.get("http://10.100.250.133" + ":7011/internal/debug/pprof", headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)

    def test_4_close_internal_debug(self):
        """GET /internal/debug/close 关闭 debug 服务状态"""
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type
        }
        # data={}
        r = requests.put(gl.url_online + "/dml/internal/debug/close", headers=headers,verify = False)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        self.assertEqual(result["body"]["debug_is_opened"], False)

    def test_5_check_internal_debug_pprof(self):
        """ip:7011/internal/debug/pprof"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        # data={}
        r = requests.get(gl.url + ":7011/internal/debug/pprof", headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)

    def test_6_open_internal_debug(self):
        """GET /internal/debug/open 开启 debug 服务状态"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        # data={}
        r = requests.put(gl.url + ":7010/internal/debug/open", headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        self.assertEqual(result["body"]["debug_is_opened"], True)
