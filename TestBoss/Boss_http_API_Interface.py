# -*- coding: utf-8 -*-
import unittest
import json
import requests

from GlobalVariables import gl

class Boss_http_APT_Interface(unittest.TestCase):
    """Boss系统HTTP API接口测试"""
    def test_boss_01_login(self):
        """登录"""
        headers = {
            # 'x-token': gl.X_Meiqia_BOSS_Token,
            'content-type': gl.content_type,
            'accept-language': 'zh-CN,zh;q=0.8',
        }
        data = {"name": "default_boss_admin","password":"admin54321"}
        r = requests.post(
            gl.url_test + ":7133/api/" + gl.api_version + "/boss/account/login",
            data=json.dumps(data), headers=headers)
        print gl.url_test + ":7133/api/" + gl.api_version + "/boss/account/login"
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        gl.X_Meiqia_BOSS_Token = result["body"]["token"]

    def test_boss_02_readAccount(self):
        """查询单个账户"""
        headers = {
            'X-Meiqia-BOSS-Token': gl.X_Meiqia_BOSS_Token,
            'content-type': gl.content_type,
            'accept-language': 'zh-CN,zh;q=0.8',
        }
        r = requests.get(
            gl.url_test + ":7133/api/" + gl.api_version + "/boss/account/"+gl.account_id,
             headers=headers)
        print gl.url_test + ":7133/api/" + gl.api_version + "/boss/account/"+gl.account_id
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)

    def test_boss_03_readAllAccount(self):
        """查询所有账户"""
        headers = {
            'X-Meiqia-BOSS-Token': gl.X_Meiqia_BOSS_Token,
            'content-type': gl.content_type,
            'accept-language': 'zh-CN,zh;q=0.8',
        }
        r = requests.get(
            gl.url_test + ":7133/api/" + gl.api_version + "/boss/account/list?para={"+"\"page_num\""+":"+str(gl.page_num)+","+"\"size\""+":"+str(gl.size)+"}",
            headers=headers)
        print gl.url_test + ":7133/api/" + gl.api_version + "/boss/account/list?para={"+"\"page_num\""+":"+str(gl.page_num)+","+"\"size\""+":"+str(gl.size)+"}"
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)

    def test_boss_04_buildAPP(self):
        """创建APP"""
        headers = {
            'X-Meiqia-BOSS-Token' : gl.X_Meiqia_BOSS_Token,
            'content-type' : gl.content_type,
            'accept-language' : 'zh-CN,zh;q=0.8',
        }
        data  = {"name" : "testApp"}
        url = gl.url_test+":7133/api/"+gl.api_version+"/boss/app"
        r = requests.post(url,data=json.dumps(data), headers=headers)
        print url
        print r, r.text
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()["code"],0)
        result = json.loads(r.text)
        gl.app_id = result["body"]["id"]
        print result["body"]["id"]

    def test_boss_04_updateAPP(self):
        """更新APP"""
        headers = {
            'X-Meiqia-BOSS-Token': gl.X_Meiqia_BOSS_Token,
            'content-type': gl.content_type,
            'accept-language': 'zh-CN,zh;q=0.8',
        }
        data = {"name": "testApp1"}
        url = gl.url_test+":7133/api/"+gl.api_version+"/boss/app/"+str(gl.app_id)
        r = requests.put(url, data=json.dumps(data), headers=headers)
        print url
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)

    def test_boss_05_deleteAPP(self):
        """删除APP"""
        headers = {
            'X-Meiqia-BOSS-Token': gl.X_Meiqia_BOSS_Token,
            'content-type': gl.content_type,
            'accept-language': 'zh-CN,zh;q=0.8',
        }
        url = gl.url_test+":7133/api/"+gl.api_version+"/boss/app/"+str(gl.app_id)
        r = requests.delete(url, headers = headers)
        print url
        print r, r.text
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()["code"],0)
        result = json.loads(r.text)

    def test_boss_06_selectAPP(self):
        """查询APP"""
        headers = {
            'X-Meiqia-BOSS-Token': gl.X_Meiqia_BOSS_Token,
            'content-type': gl.content_type,
            'accept-language': 'zh-CN,zh;q=0.8',
        }
        url = gl.url_test+":7133/api/"+gl.api_version+"/boss/app/"+str(gl.app_id)
        r = requests.get(url, headers=headers)
        print url
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)

    def test_boss_07_selectAllAPP(self):
        """查询APP列表"""
        headers = {
            'X-Meiqia-BOSS-Token': gl.X_Meiqia_BOSS_Token,
            'content-type': gl.content_type,
            'accept-language': 'zh-CN,zh;q=0.8',
        }
        url = gl.url_test + ":7133/api/" + gl.api_version + "/boss/app/list"
        r = requests.get(url, headers=headers)
        print url
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)

    def test_boss_08_bulidAction(self):
        """bulid Action"""
        headers = {
            'X-Meiqia-BOSS-Token': gl.X_Meiqia_BOSS_Token,
            'content-type': gl.content_type,
            'accept-language': 'zh-CN,zh;q=0.8',
        }
        data = {"code":gl.code,"type":1,"app_id":3,"url":"http://10.102.1.224:5000/boss/tenant/info","mode":100,"param_names":["tenant_id"]}
        url = gl.url_test + ":7133/api/" + gl.api_version + "/boss/action"
        r = requests.post(url,data = json.dumps(data), headers=headers)
        print url
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        gl.action_code = result["body"]["code"]

    def test_boss_09_transAction(self):
        """调用action"""
        headers = {
            'X-Meiqia-BOSS-Token': gl.X_Meiqia_BOSS_Token,
            'content-type': gl.content_type,
            'accept-language': 'zh-CN,zh;q=0.8',
        }
        data = {"param_map":{"tenant_id":"5"}}#待优化
        url = gl.url_test + ":7133/api/" + gl.api_version + "/boss/action/404573181/do"
        r = requests.post(url, data=json.dumps(data), headers=headers)
        print url
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)

    def  test_boss_10_updateAction(self):
        """update Action"""
        headers = {
            'X-Meiqia-BOSS-Token': gl.X_Meiqia_BOSS_Token,
            'content-type': gl.content_type,
            'accept-language': 'zh-CN,zh;q=0.8',
        }
        data = {"code":gl.action_code,"type":1,"app_id":5,"url":"http://10.102.1.224:5000/boss/tenant/info","mode":100,"param_names":["tenant_id"]}
        url = gl.url_test + ":7133/api/" + gl.api_version + "/boss/action/"+str(gl.action_code)
        r = requests.put(url, data=json.dumps(data), headers=headers)
        print url
        print r, r.text
        print json.dumps(data)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        #gl.action_code = result["body"]["code"]

    def test_boss_11_selectAction(self):
        """select action"""
        headers = {
            'X-Meiqia-BOSS-Token': gl.X_Meiqia_BOSS_Token,
            'content-type': gl.content_type,
            'accept-language': 'zh-CN,zh;q=0.8',
        }
        url = gl.url_test + ":7133/api/" + gl.api_version + "/boss/action/"+str(gl.action_code)
        r = requests.get(url, headers=headers)
        print url
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)

    def test_boss_12_selectAllAction(self):
        """select all action"""
        headers = {
            'X-Meiqia-BOSS-Token': gl.X_Meiqia_BOSS_Token,
            'content-type': gl.content_type,
            'accept-language': 'zh-CN,zh;q=0.8',
        }
        url = gl.url_test + ":7133/api/" + gl.api_version + "/boss/action/list?para={\"type\":1,\"app_id\":3, \"mode\":100}"
        r = requests.get(url, headers=headers)
        print url
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)

    def test_boss_13_deleteAction(self):
        """delete action"""
        headers = {
            'X-Meiqia-BOSS-Token': gl.X_Meiqia_BOSS_Token,
            'content-type': gl.content_type,
            'accept-language': 'zh-CN,zh;q=0.8',
        }
        url = gl.url_test+":7133/api/"+gl.api_version+"/boss/action/"+str(gl.action_code)
        r = requests.delete(url,headers = headers)
        print url
        print r, r.text
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()["code"],0)
        result = json.loads(r.text)
        gl.action_code = result['body']['code']

    def test_boss_14_createOrder(self):
        """create order"""
        headers = {
            'X-Meiqia-BOSS-Token': gl.X_Meiqia_BOSS_Token,
            'content-type': gl.content_type,
            'accept-language': 'zh-CN,zh;q=0.8',
        }
        data = {"type":1,"customer":16,"customer_tenant_id":"6","cash_decrease":6}
        url = gl.url_test+":7133/api/"+gl.api_version+"/boss/order"
        r = requests.post(url,data = json.dumps(data), headers = headers)
        print '这是url:'+url
        print r, r.text
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()["code"],0)

    def test_boss_15_payOrder(self):
        """pay order"""
        headers = {
            'X-Meiqia-BOSS-Token': gl.X_Meiqia_BOSS_Token,
            'content-type': gl.content_type,
            'accept-language': 'zh-CN,zh;q=0.8',
        }
        url = gl.url_test+":7133/api/"+gl.api_version+"/boss/order/"+str(gl.order_id)+"/pay"
        r = requests.put(url,headers = headers)
        print url
        print r, r.text
        print r
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()["code"],0)
        result = json.loads(r.text)
        gl.order_id = result["body"]["id"]

    def test_boss_16_finalOrder(self):
        """final order"""
        headers = {
            'X-Meiqia-BOSS-Token': gl.X_Meiqia_BOSS_Token,
            'content-type': gl.content_type,
            'accept-language': 'zh-CN,zh;q=0.8',
        }
        url = gl.url_test+":7133/api/"+gl.api_version+"/boss/order/"+str(gl.order_id)+"/done"
        r = requests.put(url, headers = headers)
        print r
        print r, r.text
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['code'],0)
        result = json.loads(r.text)
        gl.order_id = result["body"]["id"]

    def test_boss_17_directCreateOrder(self):
        """direct create order"""
        headers = {
            'X-Meiqia-BOSS-Token': gl.X_Meiqia_BOSS_Token,
            'content-type': gl.content_type,
            'accept-language': 'zh-CN,zh;q=0.8',
        }
        data = {"type":2,"customer":1,"customer_tenant_id":gl.customer_tenant_id,"suite_id":1}
        url = gl.url_test+":7133/api/"+gl.api_version+"/boss/order/direct"
        r = requests.put(url,data = json.dumps(data),headers = headers)
        print r
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 0)
        result = json.loads(r.text)

    def test_boss_18_selectOrder(self):
        """select order"""
        headers = {
            'X-Meiqia-BOSS-Token': gl.X_Meiqia_BOSS_Token,
            'content-type': gl.content_type,
            'accept-language': 'zh-CN,zh;q=0.8',
        }
        url = gl.url_test + ":7133/api/" + gl.api_version + "/boss/order/"+str(gl.order_id)
        r = requests.get(url, headers=headers)
        print r
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 0)
        result = json.loads(r.text)
        gl.order_id = result["body"]["id"]

    def test_boss_19_selectListOrder(self):
        """select list order"""
        headers = {
            'X-Meiqia-BOSS-Token': gl.X_Meiqia_BOSS_Token,
            'content-type': gl.content_type,
            'accept-language': 'zh-CN,zh;q=0.8',
        }
        #customer   suite_id  status   type
        url = gl.url_test + ":7133/api/" + gl.api_version + "/boss/order/list?para={\"type\":1}"
        r = requests.get(url, headers=headers)
        print r
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 0)
        result = json.loads(r.text)

    def test_boss_20_createSuite(self):
        """create suite"""
        headers = {
            'X-Meiqia-BOSS-Token': gl.X_Meiqia_BOSS_Token,
            'content-type': gl.content_type,
            'accept-language': 'zh-CN,zh;q=0.8',
        }
        data = {"name":"IAMNAME","action_code":2200,"tag":"套餐１","param_value":{"tenant_id":gl.customer_tenant_id}}
        url = gl.url_test + ":7133/api/" + gl.api_version + "/boss/suite"
        r = requests.post(url, data =json.dumps(data), headers=headers)
        print r
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 0)
        result = json.loads(r.text)

    def test_boss_21_tranceSuite(self):
        """trance suite"""
        headers = {
            'X-Meiqia-BOSS-Token': gl.X_Meiqia_BOSS_Token,
            'content-type': gl.content_type,
            'accept-language': 'zh-CN,zh;q=0.8',
        }
        data = {"name": "IAMNAME", "action_code": 2200, "tag": "套餐１",
                "param_value": {"tenant_id": gl.customer_tenant_id}}
        url = gl.url_test + ":7133/api/" + gl.api_version + "/boss/suite"
        r = requests.post(url, data=json.dumps(data), headers=headers)
        print r
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 0)
        result = json.loads(r.text)

    def test_boss_22_selectSuite(self):
        """select suite"""
        headers = {
            'X-Meiqia-BOSS-Token': gl.X_Meiqia_BOSS_Token,
            'content-type': gl.content_type,
            'accept-language': 'zh-CN,zh;q=0.8',
        }
        url = gl.url_test + ":7133/api/" + gl.api_version + "/boss/suite/"+str(gl.suite_id)
        r = requests.get(url, headers=headers)
        print r
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 0)
        result = json.loads(r.text)

    def test_boss_23_selectListSuite(self):
        """select list suite"""
        headers = {
            'X-Meiqia-BOSS-Token': gl.X_Meiqia_BOSS_Token,
            'content-type': gl.content_type,
            'accept-language': 'zh-CN,zh;q=0.8',
        }
        url = gl.url_test + ":7133/api/" + gl.api_version + "/boss/suite/list?para={}"
        r = requests.get(url, headers=headers)
        print r
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 0)
        result = json.loads(r.text)

    def test_boss_24_selectAllSuite(self):
        """select all suite"""
        headers = {
            'X-Meiqia-BOSS-Token': gl.X_Meiqia_BOSS_Token,
            'content-type': gl.content_type,
            'accept-language': 'zh-CN,zh;q=0.8',
        }
        url = gl.url_test + ":7133/api/" + gl.api_version + "/boss/suite/all?para={}"
        r = requests.get(url, headers=headers)
        print r
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 0)
        result = json.loads(r.text)

    def test_boss_25_selectLoginHistory(self):
        """select login history"""
        headers = {
            'X-Meiqia-BOSS-Token': gl.X_Meiqia_BOSS_Token,
            'content-type': gl.content_type,
            'accept-language': 'zh-CN,zh;q=0.8',
        }
        url = gl.url_test + ":7133/api/" + gl.api_version + "/boss/history/login?para={}"
        r = requests.get(url, headers=headers)
        print r
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 0)
        result = json.loads(r.text)

    def test_boss_26_selectOperationHistory(self):
        """select operation history"""
        headers = {
            'X-Meiqia-BOSS-Token': gl.X_Meiqia_BOSS_Token,
            'content-type': gl.content_type,
            'accept-language': 'zh-CN,zh;q=0.8',
        }
        url = gl.url_test + ":7133/api/" + gl.api_version + "/boss/history/action?para={\"tenant_id\":"+"\"str(gl.customer_tenant_id)\""+"}"
        r = requests.get(url, headers=headers)
        print r
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'], 0)
        result = json.loads(r.text)