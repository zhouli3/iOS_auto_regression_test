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


class TestTeamMemberRoles(unittest.TestCase):
    """测试 Team Member Roles相关接口"""

    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."

    def test_1_create_team_member_roles(self):
        """PUT /api/v1.0/meiqia/car/meta/team-member-roles/add"""

        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = {
            "new_roles": ["规则1：不许抽烟",
                          "规则2：不许喝酒",
                          "规则3：不许Game"]
        }
        print "请求参数：" + json.dumps(data)
        r = requests.put(
            gl.url + ":7020/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/meta/team-member-roles/add",
            data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["team_member_roles"])

    def test_2_get_team_member_roles(self):
        """GET /api/v1.0/meiqia/car/meta/team-member-roles"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        r = requests.get(
            gl.url + ":7020/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/meta/team-member-roles",
            headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["team_member_roles"])

    def test_3_update_team_member_roles(self):
        """PUT /api/v1.0/meiqia/car/meta/team-member-roles/alter"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = [
            {
                "old_role": "规则1：不许抽烟", "new_role": "规则1：No smoking"
            },
            {
                "old_role": "规则3：不许Game", "new_role": "规则3：No Gaming"
            }
        ]
        print "请求参数：" + json.dumps(data)
        r = requests.put(
            gl.url + ":7020/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/meta/team-member-roles/alter",
            data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["team_member_roles"])

    def test_4_delete_team_member_roles(self):
        """PUT /api/v1.0/meiqia/car/meta/team-member-roles/del"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = [
            {
                "old_role": "规则1：不许抽烟", "new_role": "规则1：No smoking"
            },
            {
                "old_role": "规则3：不许Game", "new_role": "规则3：No Gaming"
            }
        ]
        print "请求参数：" + json.dumps(data)
        r = requests.put(
            gl.url + ":7020/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/meta/team-member-roles/del",
            data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["team_member_roles"])


gl.suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestTeamMemberRoles))


