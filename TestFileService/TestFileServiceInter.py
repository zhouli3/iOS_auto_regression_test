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
            'x-token': gl.access_token,
            'content-type': "multipart/form-data",
            'accept-language': 'zh-CN,zh;q=0.8',
        }
        data = {"formfile": "D:\\work\\12365.png"}
        r = requests.post(gl.url + ":7001/"+gl.file_service_version+"/folder/" + gl.folder_id + "/file?create_thumb=true",
                         data = json.dumps(data),headers=headers)
        '''r = requests.post(
            gl.url + ":7001/api/" + gl.api_version + "/folder/" + gl.folder_id + "/file?create_thumb=true",
            fromfile=json.dumps(data), headers=headers)'''
        '''r = requests.get(
            gl.url + ":7001/api/" + gl.api_version + "/file-service/ping",headers=headers)'''
        # print gl.url + ":7001/"+gl.file_service_version+"/folder/" + gl.folder_id + "/file?create_thumb=true"
        print gl.url + ":7001/api/" + gl.api_version + "/file-service/folder/" + gl.folder_id + "/file?create_thumb=true"
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)

    def test_002_get_folder_file(self):
        """:7001/v1/folder/:folder_id/file?create_thumb=true -X POST """
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type,
            'accept-language': 'zh-CN,zh;q=0.8'
        }
        r = requests.get(gl.url + ":7001/api/" + gl.api_version + "/file-service/folder/" + gl.folder_id,
                         headers=headers)
        print gl.url + ":7001/" + gl.file_service_version + "/folder/" + gl.folder_id
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)

    def test_003_copy_folder_handler(self):
        """:7001/v1/folder/:folder_id/file?create_thumb=true -X POST """
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type,
            'accept-language': 'zh-CN,zh;q=0.8'
        }
        r = requests.post(
            gl.url + ":7001/api/" + gl.api_version + "/file-service/folder/" + gl.folder_id + "/copy?object_name=Invoice&field_name=Proofs&record_id=AQACk5HxFIZiAwAAIRnJDeAW8RRqAAAA",
            headers=headers)
        print gl.url + ":7001/" + gl.file_service_version + "/folder/" + gl.folder_id
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)

    def test_004_copy_file_handler(self):
        """:7001/v1/folder/:folder_id/file?create_thumb=true -X POST """
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type,
            'accept-language': 'en-US,en;q=0.8'
        }
        r = requests.post(
            gl.url + ":7001/api/" + gl.api_version + "/file-service/" + gl.file_id + "/copy?object_name=Invoice&field_name=Proofs&record_id=AQACk5HxFIZiAwAAIRnJDeAW8RRqAAAA",
            headers=headers)
        print gl.url + ":7001/api/" + gl.api_version + "/file-service/" + gl.file_id + "/copy?object_name=Invoice&field_name=Proofs&record_id=AQACk5HxFIZiAwAAIRnJDeAW8RRqAAAA"
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
