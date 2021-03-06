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


class TestApprovalsTemplate(unittest.TestCase):
    """测试 审批模板 相关接口"""

    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."

    def test_1_get_all_approvals_template_list(self):
        """GET /api/:ver/:org-name/service/approvals/template
        获取审批模板列表"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        r = requests.get(
            gl.url + ":7010/api/"+gl.api_version+"/" + gl.tenant_name + "/service/approvals/template/object",
            headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        res = result["body"]
        gl.object_approvals_template_name = result["body"][random.randint(0, len(res) - 1)]["name"]

    def test_2_get_object_all_approvals_template(self):
        """GET /api/:ver/:org-name/service/approvals/template/object/template-name
        获取Object对应的审批模板列表"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = gl.object_approvals_template_name
        r = requests.get(
            gl.url + ":7010/api/"+gl.api_version+"/" + gl.tenant_name + "/service/approvals/template/object/" + data,
            headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        res = result["body"]

    def test_3_create_approvals_template(self):
        """POST /api/:ver/:org-name/service/approvals/template"""
        headers = {
            'x-token': gl.access_token_test,
            'content-type': gl.content_type
        }
        data = {
            "SerialFmt": "",
            "Name": "Invoice-Folder审批测试模板-123123",
            "Description": "Invoice-Folder审批测试模板-123123",
            "Priority": 1,
            "ObjType": "Invoice",
            "UseStatus": "Apply",
            "CCIds": [],
            "Fields": [
                "Approvalstatus",
                "Bank",
                "BankAccount",
                "BussLicense.country",
                "BussLicense.state",
                "BussLicense.city",
                "BussLicense.street",
                "ContactID",
                "InvoiceStatus",
                "InvoiceTitle",
                "InvoiceType",
                "PayID",
                "PostAddress.country",
                "PostAddress.state",
                "PostAddress.city",
                "PostAddress.street",
                "PostCode",
                "PostTime",
                "Proof.filename",
                "Proof.size",
                "Proof.url",
                "RechargeID",
                "TaxNumber",
                "Type",
                "id",
                "name",
                "owner",
                "Proofs"
            ],
            "RecordCond": {
                "Exps": [
                    {
                        "Stmt": {
                            "FieldName": "Proofs",
                            "CalculateField": "ISNULL(Proofs)",
                            "Operator": "==",
                            "Value": "false",
                            "StmtDesc": "有图片"
                        },
                        "EType": "Perse"
                    }
                ],
                "Formula": "1"
            },
            "Points": [
                {
                    "Name": "审批节点1",
                    "VotePolicy": "OR",
                    "PointMembers": [
                        {
                            "MemberType": "SELF",
                            "UserId": "AQACk5HxFIZ1DAAAZ_EayDS79BStAwAA"
                        }
                    ]
                }
            ]
        }
        print "请求参数：" + json.dumps(data)
        r = requests.post(gl.url + ":7010/api/"+gl.api_version+"/" + gl.tenant_name + "/service/approvals/template",
                          data=json.dumps(data), headers=headers, verify=False)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])
        gl.approvals_template_id = result["body"]["Id"]

    def test_4_get_approvals_template_by_id(self):
        """GET /api/v1.0/meiqia/service/approvals/template/:template-id
        通过ID获取指定审批模板"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = gl.approvals_template_id
        r = requests.get(
            gl.url + ":7010/api/"+gl.api_version+"/" + gl.tenant_name + "/service/approvals/template/" + data,
            headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"])

    def test_5_update_approvals_template_by_id(self):
        """PUT /api/:ver/:org-name/service/approvals/template/:template-id
        通过ID修改指定审批模板"""
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = {
            "SerialFmt": "RECHARGE",
            "Name": "充值订单折扣审批sgkstest",
            "Description": "折扣不能低于0.3",
            "Priority": 1,
            "ObjType": "Recharge",
            "UseStatus": "Apply",
            "CCIds": [
                "529f80f13d57c2ec225ed26e9972d5fe",
                "4250baf69cc473e87e8090cb3938c431"
            ],
            "Fields": [
                "Amount"
            ],
            "UserCond": {
                "CdType": "User",
                "TargetId": "3b8549fb3fc5598b1d4f37aa564b4afb"
            },
            "RecordCond": {
                "Exps": [
                    {
                        "Stmt": {
                            "CalculateField": "PreOpen",
                            "FieldName": "Discount",
                            "Operator": "<=",
                            "Value": "0.3"
                        },
                        "EType": "Perse"
                    }
                ],
                "Formula": "1"
            },
            "Points": [
                {
                    "Name": "审批节点1",
                    "VotePolicy": "AND",
                    "PointMembers": [
                        {
                            "MemberType": "Manager",
                            "Formula": "user.Manager"
                        }
                    ]
                },
                {
                    "Name": "审批节点2",
                    "VotePolicy": "OR",
                    "Groups": [
                        {
                            "Name": "审批组21",
                            "VotePolicy": "OR",
                            "Members": [
                                {
                                    "UserId": "31676c8da5a36458678f056185dd3fd7",
                                    "MemberType": "SELF"
                                }
                            ]
                        },
                        {
                            "Name": "审批组22",
                            "VotePolicy": "OR",
                            "Members": [
                                {
                                    "UserId": "3ac7c8376eaea7ef60cb2bff5f988ff5",
                                    "MemberType": "SELF"
                                }
                            ]
                        },
                        {
                            "Name": "审批组23",
                            "VotePolicy": "OR",
                            "Members": [
                                {
                                    "UserId": "31a061e837b6322c2428dcfbbd35d9cd",
                                    "MemberType": "SELF"
                                }
                            ]
                        }
                    ]
                }
            ]
        }
        print "请求参数：" + json.dumps(data)
        r = requests.put(
            gl.url + ":7010/api/"+gl.api_version+"/" + gl.tenant_name + "/service/approvals/template/" + gl.approvals_template_id,
            data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        # result = json.loads(r.text)

    def test_6_active_approvals_template_by_id(self):
        """PUT /api/:ver/:org-name/service/approvals/template/:template-id/active
        http://10.102.1.64:7010/api/v1.0/meiqia/service/approvals/template/AQACk5HxFIb0DQAAfcqnbSDE6BQRAAAA/active
        """
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = gl.approvals_template_id
        print "请求参数approvals_template_id：" + data
        print gl.url + ":7010/api/"+gl.api_version+"/" + gl.tenant_name + "/service/approvals/template/" + data + "/active"
        r = requests.put(
            gl.url + ":7010/api/"+gl.api_version+"/" + gl.tenant_name + "/service/approvals/template/" + data + "/active",
            headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        # result = json.loads(r.text)

    def test_7_inactive_approvals_template_by_id(self):
        """PUT /api/:ver/:org-name/service/approvals/template/:template-id/inactive
        http://10.102.1.64:7010/api/v1.0/meiqia/service/approvals/template/AQACk5HxFIb0DQAAfcqnbSDE6BQRAAAA/inactive
        """
        headers = {
            'x-token': gl.access_token,
            'content-type': gl.content_type
        }
        data = gl.approvals_template_id
        print "请求参数approvals_template_id：" + data
        r = requests.put(
            gl.url + ":7010/api/"+gl.api_version+"/" + gl.tenant_name + "/service/approvals/template/" + data + "/inactive",
            headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)

    def test_8_delete_approvals_template_by_id(self):
        """DELETE /api/:ver/:org-name/service/approvals/template/:template-id
        http://10.102.1.64:7010/api/v1.0/meiqia/service/approvals/template/AQACk5HxFIb0DQAAfcqnbSDE6BQRAAAA
        """
        headers = {
            'x-token': gl.access_token_test,
            'content-type': gl.content_type
        }
        data = gl.approvals_template_id
        print "请求参数approvals_template_id：" + data
        r = requests.delete(
            gl.url + ":7010/api/"+gl.api_version+"/" + gl.tenant_name + "/service/approvals/template/" + data,
            headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)


gl.suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestApprovalsTemplate))
