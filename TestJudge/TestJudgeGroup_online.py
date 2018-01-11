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


class TestJudgeGroup(unittest.TestCase):
    """权限group接口测试"""

    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."

    def test_001_create_acl_group(self):
        """POST /acl_admin/group
        新建Group"""
        # 下面是Group结构，需要传入的参数有三个
        """type Group struct {
	        EntId     string `protobuf:"bytes,1,opt,name=ent_id,json=entId,proto3" json:"ent_id,omitempty"`
	        GroupId   string `protobuf:"bytes,2,opt,name=group_id,json=groupId,proto3" json:"group_id,omitempty"`
	        GroupName string `protobuf:"bytes,3,opt,name=group_name,json=groupName,proto3" json:"group_name,omitempty"`
        }"""
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type
        }
        data = {
            "ent_id": gl.acl_group_ent_id,  # 线上请改成测试企业
            "group_name": "SgkTestGroup1102002",
            "group_id": None
        }
        print "请求参数：" + json.dumps(data)
        r = requests.post("http://10.100.250.6:7111/acl_admin/group", data=json.dumps(data),
                          headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        result = json.loads(r.text)
        self.assertIsNotNone(result["group_id"])
        gl.acl_group_id = result["group_id"]
        gl.acl_group_name = result["group_name"]

    def test_002_update_group_by_group_id(self):
        """PUT /acl_admin/group/:group_id
        更改Group"""
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type
        }
        gl.acl_group_name = gl.acl_group_name + "new"
        data = {
            "ent_id": gl.acl_group_ent_id,
            "group_name": gl.acl_group_name,
            "group_id": gl.acl_group_id
        }
        print "请求参数：" + json.dumps(data)
        r = requests.put("http://10.100.250.6:7111/acl_admin/group/" + gl.acl_group_id, data=json.dumps(data),
                         headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        result = json.loads(r.text)
        self.assertEqual(result["code"], 0)

    def test_003_get_group_by_id(self):
        """GET /acl_admin/group/:group_id
        查询Group"""
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type
        }
        # print "请求参数：" + json.dumps(data)
        r = requests.get("http://10.100.250.6:7111/acl_admin/group/" + gl.acl_group_id,
                         headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        result = json.loads(r.text)
        self.assertEqual(result["group_name"], gl.acl_group_name)

    def test_004_get_all_groups(self):
        """GET /acl_admin/group
        获取当前企业下所有group"""
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type
        }
        # print "请求参数：" + json.dumps(data)
        r = requests.get("http://10.100.250.6:7111/acl_admin/group",
                         headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        result = json.loads(r.text)
        self.assertIsNotNone(result["groups"])

    def test_005_add_group_member(self):
        """Post /acl_admin/group/:group_id/member
        想Group中添加成员"""
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type
        }
        data = {
            "ent_id": gl.acl_group_ent_id,
            "group_id": gl.acl_group_id,
            "member_id": gl.acl_group_member_id,
            "member_type": gl.acl_group_member_type
        }
        print "请求参数：" + json.dumps(data)
        r = requests.post("http://10.100.250.6:7111/acl_admin/group/" + gl.acl_group_id + "/member", data=json.dumps(data),
                          headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        result = json.loads(r.text)
        self.assertEqual(result["code"], 0)
        self.assertEqual(result["success"], True)

    def test_006_get_acl_group_member(self):
        """Get /acl_admin/group/:group_id/member
        查询group member"""
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type
        }
        r = requests.get("http://10.100.250.6:7111/acl_admin/group/" + gl.acl_group_id + "/member",
                         headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        result = json.loads(r.text)
        self.assertIsNotNone(result["group_members"])

    def test_007_delete_group_member(self):
        """Delete /acl_admin/group/:group_id/member/:member_type/:member_id
        通过memberid 移除成员"""
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type
        }
        r = requests.delete(
            "http://10.100.250.6:7111/acl_admin/group/" + gl.acl_group_id + "/member/" + str(gl.acl_group_member_type) + "/" + gl.acl_group_member_id,
            headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        result = json.loads(r.text)
        self.assertEqual(result["code"], 0)
        self.assertEqual(result["success"], True)

    def test_008_delete_group_by_id(self):
        """Delete /acl_admin/group/:group_id
        删除指定Group"""
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type
        }
        r = requests.delete(
            "http://10.100.250.6:7111/acl_admin/group/" + gl.acl_group_id,
            headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        result = json.loads(r.text)
        self.assertEqual(result["code"], 0)
        self.assertEqual(result["success"], True)
