# -*- coding: utf-8 -*-
import unittest
import json
import urllib
import requests
import uuid
from GlobalVariables import gl

"""解决'ascii' codec can't decode byte 0xe6"""
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
requests.packages.urllib3.disable_warnings()


class TestActions(unittest.TestCase):
    """测试 actions相关接口"""

    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."

    def test_1_get_all_actions(self):
        """GET /api/v1.0/meiqia/actions
            获取所有的actions，请求路径中不包含meta名称
        """
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type
        }
        r = requests.get(
            gl.url_online + "/dml/api/" + gl.api_version + "/" + gl.online_tenant_name + "/" + gl.meta_name + "/actions",
            headers=headers, verify=False)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])

    def test_2_get_meta_actions(self):
        """GET /api/v1.0/meiqia/actions
            获取指定meta所有的actions，请求路径中包含meta名称
        """
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type
        }
        r = requests.get(
            gl.url_online + "/dml/api/" + gl.api_version + "/" + gl.online_tenant_name + "/" + gl.meta_name + "/actions",
            headers=headers, verify=False)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        gl.action_merge_data_pre_name = result["body"]["merge_data_pre"]["name"]
        gl.action_merge_data_commit_name = result["body"]["merge_data_commit"]["name"]
        gl.action_merge_data_pre_mergeid = result["body"]["merge_data_pre"]["param"]["optional"]["delete_ids"]
        gl.action_merge_data_pre_deleteid = result["body"]["merge_data_pre"]["param"]["optional"]["merge_ids"]

    def test_3_run_point_meta_action_merge_data_pre(self):
        """PUT /api/v1.0/meiqia/object/actions/run/merge_data_pre
        运行指定 Action  merge_data_pre"""
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type
        }
        data = {
            "optional": {
                "merge_ids": ["", "", ""],
                "delete_ids": []
            }
        }
        print "运行的Action name：" + gl.action_merge_data_pre_name
        print "请求参数：" + json.dumps(data)
        r = requests.put(
            gl.url_online + "/dml/api/" + gl.api_version + "/" + urllib.quote(
                gl.online_tenant_name) + "/" + gl.meta_name + "/actions/run/" + gl.action_merge_data_pre_name,
            data=json.dumps(data), headers=headers, verify=False)
        print gl.url_online + "/dml/api/" + gl.api_version + "/" + gl.online_tenant_name + "/" + gl.meta_name + "/actions/run/" + gl.action_merge_data_pre_name
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        self.assertEqual(result["body"]["permission"]["runnable"], True)

    def test_4_run_point_meta_action_merge_data_commit(self):
        """PUT /api/v1.0/meiqia/object/actions/run/merge_data_commit
        运行指定 Action  merge_data_commit"""
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type
        }
        # 此处的gl.meta_name所对应的值，可以从查询请求中获取，也可以在最初创建meta的时候保存表结构
        # 需要改成参数形式
        data = {
            "datas": {
                "User": [
                    {
                        "MobilePhone": "+86 13333333333",
                        "name": "sgktest"
                    }
                ]
            },
            "optional": {
                "merge_ids": ["", "", ""],
                "delete_ids": []
            }
        }
        print "运行的Action name：" + gl.action_merge_data_commit_name
        print "请求参数：" + json.dumps(data)
        r = requests.put(
            gl.url_online + "/dml/api/" + gl.api_version + "/" + gl.tenant_name + "/User/actions/run/" + gl.action_merge_data_commit_name,
            data=json.dumps(data), headers=headers, verify=False)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])

    def test_5_run_point_meta_action_leads_to_account_and_contact_pre(self):
        """PUT /api/v1.0/meiqia/Leads/actions/run/leads_to_account_and_contact_pre"""
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type
        }
        # 此处的id可以是 merge_data_commit 接口返回的值
        data = {
            "datas": {
                "Leads": [
                    {
                        "id": "AQACk5HxFIb0DQAAsQ__kE3U6xRxBwAA"
                    }
                ]
            },
            "optional": {
                "merge_ids": ["", "", ""],
                "delete_ids": []
            }
        }
        print "运行的Action name：" + gl.action_leads_to_account_and_contact_pre_name
        print "请求参数：" + json.dumps(data)
        r = requests.put(
            gl.url_online + "/dml/api/" + gl.api_version + "/" + gl.tenant_name + "/Leads/actions/run/" + gl.action_leads_to_account_and_contact_pre_name,
            data=json.dumps(data), headers=headers, verify=False)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])

    def test_6_run_point_meta_action_leads_to_account_and_contact_commit(self):
        """PUT /api/v1.0/meiqia/Leads/actions/run/leads_to_account_and_contact_commit"""
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type
        }
        # 此处的Account和Contact的内容可以从leads_to_account_and_contact_pre请求中得到
        # 后面改成参数形式,id只能被使用一次
        data = {
            "datas": {
                "Leads": [
                    {
                        "id": "AQACk5HxFIb0DQAAHw4ffbzV6xRFCQAA"
                    }
                ],
                "Account": [
                    {
                        "Address": {
                            "city": None,
                            "country": None,
                            "state": None,
                            "street": None
                        },
                        "AffiliatedDepartment": None,
                        "Description": None,
                        "Industry": None,
                        "IndustryCategory": None,
                        "Phone": "+86 13333333333",
                        "PostalCode": None,
                        "WeChat": None,
                        "name": "sgktest"
                    }
                ],
                "Contact": [
                    {
                        "Address": {
                            "city": None,
                            "country": None,
                            "state": None,
                            "street": None
                        },
                        "AffiliatedDepartment": None,
                        "Department": None,
                        "Description": None,
                        "Email": None,
                        "Gender": None,
                        "MobilePhone": None,
                        "Phone": "+86 13333333335",
                        "PostalCode": None,
                        "Title": None,
                        "WeChat": None,
                        "name": "sgktest"
                    }
                ]
            }
        }
        print "运行的Action name：" + gl.action_leads_to_account_and_contact_commit_name
        print "请求参数：" + json.dumps(data)
        r = requests.put(
            gl.url_online + "/dml/api/" + gl.api_version + "/" + gl.tenant_name + "/Leads/actions/run/" + gl.action_leads_to_account_and_contact_commit_name,
            data=json.dumps(data), headers=headers, verify=False)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])


gl.suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestActions))
