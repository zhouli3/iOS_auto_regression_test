# -*- coding: utf-8 -*-
import unittest
import json
import requests
import random
import time
import uuid
from GlobalVariables import gl

"""解决'ascii' codec can't decode byte 0xe6"""
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class TestData(unittest.TestCase):
    """测试 date 相关的接口"""

    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."

    def test_1_get_default_values(self):
        """GET  /api/v1.0/meiqia/car/default-values
            获取已设置的默认值
        """
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        r = requests.get(gl.url + ":7010/api/"+gl.api_version+"/" + gl.tenant_name + "/Leads/default-values",
                         headers=headers)
        print gl.url + ":7010/api/"+gl.api_version+"/" + gl.tenant_name + "/Leads/default-values"
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])

    def test_2_create_data_in_meta(self):
        """POST /api/v1.0/meiqia/car"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        # 此处的field名称和值可以通过创建的时候保存获得，也可以通过查询获得
        data = {
            "objects": [
                {
                    "name": "sgktest_pp1",
                    "sgk_test_line":2
                },
                {
                    "name": "sgktest_pp2",
                    "sgk_test_line":3
                },
                {
                    "name": "sgktest_pp3",
                    "sgk_test_line":4
                }
            ]
        }
        data = {"objects": [{"name": "商机autotest1012160510", "AccountID": "3c5938c9917ca43b73cad4f5453623b3",
                             "Amount": {"symbol": "CNY", "value": 10000000}, "CloseDate": "2017-10-12T08:03:43Z",
                             "Stage1": "初步意向", "Probability1": "20%", "Stage2": "14天（30天）保持跟进", "Probability2": "20%",
                             "Phone": None, "IndustryCategory": None, "Industry": None, "OtherService": None,
                             "AffiliatedDepartment": None, "Competitor": None,
                             "CompetitorPrice": {"symbol": None, "value": None}, "Disagreements": None, "Demands": None,
                             "Excitements": None, "FacilitatorType": None, "FacilitatorDiscount": 0,
                             "FacilitatorBusiness": None, "FacilitatorDoubts": None, "LosingStage": None,
                             "LosingReason": None, "LosingDescription": None, "StageUpdatedAt": "2017-10-12T08:03:43Z",
                             "Description": None},{"name": "商机autotest1012160510", "AccountID": "3c5938c9917ca43b73cad4f5453623b3",
                             "Amount": {"symbol": "CNY", "value": 10000000}, "CloseDate": "2017-10-12T08:03:43Z",
                             "Stage1": "初步意向", "Probability1": "20%", "Stage2": "14天（30天）保持跟进", "Probability2": "20%",
                             "Phone": None, "IndustryCategory": None, "Industry": None, "OtherService": None,
                             "AffiliatedDepartment": None, "Competitor": None,
                             "CompetitorPrice": {"symbol": None, "value": None}, "Disagreements": None, "Demands": None,
                             "Excitements": None, "FacilitatorType": None, "FacilitatorDiscount": 0,
                             "FacilitatorBusiness": None, "FacilitatorDoubts": None, "LosingStage": None,
                             "LosingReason": None, "LosingDescription": None, "StageUpdatedAt": "2017-10-12T08:03:43Z",
                             "Description": None},{"name": "商机autotest1012160510", "AccountID": "3c5938c9917ca43b73cad4f5453623b3",
                             "Amount": {"symbol": "CNY", "value": 10000000}, "CloseDate": "2017-10-12T08:03:43Z",
                             "Stage1": "初步意向", "Probability1": "20%", "Stage2": "14天（30天）保持跟进", "Probability2": "20%",
                             "Phone": None, "IndustryCategory": None, "Industry": None, "OtherService": None,
                             "AffiliatedDepartment": None, "Competitor": None,
                             "CompetitorPrice": {"symbol": None, "value": None}, "Disagreements": None, "Demands": None,
                             "Excitements": None, "FacilitatorType": None, "FacilitatorDiscount": 0,
                             "FacilitatorBusiness": None, "FacilitatorDoubts": None, "LosingStage": None,
                             "LosingReason": None, "LosingDescription": None, "StageUpdatedAt": "2017-10-12T08:03:43Z",
                             "Description": None}
        ]}
        print "请求参数data：" + json.dumps(data)
        r = requests.post(gl.url + ":7010/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name,
                          data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        data_list = result["body"]
        for index in range(len(data_list)):
            gl.data_name.insert(index, data_list[index]["name"])
            gl.data_id.insert(index, data_list[index]["id"])
            gl.data_version.insert(index, data_list[index]["version"])
        print  gl.data_name, gl.data_id, gl.data_version

    def test_3_get_data_for_point_requirements(self):
        """GET /api/v1.0/meiqia/car/query?"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        update_date = str(time.strftime('%m/%d/%Y %H:%M:%S', time.localtime(time.time())))
        # http://10.102.1.64:7010/api/v1.0/meiqia/car/query?
        # order_by=created_at&order_flag=ASC&order_by=updated_at&order_flag=DESC&offset=0&limit=50&
        # in={"field": "wheel", "in_list": [2,3,4,5,6,7,8]}&
        # view_filter={"filter_from": "all","filter": {"logical_relation": "1", "expressions": [{"field": "wheel", "operator": ">=", "operands": ["5"]}]}}
        # order_by=updated_at&order_flag=DESC&update_date=10/11/2017 16:28:06&
        # view_filter={"filter":{"logical_relation":"1","expressions":[{"display_name":"姓名","field":"name","operator":"CONTAINS","operands":["'sgk'"]}]},"filter_from":"all"}&
        # offset=0&limit=50&curField=updated_at&curFlag=DESC
        # json_in = {"field": gl.meta_line_name, "in_list": ["zhangsan1"]}
        view_filter = {
            "filter": {
                "logical_relation": "1",
                "expressions": [
                    {"display_name": "机会名称", "field": "name", "operator": "CONTAINS", "operands": ["'autotest'"]}]
            },
            "filter_from": "all"
        }
        # 以上字段名可以通过查询获得
        print "请求参数,view_filter：" + json.dumps(view_filter)
        r = requests.get(
            gl.url + ":7010/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/query?order_by=updated_at&order_flag=DESC&update_date=" + update_date +
            "&offset=0&limit=20&curField=updated_at&curFlag=DESC&"
            "view_filter=" + json.dumps(view_filter),
            headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])

    def test_4_get_data_from_data_id(self):
        """GET /api/v1.0/meiqia/car/object_id"""
        # AQACk5HxFIb0DQAAvvTBjvTW6xQ4CwAA
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        randnum = random.randint(0, len(gl.data_id) - 1)
        print 4, gl.data_id[randnum]
        print gl.data_id[randnum]
        r = requests.get(gl.url + ":7010/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/" + gl.data_id[randnum],
                         headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        # gl.data_version[randnum]+=1
        # print gl.data_version

    def test_5_update_data_by_id(self):
        """PUT /api/v1.0/meiqia/car/object_id"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = {
            "name": "sgktest_p1",
            "version": 0  # version初始值为0，随后每修改一次递增1
        }
        randnum = random.randint(0, len(gl.data_id) - 1)
        print 5, gl.data_id[randnum]
        r = requests.put(gl.url + ":7010/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/" + gl.data_id[randnum],
                         data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        gl.data_version[randnum] += 1

    def test_6_transfer_data_by_id(self):
        """PUT /api/v1.0/meiqia/car/object_id/transfer?version=0"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = {
            "owner": "01bc54a795e79def738a5e1fae0ec229"
        }
        randnum = random.randint(0, len(gl.data_version) - 1)
        # 此处的 version每修改一次data，version就会自动+1
        print 6, str(gl.data_version[randnum])
        r = requests.put(
            gl.url + ":7010/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/" + gl.data_id[
                randnum] + "/transfer?version=" + str(gl.data_version[randnum]),
            data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        gl.data_version[randnum] += 1

    def test_7_transfer_data_batch(self):
        """PUT /api/v1.0/meiqia/car/object_list/transfer"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = {
            "owner": "01bc54a795e79def738a5e1fae0ec229",
            "objects": [
                {
                    "object_id": gl.data_id[0],
                    "version": gl.data_version[0]
                },
                {
                    "object_id": gl.data_id[1],
                    "version": gl.data_version[1]
                }
            ]
        }
        print "请求参数 object list：" + json.dumps(data)
        r = requests.put(
            gl.url + ":7010/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/object_list/transfer",
            data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        gl.data_version[1] += 1
        gl.data_version[0] += 1

    def test_8_delete_data_by_id(self):
        """DELETE /api/v1.0/meiqia/car/object_id?version=0"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        id = gl.data_id[0]
        print "请求参数data id：" + id
        r = requests.delete(
            gl.url + ":7010/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/" + id + "?version=" + str(
                gl.data_version[0]),
            headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        del gl.data_id[0]
        del gl.data_name[0]
        del gl.data_version[0]

    def test_9_delete_data_batch(self):
        """DELETE /api/v1.0/meiqia/car/object_list"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = {
            "objects": [
                {
                    "object_id": gl.data_id[0],
                    "version": gl.data_version[0]
                },
                {
                    "object_id": gl.data_id[1],
                    "version": gl.data_version[1]
                }
            ]
        }
        print "请求参数object list：" + json.dumps(data)
        r = requests.delete(
            gl.url + ":7010/api/"+gl.api_version+"/" + gl.tenant_name + "/" + gl.meta_name + "/object_list",
            data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])


gl.suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestData))
