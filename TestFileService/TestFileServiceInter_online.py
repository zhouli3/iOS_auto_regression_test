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

class TestFileServiceInter(unittest.TestCase):
    """文件服务接口测试"""
    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."

    def test_001_add_folder_file_handler(self):
        """:7001/v1/folder/:folder_id/file?create_thumb=true -X POST """
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type,
            'accept-language':'zh-CN,zh;q=0.8',
        }
        data = {"upload":"审批流编号问题.png"}
        r = requests.post(gl.url_online + "/file/"+gl.file_service_version+"/folder/" + gl.folder_id + "/file?create_thumb=true",
                         data = json.dumps(data),headers=headers)
        print gl.url_online + "/file/"+gl.file_service_version+"/folder/" + gl.folder_id + "/file?create_thumb=true"
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)

    def test_002_get_folder_file(self):
        """:7001/v1/folder/:folder_id/file?create_thumb=true -X POST """
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type,
            'accept-language':'zh-CN,zh;q=0.8'
        }
        r = requests.get(gl.url_online + "/file/"+gl.file_service_version+"/folder/" + gl.folder_id_online,
                        headers=headers,verify = False)
        print gl.url_online + "/file/"+gl.file_service_version+"/folder/" + gl.folder_id
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
