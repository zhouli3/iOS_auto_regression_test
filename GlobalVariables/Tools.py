# -*- coding: utf-8 -*-
import xlrd
import json
import os
import ConfigParser as cparser
import csv
import gl
import sys
import requests
import GetParamFromFile as gpff
import gl

reload(sys)
sys.setdefaultencoding('utf-8')
requests.packages.urllib3.disable_warnings()

"""
基础配置：
    1、标准对象创建/配置
    2、Judge配置
"""

"""在新建的Meta中批量添加列"""


def add_clonum_to_meta_from_csv_file(self):
    """使用csv中的数据在meta中增加列"""
    headers = {
        'x-token': gl.access_token,
        'content-type': gl.content_type
    }
    data_list = gpff.get_fields_data_from_csv_file(gpff)
    count = 1
    for data in data_list:
        print "第" + str(count) + "次请求"
        count += 1
        print "请求参数：" + json.dumps(data)
        try:
            r = requests.put(
                gl.url + ":7020/api/v1.0/SGSoft测试/Products/meta/add",
                data=json.dumps(data), headers=headers, verify=False)
            print r, r.text
            self.assertEqual(r.status_code, 200)
            self.assertEqual(r.json()["code"], 0)
            result = json.loads(r.text)
            self.assertIsNotNone(result["body"])
        except:
            continue


"""将CI环境中的数据复制到生产"""


def create_meta_schema_with_ci_env_meta(self):
    """使用集成环境中的meta在生产环境创建meta"""
    headers = {
        'x-token': gl.access_token_online,
        'content-type': gl.content_type
    }
    clonum_dict = get_meta_from_ci_env(self)
    keys = list(clonum_dict.keys())
    count = 1
    for key in keys:
        print "第" + str(count) + "次请求"
        count += 1
        print "创建的列名：" + key
        data = clonum_dict[key]
        try:
            r = requests.put(
                gl.url_online + "/ddl/api/v1.0/test企业test001/" + gl.meta_name + "/meta/add",  # Opportunity
                data=json.dumps(data), headers=headers, verify=False)
            print r, r.text
        except:
            continue


"""将CI环境中的数据复制到生产"""


