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


class TestJudgeRole(unittest.TestCase):
    """"""

    def test_001_get_judge_roles(self):
        """ /acl_admin/role // GetRoles"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        # print "请求参数：" + json.dumps(data)
        r = requests.get(gl.url + ":7111/acl_admin/role",
                         headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        result = json.loads(r.text)

    def test_002_get_judge_role_by_id(self):
        """ Get /acl_admin/role/:role_id // GetRole"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        # print "请求参数：" + json.dumps(data)
        r = requests.get(gl.url + ":7111/acl_admin/role/AQACd5VVkc7XKAAASVO5wgPY0BQlAAAA",
                         headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        result = json.loads(r.text)

    def test_003_add_judge_role_member(self):
        """ Post /acl_admin/role/:role_id/member // AddRoleMember"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = {
            "ent_id": "00000000000000000000000000000000",
            "role_id": "AQACd5VVkc7XKAAASVO5wgPY0BQlAAAA",
            # AQACd5VVkc7XKAAAY1J6ygPY0BQmAAAA   AQACd5VVkc7XKAAASVO5wgPY0BQlAAAA(上级)
            "user_id": "AQACd5VVkc7uCAAAAI1j7y6S2xQj2QEA",
        }
        print "请求参数：" + json.dumps(data)
        r = requests.post(gl.url + ":7111/acl_admin/role/AQACd5VVkc7XKAAASVO5wgPY0BQlAAAA/member",
                          data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        result = json.loads(r.text)

    def test_003_01_add_judge_role_member(self):
        """ Delete /acl_admin/role/:role_id/member/:user_id // RemoveRoleMember"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        r = requests.delete(
            gl.url + ":7111/acl_admin/role/AQACd5VVkc7XKAAAY1J6ygPY0BQmAAAA/member/AQACd5VVkc7uCAAAAI1j7y6S2xQj2QEA",
            headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        result = json.loads(r.text)

    def test_003_02_get_user_profile(self):
        """ Delete /acl_admin/role/:role_id/member/:user_id // RemoveRoleMember"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        r = requests.get(gl.url + ":7111/acl_admin/user/AQACk5HxFIb0DAAA5tAeDLDK8xTPGQAA/profile",
                         headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        result = json.loads(r.text)

    def test_004_get_judge_role_member(self):
        """  /acl_admin/role/:role_id/member """
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        # print "请求参数：" + json.dumps(data)
        r = requests.get(gl.url + ":7111/acl_admin/role/AQACd5VVkc7XKAAASVO5wgPY0BQlAAAA/member",
                         headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        result = json.loads(r.text)

    def test_005_create_judge_role(self):
        """  /acl_admin/role/:role_id/member """
        headers = {
            'x-token': gl.access_token_test,
            'content-type': gl.content_type
        }
        # AQACk5HxFIZ1DAAA01BlN9TF9BRzBgAA(管理员，最高级)    #AQACk5HxFIZ1DAAAA48EyDS79BSsAwAA
        data = {
            "ent_id": "AQACk5HxFIZ1DAAAA48EyDS79BSsAwAA",
            "role_id": "",
            "role_name": "性能测试",
            "parent_role_id": "AQACk5HxFIZ1DAAA5cRNcaHG9BSwBgAA",
            "case_access_for_account_owner": 3,
            "contact_access_for_account_owner": 3,
            "opportunity_access_for_account_owner": 3
        }
        r = requests.post(gl.url + ":7111/acl_admin/role",
                          data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        result = json.loads(r.text)
