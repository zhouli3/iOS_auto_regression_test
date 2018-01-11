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


class TestLayOutAll(unittest.TestCase):
    """LayOut相关接口"""
    def test_001_get_tenant_id_by_name(self):
        """通过租户名称获取租户id
        http://10.102.2.212:7121/account/orgs?name=SGSoft%e6%b5%8b%e8%af%95"""
        headers = {
            'Authorization': gl.account_token
        }
        tenant_name = urllib.quote(gl.layout_tenantname)
        print tenant_name
        r = requests.get(gl.url + ":7121/account/orgs?name="+tenant_name, headers=headers)
        print r, r.text
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["orgs"])
        gl.layout_tenantid = result["body"]["orgs"][0]["id"]
        print gl.layout_tenantid

    def test_002_create_layout_json(self):
        """创建LayOut Json"""
        tenant_id = gl.layout_tenantid
        jsonTemp = gl.layout_json_temp
        return jsonTemp

    def test_003_upload_layout_json(self):
        """上传layout使用的json
        Referer: http://10.102.1.64:8555/json
        http://10.102.1.64:8555/abc"""
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type
        }
        jsonStr = gl.layout_json_temp
        # "pwd": "CBqeJFFjZqjjUR6fFNzjFJjJ",
        # "userid": "zhangsongshi"
        data = {
            "json": json.dumps(jsonStr),
            "pwd": "1234567",
            "userid": "admin"
        }
        print "请求参数：" + json.dumps(data)
        r = requests.post("http://"+gl.layout_env_IP_Online + ":8555/abc", data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["error"], False)
        self.assertEqual(r.json()["message"], "success")

    def create_layout_json(self):
        """创建LayOut Json"""
        tenant_id = test_3_get_tenant_id_by_name(self)
        jsonTemp = {
            tenant_id: {
                "objects": [
                    {"display_name": "用户", "name": "User"}
                ],

                "global_header": [
                    {"display_name": "用户", "name": "User"},
                    {"display_name": "线索", "name": "Leads"},
                    {"display_name": "客户", "name": "Account"},
                    {"display_name": "联系人", "name": "Contact"},
                    {"display_name": "商机", "name": "Opportunity"},
                    {"display_name": "合同", "name": "Contract"},
                    {"display_name": "充值订单", "name": "Recharge"},
                    {"display_name": "回款计划", "name": "Pay"},
                    {"display_name": "退款订单", "name": "Refund"},
                    {"display_name": "发票", "name": "Invoice"}
                ],

                "ios": {
                    "User": ["id", "name", "Phone", "Department", "BirthDate", "Email", "EmployeeID", "EntryDate",
                             "Gender", "Hobbies", "Manager", "MobilePhone", "NativePlace", "QQ", "Title", "created_at",
                             "owner"]
                },
                "android": {
                    "User": ["id", "name", "Phone", "Department", "BirthDate", "Email", "EmployeeID", "EntryDate",
                             "Gender", "Hobbies", "Manager", "MobilePhone", "NativePlace", "QQ", "Title", "created_at",
                             "owner"]
                },
                "web": {
                    "User_global_config": {
                        "create_order": ["id", "name", "Phone", "Department", "BirthDate", "Email", "EmployeeID",
                                         "EntryDate", "Gender", "Hobbies", "Manager", "MobilePhone", "NativePlace",
                                         "QQ", "Title"],
                        "update_order": ["id", "name", "Phone", "Department", "BirthDate", "Email", "EmployeeID",
                                         "EntryDate", "Gender", "Hobbies", "Manager", "MobilePhone", "NativePlace",
                                         "QQ", "Title"]
                    },
                    "User_list_config": {
                        "tableOrder": ["id", "name", "Phone", "Department", "BirthDate", "Email", "EmployeeID",
                                       "EntryDate", "Gender", "Hobbies", "Manager", "MobilePhone", "NativePlace", "QQ",
                                       "Title", "created_at", "owner"],
                        "createOrder": [],
                        "updateOrder": []
                    },
                    "User_detail_config": {
                        "pageHeaderOrder": ["id", "name", "Phone", "Department", "BirthDate", "Email", "EmployeeID",
                                            "EntryDate", "Gender", "Hobbies", "Manager", "MobilePhone", "NativePlace",
                                            "QQ", "Title", "created_at", "owner"],
                        "tabDetailOrder": ["id", "name", "Phone", "Department", "BirthDate", "Email", "EmployeeID",
                                           "EntryDate", "Gender", "Hobbies", "Manager", "MobilePhone", "NativePlace",
                                           "QQ", "Title", "created_at", "owner"],
                        "updateOrder": []
                    }
                }
            }
        }

    def test_3_get_tenant_id_by_name(self):
        """通过租户名称获取租户id
        http://10.102.2.212:7121/account/orgs?name=SGSoft%e6%b5%8b%e8%af%95"""
        headers = {
            'Authorization': gl.account_token
        }
        tenant_name = urllib.quote("SGSoft测试")
        print tenant_name
        r = requests.get(gl.url + ":7121/account/orgs?name="+tenant_name, headers=headers)
        print r, r.text
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["orgs"])
        tenant_id = result["body"]["orgs"][0]["id"]
        print tenant_id
        return tenant_id


gl.suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestLayOutAll))