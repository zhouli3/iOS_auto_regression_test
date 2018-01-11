# -*- coding: utf-8 -*-
import xlrd
import json
import os
import ConfigParser as cparser
import csv
from GlobalVariables import gl
import sys
import requests
from GlobalVariables import GetParamFromFile as gpff

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


"""将CI环境中meiqia企业的数据复制到测试专用企业勿动"""


def create_new_com_meta_schema_with_ci_env_meta(self):
    """将CI环境中meiqia企业的数据复制到测试专用企业勿动"""
    headers = {
        'x-token': gl.access_token_test,
        'content-type': gl.content_type
    }
    clonum_dict = get_all_meta_from_ci_env()
    keys = list(clonum_dict.keys())
    for key in keys:
        count = 1
        object_info = clonum_dict[key]
        display_name = object_info["display_name"]
        schema = object_info["schema"]
        """data = {
            "display_name": display_name,
            "description": "the description of " + display_name
        }
        print "新建标准对象：" + key + ",请求数据：" + json.dumps(data) """
        # meta创建和更新的端口是7020
        try:
            """r = requests.post(gl.url + ":7020/api/v1.0/" + gl.tenant_name_test + "/" + key + "/meta", data=json.dumps(data),
                          headers=headers)
            print r, r.text
            print schema """
            data = {
                "ent_id": "AQACk5HxFIZ1DAAAA48EyDS79BSsAwAA",
                "profile_id": "AQACk5HxFIZ1DAAAdyuRdDW79BSwAwAA",
                "access": {
                    "object_name": key,
                    "creatable": True,
                    "updatable": True,
                    "readable": True,
                    "deletable": True,
                    "view_all": True,
                    "modify_all": True
                }
            }
            r = requests.put(
                gl.url + ":7111/acl_admin/profile/AQACk5HxFIZ1DAAAdyuRdDW79BSwAwAA/object_level_access",
                data=json.dumps(data), headers=headers)
            print gl.url + ":7111/acl_admin/profile/AQACk5HxFIZ1DAAAdyuRdDW79BSwAwAA/object_level_access"
            print r, r.text
        except:
            continue
        """接下来为标准对象增加字段"""
        key_fields = list(schema.keys())
        for key_field in key_fields:
            print "第" + str(count) + "次请求"
            count += 1
            print "创建的列名：" + key_field
            data = schema[key_field]
            try:
                """r = requests.put(
                    gl.url + ":7020/api/v1.0/" + gl.tenant_name_test + "/" + key + "/meta/add",
                    data=json.dumps(data), headers=headers, verify=False)
                print r, r.text
                print gl.url + ":7020/api/v1.0/" + gl.tenant_name_test + "/" + key + "/meta/add" """
                data = {
                    "ent_id": "AQACk5HxFIZ1DAAAA48EyDS79BSsAwAA",
                    "profile_id": "AQACk5HxFIZ1DAAAdyuRdDW79BSwAwAA",
                    "access": {
                        "object_name": key,
                        "field_name": key_field,
                        "updatable": True,
                        "readable": True
                    }
                }
                r = requests.put(
                    gl.url + ":7111/acl_admin/profile/AQACk5HxFIZ1DAAAdyuRdDW79BSwAwAA/field_level_access",
                    data=json.dumps(data), headers=headers, verify=False)
                print gl.url + ":7111/acl_admin/profile/AQACk5HxFIZ1DAAAdyuRdDW79BSwAwAA/field_level_access"
                print r, r.text
            except:
                continue


def create_judge_profile_by_ci_profile():
    """通过ci环境美洽企业profile创建profile"""
    headers = {
        'x-token': gl.access_token_test,
        'content-type': gl.content_type
    }
    profile_list = get_profile_info_from_ci_meiqia_ent()
    for i in profile_list:
        print i, type(i)
        oLAs=[]
        fLAs=[]
        funcLAs=[]
        record_type_visibilities=[]
        profile_name = i["profile_name"]
        print profile_name
        if profile_name is "管理员":
            if (i.has_key("oLAs")):
                oLAs = i["oLAs"]
            else:
                oLAs = []
            if (i.has_key("fLAs")):
                fLAs = i["fLAs"]
            else:
                fLAs = []
            if (i.has_key("funcLAs")):
                funcLAs = i["funcLAs"]
            else:
                funcLAs = []
            if (i.has_key("record_type_visibilities")):
                record_type_visibilities = i["record_type_visibilities"]
            else:
                record_type_visibilities = []
        data = {
            "ent_id": "AQACk5HxFIZ1DAAAA48EyDS79BSsAwAA",
            "profile_id": "",
            "profile_name": profile_name,
            "oLAs": oLAs,
            "fLAs": fLAs,
            "access": funcLAs,    #功能权限
            "record_type_visibilities": record_type_visibilities,   #recoder_type
            "view_all_data": True,
            "modify_all_data": True
        }
        try:
            r = requests.post(gl.url + ":7111/acl_admin/profile", data=json.dumps(data), headers=headers)
            print r, r.text
        except:
            continue


def get_profile_info_from_ci_meiqia_ent():
    """从ci环境美洽企业获取详细Profile信息"""
    headers = {
        'x-token': gl.access_token,
        'content-type': gl.content_type
    }
    r = requests.get(gl.url + ":7111/acl_admin/profile", headers=headers)
    print r, r.text
    result = json.loads(r.text)
    profiles_list = result["profiles"]
    print profiles_list, type(profiles_list)
    return profiles_list


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


def get_all_meta_from_ci_env():
    """从集成环境获取meta"""
    headers = {
        'x-token': gl.access_token,
        'content-type': gl.content_type
    }
    data = "acl=true"
    print "请求数据：" + json.dumps(data)
    r = requests.get(gl.url + ":7010/api/v1.0/" + gl.tenant_name + "/all-metas?" + data, headers=headers)
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