def create_new_com_meta_schema_with_ci_env_meta(self):
    """使用集成环境中的meta在生产环境创建meta"""
    headers = {
        'x-token': gl.access_token_lt_166,
        'content-type': gl.content_type
    }
    data = {"code": 0, "body": {
        "AccountID": {"name": "AccountID", "display_name": "相关客户", "type": "master", "object_name": "Account",
                      "searchable": True, "readable": True, "writable": True},
        "AffiliatedDepartment": {"name": "AffiliatedDepartment", "display_name": "所属部门", "type": "picklist",
                                 "options": {"list": {"all": {
                                     "options_value": ["北京直销", "上海直销", "西区直销", "西区渠道", "深圳直销", "线上资源直销", "研发部门", "产品部门",
                                                       "线上支持", "增值部门"]}}}, "nullable": True, "searchable": True,
                                 "readable": True, "writable": True},
        "Amount": {"name": "Amount", "display_name": "销售金额", "type": "currency", "searchable": True, "readable": True,
                   "writable": True},
        "CloseDate": {"name": "CloseDate", "display_name": "结单日期", "type": "datetime", "searchable": True,
                      "readable": True, "writable": True},
        "Competitor": {"name": "Competitor", "display_name": "竞品", "type": "text", "nullable": True, "searchable": True,
                       "readable": True, "writable": True},
        "CompetitorPrice": {"name": "CompetitorPrice", "display_name": "竞品价格", "type": "currency", "nullable": True,
                            "searchable": True, "readable": True, "writable": True},
        "Demands": {"name": "Demands", "display_name": "客户需求点", "type": "textarea", "nullable": True,
                    "searchable": True, "readable": True, "writable": True},
        "Description": {"name": "Description", "display_name": "备注", "type": "textarea", "nullable": True,
                        "searchable": True, "readable": True, "writable": True},
        "Disagreements": {"name": "Disagreements", "display_name": "客户异议点", "type": "textarea", "nullable": True,
                          "searchable": True, "readable": True, "writable": True},
        "Excitements": {"name": "Excitements", "display_name": "客户兴趣点", "type": "textarea", "nullable": True,
                        "searchable": True, "readable": True, "writable": True},
        "FacilitatorBusiness": {"name": "FacilitatorBusiness", "display_name": "服务商业务", "type": "textarea",
                                "nullable": True, "searchable": True, "readable": True, "writable": True},
        "FacilitatorDiscount": {"name": "FacilitatorDiscount", "display_name": "服务商折扣", "type": "double",
                                "nullable": True, "searchable": True, "readable": True, "writable": True},
        "FacilitatorDoubts": {"name": "FacilitatorDoubts", "display_name": "服务商疑虑", "type": "textarea",
                              "nullable": True, "searchable": True, "readable": True, "writable": True},
        "FacilitatorType": {"name": "FacilitatorType", "display_name": "服务商类型", "type": "picklist",
                            "options": {"list": {"all": {"options_value": ["货款", "保证金"]}}}, "nullable": True,
                            "searchable": True, "readable": True, "writable": True},
        "Industry": {"name": "Industry", "display_name": "行业", "type": "picklist",
                     "options": {"related": "IndustryCategory", "list": {"IT|通信|电子|互联网": {
                         "options_value": ["互联网", "电子商务", "金融", "企业服务", "教育", "文化娱乐", "游戏", "O2O", "硬件"]}, "交通运输物流仓储": {
                         "options_value": ["物流/仓储", "交通/运输"]}, "农|林|牧|渔|其他": {
                         "options_value": ["农/林/牧/渔", "跨领域经营", "其他"]}, "商业服务": {
                         "options_value": ["专业服务/咨询/财会/法律/(人力资源等)", "广告/会展/公关", "中介服务", "外包服务", "检验/检测/认证"]},
                         "房地产|建筑业": {"options_value": ["房地产/建筑/建材/工程",
                                                       "家具/室内设计/装饰装潢",
                                                       "物业管理/商业中心"]},
                         "政府|非盈利机构": {"options_value": ["政府/公共事业/非盈利机构",
                                                        "学术/科研"]},
                         "文体教育|工艺美术": {"options_value": ["教育/培训/院校",
                                                         "礼品/玩具工艺/美术收藏品奢侈品"]},
                         "文化|传媒|娱乐|体育": {
                             "options_value": ["媒体/出版/影视/文化传播",
                                               "娱乐/体育/休闲"]}, "服务业": {
                             "options_value": ["医疗/护理/美容/保健/卫生服务", "旅游/度假", "酒店/餐饮"]}, "生产|加工|制造": {
                             "options_value": ["汽车/摩托车", "教工制造（原料加/工模具）", "印刷/包装/造纸", "医药/生物工程", "航空/航天与制造",
                                               "大型设备/机电设备/重工业", "仪器仪表及工业自动化", "办公用品及设备", "医疗设备/机械"]}, "能源|矿产|环保": {
                             "options_value": ["能源/矿产/采掘/冶炼", "电气/电力/水利", "石油/石化/化工", "环保"]}, "贸易|批发|零售|租赁业": {
                             "options_value": ["快速消费品（食品/饮料/烟酒/日化）", "耐用消费品（服饰/纺织/皮革/家具/家电）", "贸易/进出口", "零售/批发",
                                               "租赁服务"]}, "金融业": {
                             "options_value": ["基金/证券/期货/投资", "银行", "保险", "信托/担保/拍卖/典当"]}}}, "nullable": True,
                     "searchable": True, "readable": True, "writable": True},
        "IndustryCategory": {"name": "IndustryCategory", "display_name": "行业大类", "type": "picklist", "options": {
            "list": {"all": {
                "options_value": ["IT|通信|电子|互联网", "金融业", "房地产|建筑业", "商业服务", "贸易|批发|零售|租赁业", "文体教育|工艺美术", "生产|加工|制造",
                                  "交通运输物流仓储", "服务业", "文化|传媒|娱乐|体育", "能源|矿产|环保", "政府|非盈利机构", "农|林|牧|渔|其他"]}}},
                             "nullable": True, "searchable": True, "readable": True, "writable": True},
        "LosingDescription": {"name": "LosingDescription", "display_name": "输单描述", "type": "textarea", "nullable": True,
                              "searchable": True, "readable": True, "writable": True},
        "LosingReason": {"name": "LosingReason", "display_name": "输单原因", "type": "textarea", "nullable": True,
                         "searchable": True, "readable": True, "writable": True},
        "LosingStage": {"name": "LosingStage", "display_name": "输单阶段", "type": "picklist", "options": {
            "list": {"all": {"options_value": ["待上门", "意向跟进", "试用解决问题", "报价谈判", "签约审批", "签约待回款", "签约已回款", "失败"]}}},
                        "nullable": True, "searchable": True, "readable": True, "writable": True},
        "OtherService": {"name": "OtherService", "display_name": "其他服务", "type": "text", "nullable": True,
                         "searchable": True, "readable": True, "writable": True},
        "Phone": {"name": "Phone", "display_name": "电话", "type": "phone", "nullable": True, "searchable": True,
                  "readable": True, "writable": True},
        "Probability1": {"name": "Probability1", "display_name": "新签扩容机会赢率", "type": "picklist",
                         "options": {"related": "Stage1", "list": {"了解产品认同美洽": {"options_value": ["60%"]},
                                                                   "初步意向": {"options_value": ["20%"]},
                                                                   "确定产品和价格": {"options_value": ["80%"]},
                                                                   "调研客服系统产品": {"options_value": ["40%"]},
                                                                   "赢单": {"options_value": ["100%"]},
                                                                   "输单": {"options_value": ["0%"]}}},
                         "searchable": True, "readable": True, "writable": True},
        "Probability2": {"name": "Probability2", "display_name": "续费机会赢率", "type": "picklist",
                         "options": {"related": "Stage2", "list": {"14天（30天）保持跟进": {"options_value": ["20%"]},
                                                                   "到期前一月联系客户": {"options_value": ["60%"]},
                                                                   "签署合同": {"options_value": ["80%"]},
                                                                   "续费失败": {"options_value": ["0%"]},
                                                                   "续费成功": {"options_value": ["100%"]},
                                                                   "近30天活跃": {"options_value": ["40%"]}}},
                         "searchable": True, "readable": True, "writable": True},
        "Stage": {"name": "Stage", "display_name": "商机阶段", "type": "path", "options": {
            "list": {"all": {"options_value": ["初步意向", "调研客服系统产品", "了解产品认同美洽", "确认产品和价格", "赢单", "输单"]}}},
                  "nullable": True, "readable": True, "writable": True},
        "Stage1": {"name": "Stage1", "display_name": "新签扩容机会销售阶段", "type": "picklist", "options": {
            "list": {"all": {"options_value": ["初步意向", "调研客服系统产品", "了解产品认同美洽", "确定产品和价格", "赢单", "输单"]}}},
                   "searchable": True, "readable": True, "writable": True},
        "Stage2": {"name": "Stage2", "display_name": "续费机会销售阶段", "type": "picklist", "options": {
            "list": {"all": {"options_value": ["14天（30天）保持跟进", "近30天活跃", "到期前一月联系客户", "签署合同", "续费成功", "续费失败"]}}},
                   "searchable": True, "readable": True, "writable": True},
        "StageUpdatedAt": {"name": "StageUpdatedAt", "display_name": "阶段更新时间", "type": "datetime", "nullable": True,
                           "searchable": True, "readable": True, "writable": True},
        "Test": {"name": "Test", "display_name": "test_Path组件", "type": "picklist", "options": {"related": "Stage",
                                                                                                "list": {"了解产品认同美洽": {
                                                                                                    "options_value": [
                                                                                                        "Yes", "No"]},
                                                                                                    "初步意向": {
                                                                                                        "options_value": [
                                                                                                            "a",
                                                                                                            "b",
                                                                                                            "c",
                                                                                                            "d"]},
                                                                                                    "确认产品和价格": {
                                                                                                        "options_value": [
                                                                                                            "已确认",
                                                                                                            "未确认"]},
                                                                                                    "调研客服系统产品": {
                                                                                                        "options_value": [
                                                                                                            "e",
                                                                                                            "f",
                                                                                                            "j",
                                                                                                            "k"]},
                                                                                                    "赢单": {
                                                                                                        "options_value": [
                                                                                                            "Yes",
                                                                                                            "No"]},
                                                                                                    "输单": {
                                                                                                        "options_value": [
                                                                                                            "Yes",
                                                                                                            "No"]}}},
                 "nullable": True, "readable": True, "writable": True},
        "created_at": {"name": "created_at", "display_name": "创建时间", "type": "datetime", "readable": True},
        "created_by": {"name": "created_by", "display_name": "创建人", "type": "lookup", "object_name": "User",
                       "delete_option": "Restrict", "readable": True},
        "id": {"name": "id", "display_name": "ID", "type": "object_id", "readable": True},
        "name": {"name": "name", "display_name": "机会名称", "type": "text", "index": True, "searchable": True,
                 "readable": True, "writable": True},
        "owner": {"name": "owner", "display_name": "所有者", "type": "lookup", "object_name": "User",
                  "delete_option": "Restrict", "readable": True},
        "record_type": {"name": "record_type", "display_name": "记录类型", "type": "picklist",
                        "options": {"list": {"all": {"options_value": ["main"]}}}, "default_value": {"value": "main"},
                        "readable": True, "writable": True},
        "system_mod_stamp": {"name": "system_mod_stamp", "display_name": "系统修改时间", "type": "datetime",
                             "readable": True},
        "updated_at": {"name": "updated_at", "display_name": "修改时间", "type": "datetime", "readable": True},
        "updated_by": {"name": "updated_by", "display_name": "修改人", "type": "lookup", "object_name": "User",
                       "delete_option": "Restrict", "readable": True},
        "version": {"name": "version", "display_name": "版本", "type": "integer", "default_value": {"value": "0"},
                    "readable": True}}}

    clonum_dict = data["body"]
    keys = list(clonum_dict.keys())
    count = 1
    for key in keys:
        print "第" + str(count) + "次请求"
        count += 1
        print "创建的列名：" + key
        data = clonum_dict[key]
        try:
            r = requests.put(
                gl.url + ":7020/api/v1.0/" + gl.tenant_name + "/" + gl.meta_name + "/meta/add",
                data=json.dumps(data), headers=headers, verify=False)
            print r, r.text
            print gl.url + ":7020/api/v1.0/" + gl.tenant_name + "/" + gl.meta_name + "/meta/add"
        except:
            continue


def create_meta_object_online(self):
    """在生产环境创建meta"""
    headers = {
        'x-token': gl.access_token_online,
        'content-type': gl.content_type
    }
    name = gl.meta_name
    data = {
        "display_name": gl.meta_name,
        "description": "the description of " + gl.meta_name
    }
    print "请求数据：" + json.dumps(data)
    # meta创建和更新的端口是7020
    r = requests.post(gl.url_online + "/ddl/api/v1.0/test企业test001/" + name + "/meta", data=json.dumps(data),
                      headers=headers, verify=False)
    # r=requests.get(gl.url+"/api/v1.0/tenant-name/all-metas",params=data,headers=headers)
    print r, r.text


def delete_meta_object_online(self):
    """在生产环境删除meta"""
    headers = {
        'x-token': gl.access_token_online,
        'content-type': gl.content_type
    }
    name = "Opportunity"
    # meta创建和更新的端口是7020
    r = requests.delete(gl.url_online + "/ddl/api/v1.0/test企业test001/" + name + "/meta",
                        headers=headers, verify=False)
    # r=requests.get(gl.url+"/api/v1.0/tenant-name/all-metas",params=data,headers=headers)
    print r, r.text


"""用户授权和标准对象授权"""


def assign_profile_to_point_user(self):
    """授权到指定用户
    POST /acl_admin/profile/:profile_id/user"""
    headers = {
        'x-token': gl.access_token_online,
        'content-type': gl.content_type
    }
    profile_ent_id = get_acl_profile_online(self)
    data = {
        "ent_id": "AQACd5VVkc7RCAAA6vXOmrnF6BSVKwAA",
        "profile_id": "AQACd5VVkc7RCAAA1sIDurnF6BSXKwAA",
        "user_id": "AQACd5VVkc7RCAAALgrgmrnF6BSWKwAA"
        # AQACd5VVkc7RCAAALgrgmrnF6BSWKwAA   AQACd5VVkc7RCAAAucWwesDL7BR7QAAA
    }
    r = requests.post(
        gl.url_online + "/acl/acl_admin/profile/AQACd5VVkc7RCAAA1sIDurnF6BSXKwAA/user",
        data=json.dumps(data), headers=headers, verify=False)
    print gl.url_online + "/acl/acl_admin/profile/AQACd5VVkc7RCAAA1sIDurnF6BSXKwAA/user"
    print r, r.text


def add_profile_OLA(self):
    """添加meta权限到profile"""
    headers = {
        'x-token': gl.access_token_online,
        'content-type': gl.content_type
    }
    profile_ent_id = get_acl_profile_online(self)
    data = {
        "ent_id": "AQACd5VVkc7RCAAA6vXOmrnF6BSVKwAA",
        "profile_id": "AQACd5VVkc7RCAAA1sIDurnF6BSXKwAA",
        "access": {
            "object_name": gl.meta_name,
            "creatable": True,
            "updatable": True,
            "readable": True,
            "deletable": True,
            "view_all": True,
            "modify_all": True
        }
    }
    r = requests.put(
        gl.url_online + "/acl/acl_admin/profile/AQACd5VVkc7RCAAA1sIDurnF6BSXKwAA/object_level_access",
        data=json.dumps(data), headers=headers, verify=False)
    print gl.url_online + "/acl/acl_admin/profile/" + profile_ent_id[0] + "/object_level_access"
    print r, r.text
    get_acl_profile_online(self)


def add_profile_FLA(self):
    """添加meta的字段权限到profile"""
    headers = {
        'x-token': gl.access_token_online,
        'content-type': gl.content_type
    }
    profile_ent_id = get_acl_profile_online(self)
    clonum_dict = get_meta_from_online_env(self)
    keys = list(clonum_dict.keys())
    for key in keys:
        print key
        data = {
            "ent_id": "AQACd5VVkc7RCAAA6vXOmrnF6BSVKwAA",
            "profile_id": "AQACd5VVkc7RCAAA1sIDurnF6BSXKwAA",
            "access": {
                "object_name": gl.meta_name,
                "field_name": key,
                "updatable": True,
                "readable": True
            }
        }
        r = requests.put(
            gl.url_online + "/acl/acl_admin/profile/AQACd5VVkc7RCAAA1sIDurnF6BSXKwAA/field_level_access",
            data=json.dumps(data), headers=headers, verify=False)
        print gl.url_online + "/acl/acl_admin/profile/" + profile_ent_id[0] + "/field_level_access"
        print r, r.text


