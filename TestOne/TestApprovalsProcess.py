# -*- coding: utf-8 -*-
import unittest
import json
import requests
import uuid
import random
import time
from GlobalVariables import gl

"""解决'ascii' codec can't decode byte 0xe6"""
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class TestApprovalsProcess(unittest.TestCase):
    """测试 审批过程 相关接口"""

    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."

    def test_001_get_approvaling_fields_by_approval_name(self):
        """POST /api/:ver/:org-name/service/approvals/fields/:object-name/:object-id
        获取指定Record有那些字段在审批"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        approval_name = gl.object_approvals_template_name
        print "请求参数approval_name：" + approval_name + "，id=AQACk5HxFIZbAwAA7z1gvcZY7hTJAAAA"
        # 此处的:object-id为审批列表中的某条data 的id
        r = requests.get(
            gl.url + ":7010/api/" + gl.api_version + "/" + gl.tenant_name + "/service/approvals/fields/" + approval_name + "/AQACk5HxFIZbAwAA7z1gvcZY7hTJAAAA",
            headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["FieldList"])

    def test_002_get_can_create_approvals_template(self):
        """POST /api/:ver/:org-name/service/approvals/get-available-templates/:object-name
        获取创建可用的审批模板"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        approval_name = gl.object_approvals_template_name
        data = {"Type": "新开", "InvoiceType": "普通发票", "Approvalstatus": "未审批", "InvoiceStatus": "未开出", "PostTime": "未寄出",
                "PostCode": None, "RechargeID": "AQACk5HxFIZiAwAAn3SBYaJo8RREAQAA",
                "PayID": "AQACk5HxFIZiAwAAuz0oog1O8RS1AAAA", "InvoiceTitle": "1亲为の3如",
                "PostAddress": {"country": "中国", "state": "北京市", "city": "海淀区", "street": "去哇所谓的"},
                "ContactID": "AQACk5HxFIb0DQAAXxB5GGnV6xRDCQAA", "TaxNumber": None,
                "BussLicense": {"country": None, "state": None, "city": None, "street": None}, "Bank": None,
                "BankAccount": None,
                "Proofs": "https://tri-file-test.meiqia.com/v1/folder/24b1518a-ad6e-4697-a9d8-933cdd26c569"}
        print "请求参数：" + json.dumps(data)
        print approval_name
        r = requests.post(
            gl.url + ":7010/api/" + gl.api_version + "/" + gl.tenant_name + "/service/approvals/get-available-templates/" + approval_name,
            data=json.dumps(data), headers=headers)
        print gl.url + ":7010/api/" + gl.api_version + "/" + gl.tenant_name + "/service/approvals/get-available-templates/" + approval_name
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])

    def test_003_get_can_update_approval_template(self):
        """PUT /api/:ver/:org-name/service/approvals/get-available-templates/:object-name/:object-id
        获取修改可用的审批模板"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        approval_name = gl.object_approvals_template_name
        data = {"name": "shangjitest123", "AccountID": "3c5938c9917ca43b73cad4f5453623b3",
                "Amount": {"symbol": "CNY", "value": 10000000}, "CloseDate": "2017-10-11T10:28:45Z", "Stage1": "初步意向",
                "Probability1": "20%", "Stage2": "14天（30天）保持跟进", "Probability2": "20%", "Phone": None,
                "IndustryCategory": None, "Industry": None, "OtherService": None, "AffiliatedDepartment": "北京直销",
                "Competitor": None, "CompetitorPrice": {"symbol": None, "value": None}, "Disagreements": None,
                "Demands": None, "Excitements": None, "FacilitatorType": None, "FacilitatorDiscount": 0,
                "FacilitatorBusiness": None, "FacilitatorDoubts": None, "LosingStage": None, "LosingReason": None,
                "LosingDescription": None, "StageUpdatedAt": "2017-10-11T10:28:45Z", "Description": None}
        print "请求参数：" + json.dumps(data)
        print approval_name
        print gl.url + ":7010/api/" + gl.api_version + "/" + gl.tenant_name + "/service/approvals/get-available-templates/" + approval_name + "/" + gl.object_date_id
        r = requests.put(
            gl.url + ":7010/api/" + gl.api_version + "/" + gl.tenant_name + "/service/approvals/get-available-templates/" + approval_name + "/" + gl.object_date_id,
            data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])

    def test_004_01_create_an_approval(self):
        """POST /api/:ver/:org-name/service/approvals/template/:template-id/run
        创建审批"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = {"objects": [
            {"Name": "dsafsdfasdfasd", "Description": "fasdfasdfsadfsadf", "RelationType": "Opportunity",
             "OwnerId": "01bc54a795e79def738a5e1fae0ec229", "CCIds": [],
             "Record": {"record_type": "main", "name": "cvxcvxcvzxcvx", "AccountID": "3c5938c9917ca43b73cad4f5453623b3",
                        "Amount": {"symbol": "CNY", "value": 10000000}, "CloseDate": "2017-10-21T00:43:44Z",
                        "Stage1": "初步意向", "Probability1": "20%", "Stage2": "14天（30天）保持跟进", "Probability2": "20%",
                        "Phone": None, "IndustryCategory": None, "Industry": None, "FacilitatorDiscount": 0,
                        "OtherService": None, "AffiliatedDepartment": "北京直销", "Description": None,
                        "FacilitatorType": None, "Competitor": None, "CompetitorPrice": {"symbol": None, "value": None},
                        "Disagreements": None, "Demands": None, "Excitements": None, "FacilitatorBusiness": None,
                        "FacilitatorDoubts": None, "LosingStage": None, "LosingReason": None, "LosingDescription": None,
                        "StageUpdatedAt": "2017-10-21T00:43:44Z", "Test": None, "Path": None},
             "PointVoters": [{"PointId": 1, "UserId": "01bc54a795e79def738a5e1fae0ec222"},
                             {"PointId": 3, "UserId": "AQACd5VVkc7uCAAA3Ym_V7TR2xRW2wEA"}], "GroupVoters": [],
             "RelationId": ""}]}
        print "请求参数data：" + json.dumps(data)
        r = requests.post(gl.url + ":7010/api/" + gl.api_version + "/" + gl.tenant_name + "/" + gl.meta_name,
                          data=json.dumps(data), headers=headers)
        results = json.loads(r.text)
        print results
        RelationId = results["body"][0]["id"]
        # data中的 Record可以从
        data = {"Name": "审批测试sgk" + str(time.strftime('%Y/%m/%d%H%M%S', time.localtime(time.time()))),
                "Description": "审批测试sgk" + str(time.strftime('%Y/%m/%d%H%M%S', time.localtime(time.time()))),
                "RelationType": "Opportunity",
                "OwnerId": "01bc54a795e79def738a5e1fae0ec229", "CCIds": [],
                "Record": {"name": "商机审批10.11", "AccountID": "3c5938c9917ca43b73cad4f5453623b3",
                           "Amount": {"symbol": "CNY", "value": 10000000}, "CloseDate": "2017-10-11T03:59:14Z",
                           "Stage1": "初步意向", "Probability1": "20%", "Stage2": "14天（30天）保持跟进", "Probability2": "20%",
                           "Phone": None, "IndustryCategory": None, "Industry": None, "OtherService": None,
                           "AffiliatedDepartment": "北京直销", "Competitor": None,
                           "CompetitorPrice": {"symbol": None, "value": None}, "Disagreements": None, "Demands": None,
                           "Excitements": None, "FacilitatorType": None, "FacilitatorDiscount": 0,
                           "FacilitatorBusiness": None, "FacilitatorDoubts": None, "LosingStage": None,
                           "LosingReason": None, "LosingDescription": None, "StageUpdatedAt": "2017-10-11T03:59:14Z",
                           "Description": None, "version": 0},
                "PointVoters": [{"PointId": 1, "UserId": "AQAGifYUnayBDAAAn91dvYl07BQoAAAA"},
                                {"PointId": 3, "UserId": "AQAGifYUnayBDAAAn91dvYl07BQoAAAA"}], "GroupVoters": [],
                "RelationId": RelationId}  # 此处 RelationId 就是前面穿件的date id
        template_id = gl.approvals_template_id
        print "请求参数template-id：" + template_id + "，POST data：" + json.dumps(data)
        r = requests.post(
            gl.url + ":7010/api/" + gl.api_version + "/" + gl.tenant_name + "/service/approvals/template/" + template_id + "/run",
            data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        gl.approvals_run_id.insert(0, result["body"]["Aw"]["Id"])  # 此处获得的AwId就是下面请求的runid
        print gl.approvals_run_id
        gl.approvals_point_memberid.insert(0, (result["body"]["Aw"]["Points"][0]["PointMembers"][0]["MemberId"]))
        gl.approvals_point_memberid.insert(1,
                                           (result["body"]["Aw"]["Points"][1]["Groups"][0]["Members"][0]["MemberId"]))
        gl.approvals_point_memberid.insert(2, (result["body"]["Aw"]["Points"][2]["PointMembers"][0]["MemberId"]))
        print gl.approvals_point_memberid

    def test_004_02_create_an_approval(self):
        """POST /api/:ver/:org-name/service/approvals/template/:template-id/run
        创建审批 用于拒绝"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
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
                             "Description": None}]}
        print "请求参数data：" + json.dumps(data)
        r = requests.post(gl.url + ":7010/api/" + gl.api_version + "/" + gl.tenant_name + "/" + gl.meta_name,
                          data=json.dumps(data), headers=headers)
        results = json.loads(r.text)
        print results
        RelationId = results["body"]["Aw"]["id"]
        # data中的 Record可以从
        data = {"Name": "审批测试sgk" + str(time.strftime('%Y/%m/%d%H%M%S', time.localtime(time.time()))),
                "Description": "审批测试sgk" + str(time.strftime('%Y/%m/%d%H%M%S', time.localtime(time.time()))),
                "RelationType": "Opportunity",
                "OwnerId": "01bc54a795e79def738a5e1fae0ec229", "CCIds": [],
                "Record": {"name": "商机审批10.11", "AccountID": "3c5938c9917ca43b73cad4f5453623b3",
                           "Amount": {"symbol": "CNY", "value": 10000000}, "CloseDate": "2017-10-11T03:59:14Z",
                           "Stage1": "初步意向", "Probability1": "20%", "Stage2": "14天（30天）保持跟进", "Probability2": "20%",
                           "Phone": None, "IndustryCategory": None, "Industry": None, "OtherService": None,
                           "AffiliatedDepartment": "北京直销", "Competitor": None,
                           "CompetitorPrice": {"symbol": None, "value": None}, "Disagreements": None, "Demands": None,
                           "Excitements": None, "FacilitatorType": None, "FacilitatorDiscount": 0,
                           "FacilitatorBusiness": None, "FacilitatorDoubts": None, "LosingStage": None,
                           "LosingReason": None, "LosingDescription": None, "StageUpdatedAt": "2017-10-11T03:59:14Z",
                           "Description": None, "version": 0},
                "PointVoters": [{"PointId": 1, "UserId": "AQAGifYUnayBDAAAn91dvYl07BQoAAAA"},
                                {"PointId": 3, "UserId": "AQAGifYUnayBDAAAn91dvYl07BQoAAAA"}], "GroupVoters": [],
                "RelationId": RelationId}  # 此处 RelationId 就是前面创建的date id
        template_id = gl.approvals_template_id
        print "请求参数template-id：" + template_id + "，POST data：" + json.dumps(data)
        r = requests.post(
            gl.url + ":7010/api/" + gl.api_version + "/" + gl.tenant_name + "/service/approvals/template/" + template_id + "/run",
            data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        gl.approvals_run_id.insert(1, result["body"]["Aw"]["Id"])  # 此处获得的AwId就是下面请求的runid
        gl.approvals_point_memberid.insert(3, (result["body"]["Aw"]["Points"][0]["PointMembers"][0]["MemberId"]))
        print gl.approvals_run_id

    def test_004_03_create_an_approval(self):
        """POST /api/:ver/:org-name/service/approvals/template/:template-id/run
        创建审批 用于转发"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
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
                             "Description": None}]}
        print "请求参数data：" + json.dumps(data)
        r = requests.post(gl.url + ":7010/api/" + gl.api_version + "/" + gl.tenant_name + "/" + gl.meta_name,
                          data=json.dumps(data), headers=headers)
        results = json.loads(r.text)
        print results
        RelationId = results["body"][0]["id"]
        # data中的 Record可以从
        data = {"Name": "审批测试sgk" + str(time.strftime('%Y/%m/%d%H%M%S', time.localtime(time.time()))),
                "Description": "审批测试sgk" + str(time.strftime('%Y/%m/%d%H%M%S', time.localtime(time.time()))),
                "RelationType": "Opportunity",
                "OwnerId": "01bc54a795e79def738a5e1fae0ec229", "CCIds": [],
                "Record": {"name": "商机审批10.11", "AccountID": "3c5938c9917ca43b73cad4f5453623b3",
                           "Amount": {"symbol": "CNY", "value": 10000000}, "CloseDate": "2017-10-11T03:59:14Z",
                           "Stage1": "初步意向", "Probability1": "20%", "Stage2": "14天（30天）保持跟进", "Probability2": "20%",
                           "Phone": None, "IndustryCategory": None, "Industry": None, "OtherService": None,
                           "AffiliatedDepartment": "北京直销", "Competitor": None,
                           "CompetitorPrice": {"symbol": None, "value": None}, "Disagreements": None, "Demands": None,
                           "Excitements": None, "FacilitatorType": None, "FacilitatorDiscount": 0,
                           "FacilitatorBusiness": None, "FacilitatorDoubts": None, "LosingStage": None,
                           "LosingReason": None, "LosingDescription": None, "StageUpdatedAt": "2017-10-11T03:59:14Z",
                           "Description": None, "version": 0},
                "PointVoters": [{"PointId": 1, "UserId": "AQAGifYUnayBDAAAn91dvYl07BQoAAAA"},
                                {"PointId": 3, "UserId": "AQAGifYUnayBDAAAn91dvYl07BQoAAAA"}], "GroupVoters": [],
                "RelationId": RelationId}  # 此处 RelationId 就是前面穿件的date id
        template_id = gl.approvals_template_id
        print "请求参数template-id：" + template_id + "，POST data：" + json.dumps(data)
        r = requests.post(
            gl.url + ":7010/api/" + gl.api_version + "/" + gl.tenant_name + "/service/approvals/template/" + template_id + "/run",
            data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        gl.approvals_run_id.insert(2, result["body"]["Aw"]["Id"])  # 此处获得的AwId就是下面请求的runid
        gl.approvals_point_memberid.insert(4, (result["body"]["Aw"]["Points"][0]["PointMembers"][0]["MemberId"]))
        print gl.approvals_run_id

    def test_005_get_approvals_list(self):
        """GET /api/:ver/:org-name/service/approvals/run
        获取审批列表"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        listtype = gl.approvals_listtype[random.randint(0, len(gl.approvals_listtype) - 1)]
        print "请求参数litstype：" + listtype
        # listtype=Submit&orderfield=created_at&odtype=Desc&previous=0&perpage=20
        r = requests.get(
            gl.url + ":7010/api/" + gl.api_version + "/" + gl.tenant_name + "/service/approvals/run?listtype=" + listtype +
            "&orderfield=created_at&odtype=Desc&previous=0&perpage=20",
            headers=headers)
        print gl.url + ":7010/api/" + gl.api_version + "/" + gl.tenant_name + "/service/approvals/run?listtype=" + listtype + "&orderfield=created_at&odtype=Desc&previous=0&perpage=20"
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["AwList"])

    def test_006_get_point_approval_by_run_id(self):
        """GET /api/:ver/:org-name/service/approvals/run/:run-id
        获取指定审批"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        runid = gl.approvals_run_id[0]
        print "请求参数run-id：" + runid
        r = requests.get(
            gl.url + ":7010/api/" + gl.api_version + "/" + gl.tenant_name + "/service/approvals/run/" + runid,
            headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        # point_list = result["body"]["Aw"]["Points"]
        # gl.approvals_point_can_edit_fields.insert(0,point_list[0]["Fields"][0])
        # gl.approvals_point_can_edit_fields.insert(1,point_list[1]["Fields"][0])
        print gl.approvals_point_memberid

        # 上面这行代码后续将会写成一个方法

    def test_007_fill_fields_by_point_id(self):
        """PUT /api/:ver/:org-name/service/approvals/run/:run-id/fill-fields/:point-id
        在指定审批节点填写可编辑字段数据"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        runid = gl.approvals_run_id[0]
        pointid = gl.approvals_point_id  # point 审批节点 状态必须为"Status": "Voting" 才能编辑字段
        data = {
            gl.approvals_point_can_edit_fields[0]: "point" + pointid
        }  # 此处审批字段可通过test_1_get_approvaling_fields_by_approval_name 获得
        print "请求参数run-id：" + runid + "，编辑字段：" + gl.approvals_point_can_edit_fields[0]
        r = requests.put(
            gl.url + ":7010/api/" + gl.api_version + "/" + gl.tenant_name + "/service/approvals/run/" + runid + "/fill-fields/" + pointid,
            data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])

    def test_008_01_vote_point_approval_by_run_id(self):
        """POST /api/:ver/:org-name/service/approvals/run/:run-id/vote
        投票指定审批  同意"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        runid = gl.approvals_run_id[0]
        # {"GroupId":0,"PointId":1,"Comment":"Agree","MemberId":"AQAGifYUnayBDAAA1shSRKXB7BSAAAAA"}
        data = {
            "GroupId": 0,
            "PointId": 1,
            "Comment": "Agree",
            "MemberId": gl.approvals_point_memberid[0]
        }
        print "请求参数run-id：" + runid + "，data：" + json.dumps(data)
        r = requests.post(
            gl.url + ":7010/api/" + gl.api_version + "/" + gl.tenant_name + "/service/approvals/run/" + runid + "/vote",
            data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        self.assertEqual(result["body"]["Aw"]["Points"][0]["PointMembers"][0]["Status"], "Approval")
        self.assertEqual(result["body"]["Aw"]["Points"][0]["PointMembers"][1]["Status"], "Closed")

    def test_008_02_vote_point_approval_by_run_id(self):
        """POST /api/:ver/:org-name/service/approvals/run/:run-id/vote
        投票指定审批  同意"""
        headers = {
            'x-token': gl.access_token_point_2,
            'content-type': gl.content_type
        }

        runid = gl.approvals_run_id[0]

        data = {
            gl.approvals_point_can_edit_fields[1]: "point2"
        }  # 此处审批字段可通过test_1_get_approvaling_fields_by_approval_name 获得
        print gl.approvals_point_can_edit_fields[1]
        print "请求参数run-id：" + runid + "，编辑字段：" + gl.approvals_point_can_edit_fields[1]
        r = requests.put(
            gl.url + ":7010/api/" + gl.api_version + "/" + gl.tenant_name + "/service/approvals/run/" + runid + "/fill-fields/2",
            data=json.dumps(data), headers=headers)
        print r, r.text

        # {"GroupId":0,"PointId":1,"Comment":"Agree","MemberId":"AQAGifYUnayBDAAA1shSRKXB7BSAAAAA"}
        data = {
            "GroupId": 1,
            "PointId": 2,
            "Comment": "Agree",
            "MemberId": gl.approvals_point_memberid[1]
        }
        print "请求参数run-id：" + runid + "，data：" + json.dumps(data)
        r = requests.post(
            gl.url + ":7010/api/" + gl.api_version + "/" + gl.tenant_name + "/service/approvals/run/" + runid + "/vote",
            data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        self.assertEqual(result["body"]["Aw"]["Points"][0]["PointMembers"][0]["Status"], "Approval")
        self.assertEqual(result["body"]["Aw"]["Points"][0]["PointMembers"][1]["Status"], "Closed")

    def test_008_03_vote_point_approval_by_run_id(self):
        """POST /api/:ver/:org-name/service/approvals/run/:run-id/vote
        投票指定审批  同意"""
        headers = {
            'x-token': gl.access_token_point_3,
            'content-type': gl.content_type
        }
        runid = gl.approvals_run_id[0]
        # {"GroupId":0,"PointId":1,"Comment":"Agree","MemberId":"AQAGifYUnayBDAAA1shSRKXB7BSAAAAA"}
        data = {
            "GroupId": 0,
            "PointId": 3,
            "Comment": "Agree",
            "MemberId": gl.approvals_point_memberid[2]
        }
        print "请求参数run-id：" + runid + "，data：" + json.dumps(data)
        r = requests.post(
            gl.url + ":7010/api/" + gl.api_version + "/" + gl.tenant_name + "/service/approvals/run/" + runid + "/vote",
            data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        self.assertEqual(result["body"]["Aw"]["Points"][0]["PointMembers"][0]["Status"], "Approval")
        self.assertEqual(result["body"]["Aw"]["Points"][0]["PointMembers"][1]["Status"], "Closed")

    def test_009_vote_point_approval_by_run_id(self):
        """POST /api/:ver/:org-name/service/approvals/run/:run-id/vote
        投票指定审批  拒绝"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        runid = gl.approvals_run_id[1]
        # {"GroupId":0,"PointId":1,"Comment":"Agree","MemberId":"AQAGifYUnayBDAAA1shSRKXB7BSAAAAA"}
        data = {
            "GroupId": 0,
            "PointId": int(gl.approvals_point_id),
            "Comment": "DisAgree",
            "MemberId": gl.approvals_point_memberid[3]
        }
        print "请求参数run-id：" + runid + "，data：" + json.dumps(data)
        r = requests.post(
            gl.url + ":7010/api/" + gl.api_version + "/" + gl.tenant_name + "/service/approvals/run/" + runid + "/vote",
            data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        self.assertEqual(result["body"]["Aw"]["Points"][0]["PointMembers"][0]["Status"], "Reject")
        self.assertEqual(result["body"]["Aw"]["Points"][0]["PointMembers"][1]["Status"], "Voting")

    def test_010_forward_point_approval_by_run_id(self):
        """POST /api/:ver/:org-name/service/approvals/run/:run-id/forward
        转发指定审批"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        runid = gl.approvals_run_id[2]
        data = {
            "GroupId": 0,
            "PointId": int(gl.approvals_point_id),
            "MemberId": gl.approvals_point_memberid[4],
            "ToUid": gl.approvals_point_touid
        }
        print "请求参数run-id：" + runid + "，data：" + json.dumps(data)
        r = requests.post(
            gl.url + ":7010/api/" + gl.api_version + "/" + gl.tenant_name + "/service/approvals/run/" + runid + "/forward",
            data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])

    def test_011_add_comments_to_point_approval(self):
        """POST /api/:ver/:org-name/service/approvals/run/:run-id/comments
        在指定审批发表评论"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        runid = gl.approvals_run_id[0]
        data = {"content": "评论：add a new comment"}
        print "请求参数run-id：" + runid + "，评论内容：" + json.dumps(data)
        r = requests.post(
            gl.url + ":7010/api/" + gl.api_version + "/" + gl.tenant_name + "/service/approvals/run/" + runid + "/comments",
            data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])

    def test_012_get_point_approval_comments_list(self):
        """GET /api/:ver/:org-name/service/approvals/run/:run-id/comments
        获取指定审批的评论列表"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        runid = gl.approvals_run_id[0]
        print "请求参数run-id：" + runid
        r = requests.get(
            gl.url + ":7010/api/" + gl.api_version + "/" + gl.tenant_name + "/service/approvals/run/" + runid + "/comments",
            headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])

    def test_013_get_approvals_objects_list_count(self):
        """GET   /api/:ver/:org-name/service/approvals/run/list-counts
        获取审批标准对象当前数量"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        r = requests.get(
            gl.url + ":7010/api/" + gl.api_version + "/" + gl.tenant_name + "/service/approvals/run/list-counts",
            headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])

    def test_014_close_point_approval_by_run_id(self):
        """PUT /api/:ver/:org-name/service/approvals/run/:run-id/close
        关闭指定审批"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        runid = gl.approvals_run_id[1]
        print "请求的参数审批id：" + runid
        r = requests.put(
            gl.url + ":7010/api/" + gl.api_version + "/" + gl.tenant_name + "/service/approvals/run/" + runid + "/close",
            headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        # self.assertIsNotNone(result["body"])   #关闭审批之后，返回body 为 None


gl.suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestApprovalsProcess))
