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
requests.packages.urllib3.disable_warnings()  # 解决访问HTTPS错误


class TestMPayAll(unittest.TestCase):
    """支付服务接口测试"""

    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."

    def test_001_create_customer(self):
        """POST /api/v1.0/mpay/customer
        创建客户"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        # 创建客户前，需要先创建一个租户，创建的客户external_id必须是这里创建的租户的id
        # 这里的租户是指类型为CRM_TENANT的客户，且这种类型的客户只能创建一个
        data = {
            "name": "liubeiqwer",
            "phone": "+86 17888989812",
            "email": "liubeiqwer@qq.com",
            "weixin": "liubeiqwer",
            "type": "CRM_TENANT"
        }
        print "请求参数是：" + json.dumps(data)
        r = requests.post(gl.url + ":7145/api/" + gl.api_version + "/mpay/customer", data=json.dumps(data),
                          headers=headers)
        print gl.url + ":7145/api/" + gl.api_version + "/mpay/customer"
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        gl.mpay_tenant_id = result["body"]["customer"]["id"]
        # 接下来在上面创建的租户下创建客户，类型为 CRM_TENANT_ACCOUNT
        data = {
            "name": "guanyu",
            "phone": "+86 17888989812",
            "email": "guanyu123@qq.com",
            "weixin": "guanyu123",
            "type": "CRM_TENANT_ACCOUNT",
            "external_id": str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
            # str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
        }
        print "请求参数是：" + json.dumps(data)
        r = requests.post(gl.url + ":7145/api/" + gl.api_version + "/mpay/customer", data=json.dumps(data),
                          headers=headers)
        print gl.url + ":7145/api/" + gl.api_version + "/mpay/customer"
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        gl.mpay_customer_id = result["body"]["customer"]["id"]
        gl.mpay_customer_name = result["body"]["customer"]["name"]
        gl.mpay_customer_external_id = result["body"]["customer"]["external_id"]

    def test_002_update_customer_info_by_id(self):
        """PUT /api/v1.0/mpay/customer/:id
        更改客户"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = {
            "name": "Jack Jan",
            "phone": "+86 17711111111",
            "email": "test@meiqia.com",
            "weixin": "Jack1234"
        }
        print "请求参数是：" + json.dumps(data)
        r = requests.put(gl.url + ":7145/api/" + gl.api_version + "/mpay/customer/" + gl.mpay_customer_id,
                         data=json.dumps(data), headers=headers)
        print gl.url + ":7145/api/" + gl.api_version + "/mpay/customer/" + gl.mpay_customer_id
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        gl.mpay_customer_id = result["body"]["customer"]["id"]
        gl.mpay_customer_name = result["body"]["customer"]["name"]
        gl.mpay_customer_external_id = result["body"]["customer"]["external_id"]

    def test_003_query_customer_info(self):
        """GET /api/v1.0/mpay/customer/query
        查询客户"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = {
            "id": gl.mpay_customer_id,
            "phone": gl.mpay_customer_phone,
            "external_id": gl.mpay_customer_external_id,
            "type": gl.mpay_customer_type
        }
        print "请求参数是：" + json.dumps(data)
        r = requests.get(
            gl.url + ":7145/api/" + gl.api_version + "/mpay/customer/query?param=" + urllib.quote(json.dumps(data)),
            headers=headers)
        print gl.url + ":7145/api/" + gl.api_version + "/mpay/customer/query?param=" + urllib.quote(json.dumps(data))
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])

    def test_004_create_account(self):
        """POST /api/v1.0/mpay/account
        创建账户"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        # 创建CRM_TENANT类型的account，作为收款方，related_account_type必须为MQ
        data = {
            "name": "zhangsan13101",
            "customer_id": gl.mpay_tenant_id,
            "related_account_id": "zhangsan11131101",
            "related_account_type": "MQ"
        }
        print "请求参数是：" + json.dumps(data)
        r = requests.post(
            gl.url + ":7145/api/" + gl.api_version + "/mpay/account",
            data=json.dumps(data), headers=headers)
        print gl.url + ":7145/api/" + gl.api_version + "/mpay/account"
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        gl.mpay_account_id_shoukuan = result["body"]["account"]["id"]
        # 创建类型为CRM_TENANT_ACCOUNT的账户，作为付款方，related_account_type可以为其他
        data = {
            "name": "zhangsan12562121261",
            "customer_id": gl.mpay_customer_id,
            "related_account_id": "zhangsan12511313111",
            "related_account_type": "ALI"
        }
        print "请求参数是：" + json.dumps(data)
        r = requests.post(
            gl.url + ":7145/api/" + gl.api_version + "/mpay/account",
            data=json.dumps(data), headers=headers)
        print gl.url + ":7145/api/" + gl.api_version + "/mpay/account"
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        gl.mpay_account_id_fukuan = result["body"]["account"]["id"]

    def test_005_update_account_info_by_id(self):
        """PUT /api/v1.0/mpay/account/:id
        更改账户"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        name = "测试Name" + str(random.randint(1, 10))
        data = {
            "name": name,
        }
        print "请求参数是：" + json.dumps(data)
        r = requests.put(
            gl.url + ":7145/api/" + gl.api_version + "/mpay/account/" + gl.mpay_account_id_shoukuan,
            data=json.dumps(data), headers=headers)
        print gl.url + ":7145/api/" + gl.api_version + "/mpay/account" + gl.mpay_account_id_shoukuan
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        self.assertEqual(result["body"]["account"]["name"], name)

    def test_006_query_account_info(self):
        """GET /api/v1.0/mpay/account/query
        查询账户"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = {
            "id": gl.mpay_account_id_shoukuan,
            "customer_id": gl.mpay_account_related_customer_id,
            "related_account_type": gl.mpay_account_related_account_type,
            "related_account_id": gl.mpay_account_related_account_id
        }
        data = {
            "id": gl.mpay_account_id_shoukuan
        }
        print "请求参数是：" + json.dumps(data)
        r = requests.get(
            gl.url + ":7145/api/" + gl.api_version + "/mpay/account/query?param=" + urllib.quote(json.dumps(data)),
            headers=headers)
        print gl.url + ":7145/api/" + gl.api_version + "/mpay/account/query?param=" + urllib.quote(json.dumps(data))
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])

    def test_007_create_bill(self):
        """POST /api/v1.0/mpay/bill
        创建账单"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = {
            "channel": "MQ_BALANCE",  # 目前支持 阿里：MQ_ALI_QRCODE，微信：MQ_NATIVE，余额消费：MQ_BALANCE
            "amount": 1,
            "currency": "CNY",
            "title": "测试 Bill Pay",
            "timeout": 600,
            "return_url": "https://meiqia.com",
            "type": "PAY",
            "to_account_id": gl.mpay_account_id_shoukuan,  # 收款方必须是当前租户，而且关联账户类型必须是美洽（MQ）
            "from_customer_id": gl.mpay_customer_id,
            # from_customer_id此处传的是租户下CRM_TENANT_ACCOUNT类型的客户id，如果path类型为TENANT_TO_MQ，这里需要用CRM_TENANT类型的customer
            "path": gl.mpay_bill_path
        }
        print "请求参数是：" + json.dumps(data)
        r = requests.post(
            gl.url + ":7145/api/" + gl.api_version + "/mpay/bill",
            data=json.dumps(data), headers=headers)
        print gl.url + ":7145/api/" + gl.api_version + "/mpay/bill"
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        gl.mpay_bill_id = result["body"]["bill"]["id"]

    def test_008_query_bill_info(self):
        """GET  /api/v1.0/mpay/bill/query
        账单查询"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = {
            "id": gl.mpay_bill_id,  # 账单ID
            "customer_id": "",  # 关联的客户ID
            # "succeeded_after": "",         #起始时间
            # "succeeded_before": "",        #结束时间
            "channel": "",  # 渠道
            "status": "",  # 账单状态
            "channel_bill_id": "",  # 渠道交易号
            "channel_order_id": "",  # 渠道商户订单号
            "related_bill_id": "",  # 关联账单号
            "beecloud_bill_id": "",  # beecloud 账单唯一标识ID
            "type": "PAY",  # 账单类型
            "to_account_id": gl.mpay_account_id_shoukuan,  # 收款账户ID
            "from_account_id": gl.mpay_bill_account_id_mq_type  # 付款账户ID
        }
        data = {
            "id": gl.mpay_bill_id,
            "type": "PAY",
            "to_account_id": gl.mpay_account_id_shoukuan
        }
        print "请求参数是：" + json.dumps(data)
        r = requests.get(
            gl.url + ":7145/api/" + gl.api_version + "/mpay/bill/query?param=" + urllib.quote(json.dumps(data)),
            data=json.dumps(data), headers=headers)
        print gl.url + ":7145/api/" + gl.api_version + "/mpay/bill"
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])


gl.suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMPayAll))
