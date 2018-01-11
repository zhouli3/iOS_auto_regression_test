# -*- coding: utf-8 -*-
#import xlrd
import json
import os
import ConfigParser as cparser
import csv
import gl

base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + "/GlobalVariables/TestData.ini"
cf = cparser.ConfigParser()
cf.read(file_path)
# print file_path

"""从配置文件读取用户名密码"""


def get_login_username_from_config_file(self):
    """返回登录用户名 """
    login_username = cf.get("loginUser", "phoneNo")
    return login_username


def get_login_username_password_from_config_file(self):
    """返回登录用户密码"""
    login_user_password = cf.get("loginUser", "password")
    return login_user_password


def get_fields_data_from_csv_file(self):
    """从CSV文件中读取字段信息"""
    datas = []
    # 读取每行数据
    reader = csv.DictReader(open('D:/work/Product.csv', 'rb'))
    for line in reader:
        #print line
        replace_json_bool_items_and_del_null_items(self,line)  #删除空值的元素，并将bool值转化为请求可识别的值
        format_json_string_default_value(self,line)
        #line = json.dumps(line)
        #print line
        datas.append(line)
    print "读取到的CSV文件中的数据："+json.dumps(datas)
    return datas

    # for item in line:
    #  print item
def replace_json_bool_items_and_del_null_items(self,dict):
    dict_keys = list(dict.keys())
    for key in dict_keys:
        if (dict[key] == ""):
            del dict[key]
        else:
            if (dict[key] == "true"):
                dict[key] = True
            else:
                if (dict[key] == "false"):
                    dict[key] = False
    return dict

def format_json_string_default_value(self,dict):
    """将json中的默认值选项格式化"""
    print dict
    if(dict.has_key("default_value")):
        value = dict["default_value"]
        dict["default_value"] = {"value": value}
    return dict

def load_json_file(self,json_file_name):
    """读取json文件"""
    with open(base_dir+"/GlobalVariables/"+json_file_name) as json_file:
        data = json.load(json_file)
        return data

def write_json_file(self,json_file_name,write_data):
    """读取json文件"""
    with open(base_dir+"/GlobalVariables/"+json_file_name, 'w') as json_file:
        json_file.write(json.dumps(write_data))

