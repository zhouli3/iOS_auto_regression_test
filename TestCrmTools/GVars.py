# -*- coding: utf-8 -*-

import unittest
import json


suites = unittest.TestSuite()

url = "http://10.102.2.5"

access_token = "ASkAACgQDFp4AEFRQUNrNUh4RklaMURBQUEteUJiUlRLLTlCVF9CQUFBQVFBQ2s1SHhGSVoxREFBQUE0OEV5RFM3OUJTc0F3QUEC9_7gVIApE_88GcE728NNyNvI3ewPK1QrI2oqGUqxpVVlMeu13NBxmn3-Ok1eA8sBLtbufQ4Wh9extqVI8Jkc"

tenant_name = "meqia"  # test企业test   meiqia

meta_name = "Leads"

meta_column_name = "guanlianhetong"

# header
content_type = "application/json"

layout_json_temp = json.load(open("./layout1.64_test_ent.json"))

