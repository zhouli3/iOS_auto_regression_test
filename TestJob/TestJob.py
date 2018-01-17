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

cron_id = ""
job_id = ""
script = "var time = import(\"time\");var fmt = import(\"fmt\");sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));println(\"test\")"

class TestJob(unittest.TestCase):
    """测试job http doc（定时任务http文档）"""

    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."

    def test_1_create_cron(self):
        """Test POST /api/v1.0/cron-job/cron"""
        print uuid.uuid1()
        data = {
            "title": "测试定时任务" + str(uuid.uuid1()),
            "comment": "每分钟执行一次的定时任务",
            "schedule": "*/1 * * * *",
            "script": "var time = import(\"time\");var fmt = import(\"fmt\");sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));println(\"test\")"
        }
        headers = {
            'X-Token': gl.access_token,
            'Content-Type': 'application/json'
        }
        print "传入参数：" + json.dumps(data)
        r = requests.post(gl.url + ':7146/api/v1.0/cron-job/cron', data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["cron_id"])
        print result["body"]["cron_id"]
        gl.cron_id = result["body"]["cron_id"]

    def test_2_get_cronById(self):
        """Test GET /api/v1.0/cron-job/cron/:cron_id"""
        headers = {
            'X-Token': gl.access_token
        }
        r = requests.get(gl.url + ":7146/api/v1.0/cron-job/cron/" + gl.cron_id, headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["cron_id"])

    def test_3_get_cron_list(self):
        """Test GET /api/v1.0/cron-job/crons"""
        headers = {
            'X-Token': gl.access_token
        }
        r = requests.get(gl.url + ":7146/api/v1.0/cron-job/crons", headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["cron_id"])

    def test_4_start_cron(self):
        """Test POST /api/v1.0/cron-job/cron/:cron_id/start"""
        headers = {
            'X-Token': gl.access_token
        }
        r = requests.post(gl.url + ":7146/api/v1.0/cron-job/cron/" + gl.cron_id + "/start", headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["cron_id"])

    def test_5_get_job_list(self):
        """查询定时任务创建job前 先休眠2分钟 创建几条job数据"""
        time.sleep(60)
        """Test GET /api/v1.0/cron-job/jobs/cron/:cron_id"""
        headers = {
            'X-Token': gl.access_token
        }
        r = requests.get(gl.url + ":7146/api/v1.0/cron-job/jobs/cron/" + gl.cron_id, headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["jobs"][0])
        gl.job_id = result["body"]["jobs"][0]["job_id"]

    def test_6_get_logs_list(self):
        """Test GET /api/v1.0/cron-job/logs/cron/:cron_id/job/:job_id"""
        headers = {
            'X-Token': gl.access_token
        }
        r = requests.get(gl.url + ":7146/api/v1.0/cron-job/logs/cron/" + gl.cron_id + "/job/" + gl.job_id, headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["logs"])

    def test_7_stop_cron(self):
        """Test POST /api/v1.0/cron-job/cron/:cron_id/stop"""
        headers = {
            'X-Token': gl.access_token
        }
        r = requests.post(gl.url + ":7146/api/v1.0/cron-job/cron/" + gl.cron_id + "/stop", headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"][""])

    def test_8_delete_cron(self):
        """Test DELETE /api/v1.0/cron-job/cron/:cron_id"""
        headers = {
            'X-Token': gl.access_token
        }
        r = requests.delete(gl.url + ":7146/api/v1.0/cron-job/cron/" + gl.cron_id, headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["cron_id"])

gl.suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestJob))