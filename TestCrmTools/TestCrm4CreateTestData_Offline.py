# -*- coding: utf-8 -*-
import unittest
import json
import requests
import uuid
import GVars

"""解决'ascii' codec can't decode byte 0xe6"""
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class TestCrm4CreateTestDataOffline(unittest.TestCase):
    """常用工具方法集合"""

    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."

    @classmethod
    def tearDownClass(cls):
        print "This tearDownClass() method only called once too."

    def test_001_create_object(self):
        """创建标准对象"""
        headers = {
            'x-token': GVars.access_token,
            'content-type': GVars.content_type
        }
        name = "CollectPayment"
        data = {
            "display_name": "CollectPayment",
            "description": "the description of CollectPayment."
        }
        print "请求数据：" + json.dumps(data)
        # meta创建和更新的端口是7020
        r = requests.post(GVars.url + ":7020/api/v1.0/" + GVars.tenant_name + "/" + name + "/meta",
                          data=json.dumps(data),
                          headers=headers)
        # r=requests.get(gl.url+"/api/v1.0/tenant-name/all-metas",params=data,headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["code"], 0)
        result = json.loads(r.text)
        self.assertIsNotNone(result["body"]["meta"])

    def test_002_create_object_fields(self):
        """在新建的标准对象下添加字段"""
        headers = {
            'x-token': GVars.access_token,
            'content-type': GVars.content_type
        }
        data = {"code": 0, "body": {
            "Address": {"name": "Address", "display_name": "客户详细地址", "type": "address", "nullable": True,
                        "searchable": True, "readable": True, "writable": True},
            "AffiliatedDepartment": {"name": "AffiliatedDepartment", "display_name": "所属部门", "type": "picklist",
                                     "options": {"list": {"all": {
                                         "options_value": ["北京直销", "上海直销", "西区直销", "西区渠道", "深圳直销", "线上资源直销", "研发部门",
                                                           "产品部门", "线上支持", "增值部门"]}}}, "nullable": True,
                                     "searchable": True, "readable": True, "writable": True},
            "ApplicationChannel": {"name": "ApplicationChannel", "display_name": "应用渠道", "type": "mpicklist",
                                   "options": {"list": {"all": {"options_value": ["PC", "WEB", "微信", "微博", "SDK"]}}},
                                   "nullable": True, "searchable": True, "readable": True, "writable": True},
            "BanExpiredTime": {"name": "BanExpiredTime", "display_name": "封禁失效时间", "type": "datetime", "nullable": True,
                               "searchable": True, "readable": True, "writable": True},
            "BannedUser": {"name": "BannedUser", "display_name": "封禁用户", "type": "lookup", "object_name": "User",
                           "delete_option": "SetNull", "nullable": True, "searchable": True, "readable": True,
                           "writable": True},
            "Competitor": {"name": "Competitor", "display_name": "之前应用的竞品", "type": "text", "nullable": True,
                           "searchable": True, "readable": True, "writable": True},
            "Description": {"name": "Description", "display_name": "备注", "type": "textarea", "nullable": True,
                            "searchable": True, "readable": True, "writable": True},
            "Fax": {"name": "Fax", "display_name": "传真", "type": "text", "nullable": True, "searchable": True,
                    "readable": True, "writable": True},
            "Industry": {"name": "Industry", "display_name": "行业", "type": "picklist",
                         "options": {"related": "IndustryCategory", "list": {"IT|通信|电子|互联网": {
                             "options_value": ["互联网", "电子商务", "金融", "企业服务", "教育", "文化娱乐", "游戏", "O2O", "硬件"]},
                             "交通运输物流仓储": {
                                 "options_value": ["物流/仓储", "交通/运输"]},
                             "农|林|牧|渔|其他": {
                                 "options_value": ["农/林/牧/渔", "跨领域经营",
                                                   "其他"]}, "商业服务": {
                                 "options_value": ["专业服务/咨询/财会/法律/(人力资源等)", "广告/会展/公关", "中介服务", "外包服务", "检验/检测/认证"]},
                             "房地产|建筑业": {
                                 "options_value": ["房地产/建筑/建材/工程",
                                                   "家具/室内设计/装饰装潢",
                                                   "物业管理/商业中心"]},
                             "政府|非盈利机构": {
                                 "options_value": ["政府/公共事业/非盈利机构",
                                                   "学术/科研"]},
                             "文体教育|工艺美术": {"options_value": ["教育/培训/院校",
                                                             "礼品/玩具工艺/美术收藏品奢侈品"]},
                             "文化|传媒|娱乐|体育": {
                                 "options_value": ["媒体/出版/影视/文化传播",
                                                   "娱乐/体育/休闲"]},
                             "服务业": {
                                 "options_value": ["医疗/护理/美容/保健/卫生服务",
                                                   "旅游/度假", "酒店/餐饮"]},
                             "生产|加工|制造": {"options_value": ["汽车/摩托车",
                                                            "教工制造（原料加/工模具）",
                                                            "印刷/包装/造纸",
                                                            "医药/生物工程",
                                                            "航空/航天与制造",
                                                            "大型设备/机电设备/重工业",
                                                            "仪器仪表及工业自动化",
                                                            "办公用品及设备",
                                                            "医疗设备/机械"]},
                             "能源|矿产|环保": {
                                 "options_value": ["能源/矿产/采掘/冶炼",
                                                   "电气/电力/水利",
                                                   "石油/石化/化工", "环保"]},
                             "贸易|批发|零售|租赁业": {
                                 "options_value": ["快速消费品（食品/饮料/烟酒/日化）",
                                                   "耐用消费品（服饰/纺织/皮革/家具/家电）",
                                                   "贸易/进出口", "零售/批发",
                                                   "租赁服务"]}, "金融业": {
                                 "options_value": ["基金/证券/期货/投资", "银行", "保险", "信托/担保/拍卖/典当"]}}}, "nullable": True,
                         "searchable": True, "readable": True, "writable": True},
            "IndustryCategory": {"name": "IndustryCategory", "display_name": "行业大类", "type": "picklist", "options": {
                "list": {"all": {
                    "options_value": ["IT|通信|电子|互联网", "金融业", "房地产|建筑业", "商业服务", "贸易|批发|零售|租赁业", "文体教育|工艺美术", "生产|加工|制造",
                                      "交通运输物流仓储", "服务业", "文化|传媒|娱乐|体育", "能源|矿产|环保", "政府|非盈利机构", "农|林|牧|渔|其他"]}}},
                                 "nullable": True, "searchable": True, "readable": True, "writable": True},
            "MeChatAdminLastLoginDate": {"name": "MeChatAdminLastLoginDate", "display_name": "客户最后登录时间",
                                         "type": "datetime", "nullable": True, "readable": True},
            "MeChatCurrentVersion": {"name": "MeChatCurrentVersion", "display_name": "当前方案", "type": "text",
                                     "nullable": True, "readable": True},
            "MeChatCustomerServiceAmount": {"name": "MeChatCustomerServiceAmount", "display_name": "客服数目",
                                            "type": "integer", "nullable": True, "readable": True},
            "MeChatPayAmount": {"name": "MeChatPayAmount", "display_name": "付费总额", "type": "currency", "nullable": True,
                                "readable": True},
            "MeChatRegisterDate": {"name": "MeChatRegisterDate", "display_name": "客户注册时间", "type": "datetime",
                                   "nullable": True, "readable": True},
            "MeChatSeats": {"name": "MeChatSeats", "display_name": "坐席数目", "type": "integer", "nullable": True,
                            "readable": True},
            "MeChatSession30Days": {"name": "MeChatSession30Days", "display_name": "最近30天对话数", "type": "integer",
                                    "nullable": True, "readable": True},
            "MeChatSession7Days": {"name": "MeChatSession7Days", "display_name": "最近7天对话数", "type": "integer",
                                   "nullable": True, "readable": True},
            "MeChatSessionToday": {"name": "MeChatSessionToday", "display_name": "今天对话数", "type": "integer",
                                   "nullable": True, "readable": True},
            "MeChatSessionYesterday": {"name": "MeChatSessionYesterday", "display_name": "昨天对话数", "type": "integer",
                                       "nullable": True, "readable": True},
            "MechatAdministratorAccount": {"name": "MechatAdministratorAccount", "display_name": "美洽超管邮箱",
                                           "type": "email", "nullable": True, "searchable": True, "readable": True,
                                           "writable": True},
            "MechatCustomerID": {"name": "MechatCustomerID", "display_name": "LiveChatTrackID", "type": "text",
                                 "nullable": True, "readable": True, "writable": True},
            "MechatExpirationDate": {"name": "MechatExpirationDate", "display_name": "美洽到期时间", "type": "datetime",
                                     "nullable": True, "searchable": True, "readable": True, "writable": True},
            "OwnDate": {"name": "OwnDate", "display_name": "开始持有时间", "type": "datetime", "searchable": True,
                        "readable": True, "writable": True},
            "OwnDays": {"name": "OwnDays", "display_name": "被持有天数", "type": "calculated", "related_type": "integer",
                        "expression": "DATETIME_SUB(TODAY(), OwnDate)/(24 * 3600 * 1000000000)", "nullable": True,
                        "searchable": True, "readable": True},
            "Phone": {"name": "Phone", "display_name": "电话", "type": "phone", "nullable": True, "searchable": True,
                      "readable": True, "writable": True},
            "PostalCode": {"name": "PostalCode", "display_name": "邮政编码", "type": "text", "nullable": True,
                           "searchable": True, "readable": True, "writable": True},
            "Rating": {"name": "Rating", "display_name": "客户级别", "type": "picklist",
                       "options": {"list": {"all": {"options_value": ["价高意低", "价低意高", "价低意低", "价高意高", "无需求"]}}},
                       "nullable": True, "searchable": True, "readable": True, "writable": True},
            "Source": {"name": "Source", "display_name": "客户来源", "type": "picklist",
                       "options": {"list": {"all": {"options_value": ["广告", "会议", "搜索引擎", "客户介绍", "自主开发", "其他"]}}},
                       "nullable": True, "searchable": True, "readable": True, "writable": True},
            "Status": {"name": "Status", "display_name": "状态", "type": "picklist",
                       "options": {"list": {"all": {"options_value": ["自建", "未领取", "已领取", "已签约", "已冻结", "已废弃"]}}},
                       "nullable": True, "searchable": True, "default_value": {"value": "未领取"}, "readable": True,
                       "writable": True},
            "TransferDate": {"name": "TransferDate", "display_name": "预计改派时间", "type": "datetime", "nullable": True,
                             "searchable": True, "readable": True, "writable": True},
            "Type": {"name": "Type", "display_name": "客户类型", "type": "picklist",
                     "options": {"list": {"all": {"options_value": ["中小", "KA"]}}}, "nullable": True,
                     "searchable": True, "readable": True, "writable": True},
            "WeChat": {"name": "WeChat", "display_name": "微信", "type": "text", "nullable": True, "searchable": True,
                       "readable": True, "writable": True},
            "WeChatPublicAccount": {"name": "WeChatPublicAccount", "display_name": "微信公众账号", "type": "text",
                                    "nullable": True, "searchable": True, "readable": True, "writable": True},
            "Website": {"name": "Website", "display_name": "公司网址", "type": "url", "nullable": True, "searchable": True,
                        "readable": True, "writable": True},
            "created_at": {"name": "created_at", "display_name": "创建时间", "type": "datetime", "readable": True},
            "created_by": {"name": "created_by", "display_name": "创建人", "type": "lookup", "object_name": "User",
                           "delete_option": "Restrict", "readable": True},
            "id": {"name": "id", "display_name": "ID", "type": "object_id", "readable": True},
            "name": {"name": "name", "display_name": "客户名称", "type": "text", "index": True, "unique": True,
                     "searchable": True, "readable": True, "writable": True},
            "owner": {"name": "owner", "display_name": "所有者", "type": "lookup", "object_name": "User",
                      "delete_option": "Restrict", "readable": True},
            "record_type": {"name": "record_type", "display_name": "记录类型", "type": "picklist",
                            "options": {"list": {"all": {"options_value": ["main"]}}},
                            "default_value": {"value": "main"}, "readable": True, "writable": True},
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
                    GVars.url + ":7020/api/v1.0/" + GVars.tenant_name + "/" + GVars.meta_name + "/meta/add",
                    data=json.dumps(data), headers=headers, verify=False)
                print r, r.text
                print GVars.url + ":7020/api/v1.0/" + GVars.tenant_name + "/" + GVars.meta_name + "/meta/add"
            except:
                continue

    def test_002_create_object_fields(self):
        """在新建的标准对象下添加字段"""
        headers = {
            'x-token': GVars.access_token,
            'content-type': GVars.content_type
        }
        data = {"code": 0, "body": {
            "Address": {"name": "Address", "display_name": "地址", "type": "address", "nullable": True,
                        "searchable": True, "readable": True, "writable": True},
            "AffiliatedDepartment": {"name": "AffiliatedDepartment", "display_name": "所属部门", "type": "picklist",
                                     "options": {"list": {"all": {
                                         "options_value": ["北京直销", "上海直销", "西区直销", "西区渠道", "深圳直销", "线上资源直销", "研发部门",
                                                           "产品部门", "线上支持", "增值部门"]}}}, "nullable": True,
                                     "searchable": True, "readable": True, "writable": True},
            "CampaignID": {"name": "CampaignID", "display_name": "相关市场活动", "type": "lookup", "object_name": "Campaign",
                           "delete_option": "NoAction", "nullable": True, "searchable": True, "readable": True,
                           "writable": True},
            "Company": {"name": "Company", "display_name": "公司名称", "type": "text", "nullable": True, "searchable": True,
                        "readable": True, "writable": True},
            "CreatedAt": {"name": "CreatedAt", "display_name": "线索生成日期", "type": "datetime", "nullable": True,
                          "searchable": True, "readable": True, "writable": True},
            "CreatedBy": {"name": "CreatedBy", "display_name": "线索创建人（cs专用字段）", "type": "picklist", "options": {
                "list": {"all": {"options_value": ["崔晓慧", "刘佳", "王进宝", "刘奥", "李贵颖", "郭元元", "冯硕"]}}}, "nullable": True,
                          "searchable": True, "readable": True, "writable": True},
            "Department": {"name": "Department", "display_name": "部门", "type": "text", "nullable": True,
                           "searchable": True, "readable": True, "writable": True},
            "Description": {"name": "Description", "display_name": "备注", "type": "textarea", "nullable": True,
                            "searchable": True, "readable": True, "writable": True},
            "Email": {"name": "Email", "display_name": "电子邮件", "type": "email", "nullable": True, "searchable": True,
                      "readable": True, "writable": True},
            "Gender": {"name": "Gender", "display_name": "性别", "type": "picklist",
                       "options": {"list": {"all": {"options_value": ["男", "女"]}}}, "nullable": True,
                       "searchable": True, "readable": True, "writable": True},
            "Industry": {"name": "Industry", "display_name": "行业", "type": "picklist",
                         "options": {"related": "IndustryCategory", "list": {"IT|通信|电子|互联网": {
                             "options_value": ["互联网", "电子商务", "金融", "企业服务", "教育", "文化娱乐", "游戏", "O2O", "硬件"]},
                                                                             "交通运输物流仓储": {
                                                                                 "options_value": ["物流/仓储", "交通/运输"]},
                                                                             "农|林|牧|渔|其他": {
                                                                                 "options_value": ["农/林/牧/渔", "跨领域经营",
                                                                                                   "其他"]}, "商业服务": {
                                 "options_value": ["专业服务/咨询/财会/法律/(人力资源等)", "广告/会展/公关", "中介服务", "外包服务", "检验/检测/认证"]},
                                                                             "房地产|建筑业": {
                                                                                 "options_value": ["房地产/建筑/建材/工程",
                                                                                                   "家具/室内设计/装饰装潢",
                                                                                                   "物业管理/商业中心"]},
                                                                             "政府|非盈利机构": {
                                                                                 "options_value": ["政府/公共事业/非盈利机构",
                                                                                                   "学术/科研"]},
                                                                             "文体教育|工艺美术": {"options_value": ["教育/培训/院校",
                                                                                                             "礼品/玩具工艺/美术收藏品奢侈品"]},
                                                                             "文化|传媒|娱乐|体育": {
                                                                                 "options_value": ["媒体/出版/影视/文化传播",
                                                                                                   "娱乐/体育/休闲"]},
                                                                             "服务业": {
                                                                                 "options_value": ["医疗/护理/美容/保健/卫生服务",
                                                                                                   "旅游/度假", "酒店/餐饮"]},
                                                                             "生产|加工|制造": {"options_value": ["汽车/摩托车",
                                                                                                            "教工制造（原料加/工模具）",
                                                                                                            "印刷/包装/造纸",
                                                                                                            "医药/生物工程",
                                                                                                            "航空/航天与制造",
                                                                                                            "大型设备/机电设备/重工业",
                                                                                                            "仪器仪表及工业自动化",
                                                                                                            "办公用品及设备",
                                                                                                            "医疗设备/机械"]},
                                                                             "能源|矿产|环保": {
                                                                                 "options_value": ["能源/矿产/采掘/冶炼",
                                                                                                   "电气/电力/水利",
                                                                                                   "石油/石化/化工", "环保"]},
                                                                             "贸易|批发|零售|租赁业": {
                                                                                 "options_value": ["快速消费品（食品/饮料/烟酒/日化）",
                                                                                                   "耐用消费品（服饰/纺织/皮革/家具/家电）",
                                                                                                   "贸易/进出口", "零售/批发",
                                                                                                   "租赁服务"]}, "金融业": {
                                 "options_value": ["基金/证券/期货/投资", "银行", "保险", "信托/担保/拍卖/典当"]}}}, "nullable": True,
                         "searchable": True, "readable": True, "writable": True},
            "IndustryCategory": {"name": "IndustryCategory", "display_name": "行业大类", "type": "picklist", "options": {
                "list": {"all": {
                    "options_value": ["IT|通信|电子|互联网", "金融业", "房地产|建筑业", "商业服务", "贸易|批发|零售|租赁业", "文体教育|工艺美术", "生产|加工|制造",
                                      "交通运输物流仓储", "服务业", "文化|传媒|娱乐|体育", "能源|矿产|环保", "政府|非盈利机构", "农|林|牧|渔|其他"]}}},
                                 "nullable": True, "searchable": True, "readable": True, "writable": True},
            "LeadsSource": {"name": "LeadsSource", "display_name": "线索来源", "type": "picklist",
                            "options": {"list": {"all": {"options_value": ["搜索引擎", "广告", "展会", "客户介绍", "自主开发", "其他"]}}},
                            "nullable": True, "searchable": True, "readable": True, "writable": True},
            "MeChatAdminLastLoginDate": {"name": "MeChatAdminLastLoginDate", "display_name": "客户最后登录时间",
                                         "type": "datetime", "nullable": True, "readable": True, "writable": True},
            "MeChatCurrentVersion": {"name": "MeChatCurrentVersion", "display_name": "当前方案", "type": "text",
                                     "nullable": True, "readable": True, "writable": True},
            "MeChatCustomerServiceAmount": {"name": "MeChatCustomerServiceAmount", "display_name": "客服数目",
                                            "type": "integer", "nullable": True, "readable": True, "writable": True},
            "MeChatPayAmount": {"name": "MeChatPayAmount", "display_name": "付费总额", "type": "currency", "nullable": True,
                                "readable": True, "writable": True},
            "MeChatRegisterDate": {"name": "MeChatRegisterDate", "display_name": "客户注册时间", "type": "datetime",
                                   "nullable": True, "readable": True, "writable": True},
            "MeChatSeats": {"name": "MeChatSeats", "display_name": "坐席数目", "type": "integer", "nullable": True,
                            "readable": True, "writable": True},
            "MeChatSession30Days": {"name": "MeChatSession30Days", "display_name": "最近30天对话数", "type": "integer",
                                    "nullable": True, "readable": True, "writable": True},
            "MeChatSession7Days": {"name": "MeChatSession7Days", "display_name": "最近7天对话数", "type": "integer",
                                   "nullable": True, "readable": True, "writable": True},
            "MeChatSessionToday": {"name": "MeChatSessionToday", "display_name": "今天对话数", "type": "integer",
                                   "nullable": True, "readable": True, "writable": True},
            "MeChatSessionYesterday": {"name": "MeChatSessionYesterday", "display_name": "昨天对话数", "type": "integer",
                                       "nullable": True, "readable": True, "writable": True},
            "MechatAccountID": {"name": "MechatAccountID", "display_name": "美洽账号", "type": "lookup",
                                "object_name": "MechatAccount", "delete_option": "NoAction", "nullable": True,
                                "searchable": True, "readable": True, "writable": True},
            "MechatAdministratorAccount": {"name": "MechatAdministratorAccount", "display_name": "美洽超管邮箱",
                                           "type": "email", "nullable": True, "readable": True, "writable": True},
            "MechatCustomerID": {"name": "MechatCustomerID", "display_name": "LiveChatTrackID", "type": "text",
                                 "nullable": True, "readable": True, "writable": True},
            "MechatExpirationDate": {"name": "MechatExpirationDate", "display_name": "美洽到期时间", "type": "datetime",
                                     "nullable": True, "readable": True, "writable": True},
            "MobilePhone": {"name": "MobilePhone", "display_name": "手机", "type": "phone", "nullable": True,
                            "searchable": True, "readable": True, "writable": True},
            "Phone": {"name": "Phone", "display_name": "电话", "type": "phone", "nullable": True, "searchable": True,
                      "readable": True, "writable": True},
            "PostalCode": {"name": "PostalCode", "display_name": "邮政编码", "type": "text", "nullable": True,
                           "searchable": True, "readable": True, "writable": True},
            "QQ": {"name": "QQ", "display_name": "QQ", "type": "text", "nullable": True, "searchable": True,
                   "readable": True, "writable": True},
            "RecommendedBy": {"name": "RecommendedBy", "display_name": "推荐人", "type": "lookup", "object_name": "User",
                              "delete_option": "NoAction", "nullable": True, "searchable": True, "readable": True,
                              "writable": True},
            "Status": {"name": "Status", "display_name": "跟进状态", "type": "picklist",
                       "options": {"list": {"all": {"options_value": ["未处理", "已联系", "已转换", "关闭"]}}}, "searchable": True,
                       "default_value": {"value": "未处理"}, "readable": True, "writable": True},
            "Title": {"name": "Title", "display_name": "职务", "type": "text", "nullable": True, "searchable": True,
                      "readable": True, "writable": True},
            "WeChat": {"name": "WeChat", "display_name": "微信", "type": "text", "nullable": True, "searchable": True,
                       "readable": True, "writable": True},
            "created_at": {"name": "created_at", "display_name": "创建时间", "type": "datetime", "readable": True},
            "created_by": {"name": "created_by", "display_name": "创建人", "type": "lookup", "object_name": "User",
                           "delete_option": "Restrict", "readable": True},
            "id": {"name": "id", "display_name": "ID", "type": "object_id", "readable": True},
            "name": {"name": "name", "display_name": "姓名", "type": "text", "index": True, "searchable": True,
                     "readable": True, "writable": True},
            "owner": {"name": "owner", "display_name": "所有者", "type": "lookup", "object_name": "User",
                      "delete_option": "Restrict", "readable": True},
            "record_type": {"name": "record_type", "display_name": "记录类型", "type": "picklist",
                            "options": {"list": {"all": {"options_value": ["main"]}}},
                            "default_value": {"value": "main"}, "readable": True, "writable": True},
            "system_mod_stamp": {"name": "system_mod_stamp", "display_name": "系统修改时间", "type": "datetime",
                                 "readable": True},
            "territory_id": {"name": "territory_id", "display_name": "territory_id", "type": "external_id",
                             "nullable": True, "index": True, "readable": True, "writable": True},
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
                    GVars.url + ":7020/api/v1.0/" + GVars.tenant_name + "/" + GVars.meta_name + "/meta/add",
                    data=json.dumps(data), headers=headers, verify=False)
                print r, r.text
                print GVars.url + ":7020/api/v1.0/" + GVars.tenant_name + "/" + GVars.meta_name + "/meta/add"
            except:
                continue

    def test_003_add_profile_OLA(self):
        """添加meta权限到profile，标准对象授权"""
        headers = {
            'x-token': GVars.access_token,
            'content-type': GVars.content_type
        }
        data = {
            "ent_id": "00000000000000000000000000000000",
            "profile_id": "AQACd5VVkc56EgAAlRN1m4BW0BQBAAAA",
            "access": {
                "object_name": GVars.meta_name,
                "creatable": True,
                "updatable": True,
                "readable": True,
                "deletable": True,
                "view_all": True,
                "modify_all": True
            }
        }
        r = requests.put(
            GVars.url + ":7111/acl_admin/profile/AQACd5VVkc56EgAAlRN1m4BW0BQBAAAA/object_level_access",
            data=json.dumps(data), headers=headers, verify=False)
        print GVars.url + ":7111/acl_admin/profile/AQACd5VVkc56EgAAlRN1m4BW0BQBAAAA/object_level_access"
        print r, r.text

    def test_004_add_profile_FLA(self):  # 字段授权
        headers = {
            # 'x-token': gl.access_token_lt_166,
            'x-token': GVars.access_token,
            'content-type': GVars.content_type
        }
        r = requests.get(
            GVars.url + ":7010/api/v1.0/" + GVars.tenant_name + "/" + GVars.meta_name + "/meta/schema",
            headers=headers, verify=False)
        print r, r.text
        result = json.loads(r.text)
        GVars.clonum_dict = result["body"]
        keys = list(GVars.clonum_dict.keys())
        for key in keys:
            print key
            data = {
                "ent_id": "00000000000000000000000000000000",
                "profile_id": "AQACd5VVkc56EgAAlRN1m4BW0BQBAAAA",
                "access": {
                    "object_name": GVars.meta_name,
                    "field_name": key,
                    "updatable": True,
                    "readable": True
                }
            }
            headers = {
                # 'x-token': gl.access_token_lt_166,
                'x-token': GVars.access_token,
                'content-type': GVars.content_type
            }
            r = requests.put(
                GVars.url + ":7111/acl_admin/profile/AQACd5VVkc56EgAAlRN1m4BW0BQBAAAA/field_level_access",
                data=json.dumps(data), headers=headers, verify=False)
            print GVars.url + ":7111/acl_admin/profile/AQACd5VVkc56EgAAlRN1m4BW0BQBAAAA/field_level_access"
            print r, r.text

    def test_005_assign_profile_to_point_user(self):
        """授权到指定用户"""
        headers = {
            'x-token': GVars.access_token,
            'content-type': GVars.content_type
        }
        data = {
            "ent_id": "00000000000000000000000000000000",
            "profile_id": "AQACd5VVkc56EgAAlRN1m4BW0BQBAAAA",
            "user_id": "AQACd5VVkc7RCAAALgrgmrnF6BSWKwAA"
            # AQACd5VVkc7RCAAALgrgmrnF6BSWKwAA   AQACd5VVkc7RCAAAucWwesDL7BR7QAAA
        }
        r = requests.post(
            GVars.url + "/acl/acl_admin/profile/AQACd5VVkc7RCAAA1sIDurnF6BSXKwAA/user",
            data=json.dumps(data), headers=headers, verify=False)
        print GVars.url + "/acl/acl_admin/profile/AQACd5VVkc7RCAAA1sIDurnF6BSXKwAA/user"
        print r, r.textn

    def test_006_upload_layout_json(self):
        """上传layout使用的json"""
        headers = {
            'x-token': GVars.access_token,
            'content-type': GVars.content_type
        }
        jsonStr = GVars.layout_json_temp
        # "pwd": "CBqeJFFjZqjjUR6fFNzjFJjJ",
        # "userid": "zhangsongshi"
        data = {
            "json": json.dumps(jsonStr),
            "pwd": "1234567",
            "userid": "admin"
        }
        print "请求参数：" + json.dumps(data)
        r = requests.post(GVars.url + ":8555/abc", data=json.dumps(data), headers=headers)
        print r, r.text
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["error"], False)
        self.assertEqual(r.json()["message"], "success")


GVars.suites.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCrm4CreateTestDataOffline))
