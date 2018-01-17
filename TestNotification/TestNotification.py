# -*- coding: utf-8 -*-
import unittest
import json
import uuid
import requests
from GlobalVariables import gl

"""解决'ascii' codec can't decode byte 0xe6"""
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')

# 通知通用变量定义
notification_id = "AQACk5HxFIbqCwAAn1t7WBFDChUaBAAA"  # 通知ID
notice_type = 0  # 通知类型(0=提醒, 1=待办, 2=通告)
template_id = "AQACk5HxFIYFDAAAInFgo598_xT6AgAA"

class TestNotification(unittest.TestCase):
    """测试 通知服务http"""

    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."

    def test_1_create_notice(self):
        """Test POST /api/v1.0/notification-gateway/notice"""
        kv = "{\"user_name\":\"周丽\",\"user_id\":\"AQACk5HxFIZ1DAAAn_hVhmAL9RS7DAAA\",\"lead_name\":\"测试通知-"+ str(uuid.uuid1())+"\",\"avatar_url\":\"nil\",\"avatar_user\":\"AQACk5HxFIZ1DAAAn_hVhmAL9RS7DAAA\",\"lead_id\":\"\"}"
        data = {
            "user_id": "AQACk5HxFIZ1DAAAn_hVhmAL9RS7DAAA",
            "template_id": template_id,
            "kv": kv,
            "notice_type": notice_type
        }
        headers = {
            'X-Token': gl.access_token,
            'Content-Type': 'application/json'
        }
        print "传入参数：" + json.dumps(data)
        r = requests.post(gl.url + ':7522/api/v1.0/notification-gateway/notice', data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["id"])
        print result["body"]["id"]
        notification_id = result["body"]["id"]

    def test_2_get_noticeById(self):
        """Test GET /api/v1.0/notification-gateway/notices/{id}"""
        headers = {
            'X-Token': gl.access_token
        }
        print "创建的通知ID："+notification_id
        r = requests.get(gl.url + ":7522/api/v1.0/notification-gateway/notices/" + notification_id, headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["notification"]["content"])

    def test_3_get_noticelist_byUserId(self):
        """Test GET /api/v1.0/notification-gateway/notices?notice_type=&tenant_type=&limit=&offset=&count_flag="""
        headers = {
            'X-Token': gl.access_token
        }
        r = requests.get(gl.url + ":7522/api/v1.0/notification-gateway/notices?notice_type=0&tenant_type=0&limit=10&offset=0&count_flag=1", headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["notifications"][0]["id"])

    def test_4_get_unreadCount_byNoticeType(self):
        """Test GET /api/v1.0/notification-gateway/notices/count?notice_type=0"""
        headers = {
            'X-Token': gl.access_token
        }
        r = requests.get(gl.url + ":7522/api/v1.0/notification-gateway/notices/count?notice_type="+str(notice_type), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        print "当前租户未读通知数量："+str(result["body"]["current_count"])
        self.assertIsNotNone(result["body"]["current_count"])
        self.assertIsNotNone(result["body"]["related_count"])

    def test_5_get_notice_unreadCount_all(self):
        """Test GET /api/v1.0/notification-gateway/notices/count-all"""
        headers = {
            'X-Token': gl.access_token
        }
        r = requests.get(gl.url + ":7522/api/v1.0/notification-gateway/notices/count-all", headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["remind_current_count"])
        self.assertIsNotNone(result["body"]["remind_related_count"])

    def test_6_update_noticeRead_byId(self):
        """Test PUT /api/v1.0/notification-gateway/mark/{id}"""
        headers = {
            'X-Token': gl.access_token
        }
        r = requests.put(gl.url + ":7522/api/v1.0/notification-gateway/mark/"+notification_id, headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertEqual(result["body"]["read_status"], 1)

    def test_7_update_notice_read(self):
        """Test PUT /api/v1.0/notification-gateway/mark"""
        headers = {
            'X-Token': gl.access_token
        }
        data = {
            "notice_type": notice_type,
            "tenant_type": 0
        }
        r = requests.put(gl.url + ":7522/api/v1.0/notification-gateway/mark", data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)


    #@unittest.skip("I don't want to run this case.")
    def test_8_create_notices(self):
        """Test POST /api/v1.0/notifications/notices"""
        headers = {
            'X-Token': gl.access_token
        }
        kv = "{\"user_name\":\"周丽\",\"user_id\":\"AQACk5HxFIZ1DAAAn_hVhmAL9RS7DAAA\",\"lead_name\":\"测试群发通知-" + str(
            uuid.uuid1()) + "\",\"avatar_url\":\"nil\",\"avatar_user\":\"AQACk5HxFIZ1DAAAn_hVhmAL9RS7DAAA\",\"lead_id\":\"\"}"
        receivers = [
            {"user_id": "AQACk5HxFIZ1DAAAn_hVhmAL9RS7DAAA","kv":kv},
            {"user_id": "AQACk5HxFIZ1DAAA-yBbRTK-9BT_BAAA","kv":kv},
            {"user_id": "AQACk5HxFIZ1DAAAZ_EayDS79BStAwAA","kv":kv}
        ]
        data = {
            "receivers": receivers,
            "template_id": template_id,
            "notice_type": notice_type
        }
        r = requests.post(gl.url + ":7522/api/v1.0/notifications/notices", data=json.dumps(data),  headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["task_id"])

gl.suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestNotification))