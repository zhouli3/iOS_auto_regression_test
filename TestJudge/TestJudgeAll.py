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
requests.packages.urllib3.disable_warnings()


class TestJudgeAll(unittest.TestCase):
    """def test_1_create_acl_profile(self):
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type
        }
        data = {
            "ent_id": "AQACd5VVkc7RCAAA6vXOmrnF6BSVKwAA",
            "profile_id": "",
            "profile_name": "testprofile-str(time.strftime('%Y/%m/%d%H%M%S', time.localtime(time.time())))",
            "oLAs": [],
            "fLAs": []
        }
        r = requests.post(
            "http://10.100.250.6:7111/acl_admin/profile",
            data=json.dumps(data), headers=headers, verify=False)
        print r, r.text
        result = json.loads(r.text)
        gl.profile_id = result["profile_id"]"""

    def test_2_get_acl_profile_by_profile_id(self):
        headers = {
            'x-token': gl.access_token_online,
            'content-type': gl.content_type
        }
        r = requests.get(
            "http://10.100.250.6:7111/acl_admin/profile/" + gl.profile_id,
            headers=headers, verify=False)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["profile_id"], gl.profile_id)


gl.suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestJudgeAll))
