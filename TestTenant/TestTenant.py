# -*- coding: utf-8 -*-
import unittest
import json
import uuid
import requests
from GlobalVariables import gl

"""解决'ascii' codec can't decode byte 0xe6"""
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class TestTenant(unittest.TestCase):
    """测试Tenant流程"""

    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."

    def test_1_create_tenant_or_org(self):
        """Test POST /account/org"""
        print uuid.uuid1()
        data = {
            "name": "测试企业123",
            "primaryContact": {
                "name": "123",
                "phone": "12345678999",
                "email": "test@qq.com"
            },
            "phone": "12345678999",
            "fax": "0592-88889999",
            "address": {
                "street": "北京市海淀",
                "city": "beijing",
                "state": "wanggujin",
                "post_code": "200",
                "country": "China",
                "country_code": "010"
            }
        }
        headers = {
            'authorization': gl.account_token,
            'Content-Type': 'application/json'
        }
        print "传入参数：" + json.dumps(data)
        r = requests.post(gl.url + ':7121/account/org', data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["creator_account_id"])
        gl.tenant_id = result["body"]["id"]

    def test_2_tenant_sign(self):
        """Test POST /account/signin"""
        data = "{\"source\":\"web\",\"tenant_id\":\"" + gl.tenant_id + "\"}"
        headers = {
            'Authorization': gl.account_token
        }
        print "传入参数：" + data
        r = requests.post(gl.url + ":7121/account/signin", data=data, headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["access_token"])
        gl.access_token = result["body"]["access_token"]
        gl.refresh_token = result["body"]["refresh_token"]
        print result["body"]["access_token"]

    def test_3_tenant_org_update(self):
        """Test POST /tenant/org/update"""
        data = {
            "id": gl.tenant_id,
            "org": {
                "id": gl.tenant_id,
                "name": "测试" + str(uuid.uuid1()),
                "primaryContact": {
                    "name": "测试",
                    "phone": "12345678999",
                    "email": "test@qq.com"
                },
                "phone": "12345678999",
                "fax": "0592-88887777",
                "address": {
                    "street": "ddddd",
                    "city": "beijing",
                    "state": "wanggujin",
                    "post_code": "200",
                    "country": "China",
                    "country_code": "010"
                },
                "creatorAccountId": "AQAC12hSbKqGKQAAFmS7xyHg4xQ0GwAA",
                "lastUpdatorAccountId": "AQAC12hSbKqGKQAAFmS7xyHg4xQ0GwAA"
            }
        }
        headers = {
            'X-Token': gl.access_token
        }
        print "传入参数：" + json.dumps(data)
        r = requests.put(gl.url + ':7121/tenant/org/update', data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["id"])

    def test_4_get_tenant_org(self):
        """Test get /tenant/org/:id"""
        headers = {
            'X-Token': gl.access_token
        }
        print "传入参数：" + gl.tenant_id
        r = requests.get(gl.url + ':7121/tenant/org/' + gl.tenant_id, headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["id"])

    # 搜索含有该name的企业
    def test_5_get_account_orgs(self):
        """Test get /account/orgs?name=xxx"""
        headers = {
            'Authorization': gl.account_token
        }
        r = requests.get(gl.url + ':7121/account/orgs?name=SGSoft测试', headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["orgs"])

    def test_6_get_tenant_relations(self):
        """Test get /tenant/relations"""
        headers = {
            'X-Token': gl.access_token
        }
        r = requests.get(gl.url + ':7121/tenant/relations', headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["items"])

    def test_7_get_account_relations(self):
        """Test get /account/relations"""
        headers = {
            'Authorization': gl.account_token
        }
        r = requests.get(gl.url + ':7121/account/relations', headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["items"])

    def test_8_tenant_refresh_token(self):
        """Test put /tenant/refresh_token"""
        headers = {
            'X-Token': gl.access_token
        }
        data = '{"refresh_token":"' + gl.refresh_token + '"}'
        print "传入参数：" + data
        r = requests.put(gl.url + ':7121/tenant/refresh_token', data=data, headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["access_token"])
        gl.access_token = result["body"]["access_token"]
        gl.refresh_token = result["body"]["refresh_token"]

    def test_9_1personal_token(self):
        """Test POST /personal_token"""
        headers = {
            'X-Token': gl.access_token
        }
        data = '{"name":"zhouli"}'
        print "传入参数：" + data
        r = requests.post(gl.url + ':7121/personal_token', data=data, headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["personal_token"])

        """Test GET /personal_token/list"""
        headers = {
            'X-Token': gl.access_token
        }
        r = requests.get(gl.url + ':7121/personal_token/list', headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["personal_tokens"])

        """Test DELETE /personal_token"""
        headers = {
            'X-Token': gl.access_token
        }
        data = '{"name":"zhouli"}'
        print "传入参数：" + data
        r = requests.delete(gl.url + ':7121/personal_token', data=data, headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)

    def test_9_enterprise_info(self):
        """Test get /enterprise_info/search_infoes"""
        headers = {
            'X-Token': gl.access_token
        }
        r = requests.get(gl.url + ':7121/enterprise_info/search_infoes', headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)

    def test_9_tenant2_user_delete(self):
        """Test delete /tenant/user/:userId"""
        headers = {
            'X-Token': gl.access_token
        }
        r = requests.delete(gl.url + ':7121/tenant/user/AQAGsSX2s7BCDQAAnp3gvgP_9BQDAAAA', headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)

    def test_9_tenant_signout(self):
        """Test post /tenant/signout"""
        headers = {
            'X-Token': gl.access_token
        }
        data = '{"source":"web"}'
        r = requests.post(gl.url + ':7121/tenant/signout', data=data, headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)

gl.suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestTenant))
