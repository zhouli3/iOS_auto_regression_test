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


class TestJudgeOwd(unittest.TestCase):
    """权限Owd接口测试"""

    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."

    """
    type OWDItem struct {
	EntId              string              `protobuf:"bytes,1,opt,name=ent_id,json=entId,proto3" json:"ent_id,omitempty"`
	ObjectName         string              `protobuf:"bytes,2,opt,name=object_name,json=objectName,proto3" json:"object_name,omitempty"`
	AccessLevel        OWDItem_AccessLevel `protobuf:"varint,3,opt,name=access_level,json=accessLevel,proto3,enum=judge.OWDItem_AccessLevel" json:"access_level,omitempty"`
	GrantRoleHierarchy bool                `protobuf:"varint,4,opt,name=grant_role_hierarchy,json=grantRoleHierarchy,proto3" json:"grant_role_hierarchy,omitempty"`
    }
    """

    def test_001_acl_add_owd_item(self):
        """Post /acl_admin/organization_wide_default/owd_item
        添加owd item"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        """
        type OWDItem_AccessLevel int32

        const (
	        OWDItem_Private                 OWDItem_AccessLevel = 0
	        OWDItem_ControlledByParent      OWDItem_AccessLevel = 1
	        OWDItem_PublicRead              OWDItem_AccessLevel = 2
	        OWDItem_PublicReadWrite         OWDItem_AccessLevel = 3
	        OWDItem_PublicReadWriteTransfer OWDItem_AccessLevel = 4
	        OWDItem_PublicFullAccess        OWDItem_AccessLevel = 5
        )
        """
        data = {
            "ent_id": gl.acl_group_ent_id,  # 线上请改成测试企业
            "object_name": "User",
            "access_level": 5,
            "grant_role_hierarchy": True
        }
        print "请求参数："+json.dumps(data)
        r = requests.post(gl.url + ":7111/acl_admin/organization_wide_default/owd_item", data=json.dumps(data),
                          headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"],0)
        self.assertEqual(r.json()["success"],True)
        result = json.loads(r.text)

    def test_002_get_acl_owd(self):
        """Get /acl_admin/organization_wide_default // GetOWD
        查询owd"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        r = requests.get(gl.url + ":7111/acl_admin/organization_wide_default",
                          headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        result = json.loads(r.text)
        self.assertIsNotNone(result["items"])