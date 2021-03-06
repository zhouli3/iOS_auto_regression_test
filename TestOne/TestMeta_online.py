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
requests.packages.urllib3.disable_warnings()


class TestMeta_online(unittest.TestCase):
    """测试meta流程"""

    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."

    def test_1_get_all_metas(self):
        """Test Get /api/v1.0/tenant-name/all-metas 获取所有Meta"""
        headers = {
            'x-token': gl.access_token_online
        }
        data = "acl=true"
        print "请求数据：" + json.dumps(data)
        r = requests.get(gl.url_online + "/dml/api/"+gl.api_version+"/" + gl.online_tenant_name + "/all-metas?" + data,
                         headers=headers, verify=False)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["User"])

    def test_2_create_meta(self):
        """Test Post /api/v1.0/meiqia/car/meta 创建Meta"""
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type
        }
        name = "sgktestmeta" + str(random.randint(1, 9999))
        gl.meta_name = name
        data = {
            "display_name": name,
            "description": "the description of car."
        }
        print "请求数据：" + json.dumps(data)
        # meta创建和更新的端口是7020
        r = requests.post(gl.url_online + "/ddl/api/"+gl.api_version+"/" + gl.online_tenant_name + "/" + name + "/meta",
                          data=json.dumps(data),
                          headers=headers, verify=False)
        # r=requests.get(gl.url+"/api/v1.0/tenant-name/all-metas",params=data,headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["meta"])

    def test_2_1_create_meta(self):
        """Test Post /api/v1.0/meiqia/car/meta 创建Meta"""
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type
        }
        name = "sgktestmeta" + str(random.randint(1, 9999))
        data = {
            "display_name": name,
            "description": "the description of car."
        }
        print "请求数据：" + json.dumps(data)
        # meta创建和更新的端口是7020
        r = requests.post(gl.url_online + "/ddl/api/"+gl.api_version+"/" + gl.online_tenant_name + "/" + name + "/meta",
                          data=json.dumps(data),
                          headers=headers, verify=False)
        # r=requests.get(gl.url+"/api/v1.0/tenant-name/all-metas",params=data,headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["meta"])
        gl.meta_name = result["body"]["meta"]["display_name"]

    def test_3_get_point_meta(self):
        """Test Get /api/v1.0/meiqia/car/meta 获取Meta"""
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type
        }
        data = {}
        r = requests.get(gl.url_online + "/dml/api/"+gl.api_version+"/" + gl.online_tenant_name + "/" + gl.meta_name + "/meta",
                         headers=headers, verify=False)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["schema"])

    """
    以下均和修改Meta有关
    meta创建和更新的端口均是7020
    """

    def test_4_car_update_meta_displayname(self):
        """Test1 PUT /api/v1.0/meiqia/car/meta/modify-displayName"""
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type
        }
        data = {
            "display_name": gl.meta_name + "new"
        }
        r = requests.put(
            gl.url_online + "/ddl/api/"+gl.api_version+"/" + gl.online_tenant_name + "/" + gl.meta_name + "/meta/modify-displayName",
            data=json.dumps(data), headers=headers, verify=False)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["display_name"])

    def test_5_car_update_meta_description(self):
        """PUT /api/v1.0/meiqia/car/meta/modify-description"""
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type
        }
        data = {
            "description": "这是sgk测试用的meta"
        }
        r = requests.put(
            gl.url_online + "/ddl/api/"+gl.api_version+"/" + gl.online_tenant_name + "/" + gl.meta_name + "/meta/modify-description",
            data=json.dumps(data), headers=headers, verify=False)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["description"])

    def test_6_car_update_meta_addline(self):
        """PUT /api/v1.0/meiqia/car/meta/add"""
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type
        }
        data = {
            "name": "sgk_test_line",
            "display_name": "Wheel",
            "type": "integer",
            "nullable": False,
            "index": False,
            "unique": False,
            "default": {
                "value": "4",
                "dynamic": False
            }
        }
        r = requests.put(gl.url_online + "/ddl/api/"+gl.api_version+"/" + gl.online_tenant_name + "/" + gl.meta_name + "/meta/add",
                         data=json.dumps(data), headers=headers, verify=False)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["column"])
        gl.meta_line_name = result["body"]["column"]["name"]

    def test_6_car_update_meta_addline(self):
        """PUT /api/v1.0/meiqia/car/meta/add"""
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type
        }
        data = {"name": "Stage", "display_name": "商机阶段", "type": "path", "nullable": True, "options": {"related": "",
                                                                                                        "list": {
                                                                                                            "all": {
                                                                                                                "options_value": [
                                                                                                                    "初步意向",
                                                                                                                    "调研客服系统产品",
                                                                                                                    "了解产品认同美洽",
                                                                                                                    "确认产品和价格",
                                                                                                                    "赢单",
                                                                                                                    "输单"]}}}}
        r = requests.put(gl.url_online + "/ddl/api/"+gl.api_version+"/" + gl.online_tenant_name + "/" + gl.meta_name + "/meta/add",
                         data=json.dumps(data), headers=headers, verify=False)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["column"])
        gl.meta_line_name = result["body"]["column"]["name"]

    def test_7_update_meta_delline(self):
        """PUT /api/v1.0/meiqia/car/meta/drop"""
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type
        }
        data = {
            "name": gl.meta_line_name
        }
        r = requests.put(gl.url_online + "/ddl/api/"+gl.api_version+"/" + gl.online_tenant_name + "/" + gl.meta_name + "/meta/drop",
                         data=json.dumps(data), headers=headers, verify=False)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["name"])

    def test_8_update_meta_add_territoryid(self):
        """PUT /api/v1.0/meiqia/car/meta/add-territoryid"""
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type
        }
        r = requests.put(
            gl.url_online + "/ddl/api/"+gl.api_version+"/" + gl.online_tenant_name + "/" + gl.meta_name + "/meta/add-territoryid",
            headers=headers, verify=False)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["column"])

    # 执行后面的case之前先不要执行
    def test_9_update_meta_delmeta(self):
        """DELETE /api/v1.0/meiqia/car/meta"""
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type
        }
        r = requests.delete(gl.url_online + "/ddl/api/"+gl.api_version+"/" + gl.online_tenant_name + "/" + gl.meta_name + "/meta",
                            headers=headers, verify=False)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["name"])


gl.suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMeta_online))