def get_meta_from_online_env(self):
    """从生产环境获取meta"""
    headers = {
        'x-token': gl.access_token_online,
        'content-type': gl.content_type
    }
    r = requests.get(
        gl.url_online + "/dml/api/v1.0/test企业test001/" + gl.meta_name + "/meta/schema",
        headers=headers, verify=False)
    print r, r.text
    result = json.loads(r.text)
    meta_schema_list = result["body"]
    print meta_schema_list, type(meta_schema_list)
    return meta_schema_list


def get_meta_from_ci_env(self):
    """从集成环境获取meta"""
    headers = {
        'x-token': gl.access_token,
        'content-type': gl.content_type
    }
    r = requests.get(
        gl.url + ":7010/api/v1.0/meiqia/" + gl.meta_name + "/meta/schema",
        headers=headers)
    print r, r.text
    result = json.loads(r.text)
    meta_schema_list = result["body"]
    print meta_schema_list, type(meta_schema_list)
    return meta_schema_list


def get_meta_from_lt_env(self):
    """从联调环境获取meta"""
    headers = {
        'x-token': gl.access_token,
        'content-type': gl.content_type
    }
    r = requests.get(
        gl.url + ":7010/api/v1.0/meiqia/Opportunity/meta/schema",
        headers=headers)
    print r, r.text
    result = json.loads(r.text)
    meta_schema_list = result["body"]
    print meta_schema_list, type(meta_schema_list)
    return meta_schema_list


def get_acl_profile_online(self):
    """获取权限profile"""
    headers = {
        'x-token': gl.access_token_online,
        'content-type': gl.content_type
    }
    r = requests.get(
        gl.url_online + "/acl/acl_admin/profile",
        headers=headers, verify=False)
    print gl.url_online + "/acl/acl_admin/profile"
    print r, r.text
    result = json.loads(r.text)
    profile_ent_id = []
    profile_ent_id.insert(0, result["profiles"][0]["profile_id"])
    profile_ent_id.insert(1, result["profiles"][0]["ent_id"])
    return profile_ent_id
