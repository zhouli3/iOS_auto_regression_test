# -*- coding: utf-8 -*-

import unittest
import GetParamFromFile as gpff
import random

suite = unittest.TestSuite()
#http://10.102.1.64      10.102.2.133
url = "http://10.102.1.64"
#url = "http://10.102.2.14"
access_token_lt_166 = "AUECAGtY8FkAADAxYmM1NGE3OTVlNzlkZWY3MzhhNWUxZmFlMGVjMjI5MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDA5s0xQ8_2efkkKc3SuVJ3M76Ot6pWTZbEetr07YjRqJPGN8yLi8q3lp0HUw5B10rm4nIeodQu6c5sbstXgXgFU"
url_online = "https://crm.meiqia.com"
url_online = "http://10.100.250.164"
access_token_online = "AQdSCinUClp4AEFRQUNkNVZWa2M3UkNBQUF1Y1d3ZXNETDdCUjdRQUFBQVFBQ2Q1VlZrYzdSQ0FBQTZ2WE9tcm5GNkJTVkt3QUHmA-7Vh7BTyO0G5HEmv5nta9r4BIn21TtcsJ6Tofyzf9O74kuxbtKcuNPmH7N4AlzKrcBzwUtCcsENGQidSugY"
online_meta_name = "Opportunity"     #Opportunity
online_tenant_name = "test企业test001"


captcha_token = ""#图形验证码token
captcha_value = ""#图形验证码
verify_code = ""#验证码
account_token = "AQUAAHHXmg_cWo7j9IxMYb6uroby9MOnw636QDeXgwy26C5-Krz8XwCZP-_rJ6nO193fiz70_JIjEeGDO05qyVYNkFSUegJa0AJBUUFHc1NYMnM3QkNEUUFBUkdJajFzSC05QlFBQUFBQXdlYg=="
# ci
access_token_point_2 = "AZABAE7b5VkAAEFRQUNkNVZWa2M3dUNBQUEzWW1fVjdUUjJ4Ulcyd0VBMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDDcaL3_AaF4dXDGN6_1H9fMGN6xz-WdCkWRTW2AiX8Qiywe5AAMcoMcePuIAqlZlJht4jhpEhk5kg2VUOUNkWa8"
access_token_point_3 = "AY4BAIva5VkAAEFRQUMxMmhTYktyRkNBQUFCZW41RkJnbTRCUi1BZ0FBMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDCmqR95NifNvpOonFcDuKe0v782oLdBpY51sCNYU9nH7UziC2rU_amQW7LHY9-gaP4ytlxDoDizy7u0WYJoZLGB"
access_token = "AagAAK3oVVp4AEFRQUNrNUh4RklZRkRBQUFXYXI0TmZrZ194VDhBUUFBMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAZz9wL7SNoPBtzoz-sbU4_W6xcogWcr1ipHGKFHosL9MHu6LEHE2SuVBzlr1UjCLElWRhyneGDzSdldU7ytGCG"
#access_token = "AbsFAK5wCVoAAEFRQUNrNUh4RklaMURBQUFaX0VheURTNzlCU3RBd0FBQVFBQ2s1SHhGSVoxREFBQUE0OEV5RFM3OUJTc0F3QUHL3NoEB80ks0xgy9KOE02EoXBmZNR7M4Ef_enpFCk59lcV72y0UCKrGFKnymN_p8THPBYuZW0k33HHEr30gmnf"
access_token_test = "AT4CAA75CFp4AEFRQUNrNUh4RklaMURBQUFaX0VheURTNzlCU3RBd0FBQVFBQ2s1SHhGSVoxREFBQUE0OEV5RFM3OUJTc0F3QUElk-W3faRfOT6upHq2vfCGeKLEYVjLAv7Zb8j6euGoY95yQw3_Zm98S-AD-TzpMntOkco9EILYqSpPoRhsWe_s"
# lt
#access_token = "AX8BAKlJ8FkAADAxYmM1NGE3OTVlNzlkZWY3MzhhNWUxZmFlMGVjMjI5MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDBM7zTTiEBcn6xivo5LoLjVfbpTAojuxi-fOy8LY-lq4YFqh6DxHuawIIx4YC9ureHtW-q_hss1nFEvgpgX01LM"
#access_token = "ASgAAOhgCVp4AEFRQUNrNUh4RkliMERBQUF2NXdFVExlZDhoUmxCQUFBQVFBQ2s1SHhGSWIwREFBQUoxZnlTN2VkOGhSa0JBQUGLtpXbYojigHEQuIhRv3XWfF0K_6UZgVEZODv2E4i8_Hki6sL9QXbWxm3RC4M8pyGzgDIgGxokjTaFUf5blFZU"
#access_token_point_2 = "AQ4AACot4FkAAEFRQUNkNVZWa2M3dUNBQUEzWW1fVjdUUjJ4Ulcyd0VBMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDBNPfRMF-YxoIPxy5K4E0Bot4qVzJeJRY5QvZf30Vy18HTtSRqcX2hstDgd-qHqdrB60RzG4u_tQbvRusYh-s8O"
#access_token_point_3 = "AQwAAHcs4FkAAEFRQUMxMmhTYktyRkNBQUFCZW41RkJnbTRCUi1BZ0FBMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDDEeD-9cV5_Jd1CAjTkbvquqaS4OM6t5ElvWDHRB35_6l3R6xq56F0gfPturX3yTqNO0J_Dn7dYuH9hddOMQUzR"
refresh_token = ""
tenant_id = ""
tenant_name = "meiqia"   #test企业test   meiqia
tenant_name_test = "测试专用企业勿动"   #test企业test   meiqia
#meta相关

meta_name = "User"    #Leads  Opportunity   Refund    Invoice  Recharge  Contract   PriceBook  PriceBookItem   object_name=MechatAccount   Campaign
meta_line_name = "sgk_test_line"
meta_validation_name = "测试validation名字"
meta_selectfilter_name = ""

#view filter 相关
view_filter_id = ""
view_filter_user = ""

#审批 模板/过程 相关
object_approvals_template_name = "Account"
object_approvals_template_id = "AQAC12hSbKqGKQAAkvjFG5PQ4xTAGQAA"   #AQAC12hSbKqGKQAAkvjFG5PQ4xTAGQAA
object_date_id = "AQACd5VVkc7RCAAAyQjQcu1N7hTnSwAA"    #标准对象数据id   AQAC12hSbKqGKQAABHNVWS2Z4xRDGAAA     AQACd5VVkc7RCAAAyQjQcu1N7hTnSwAA
approval_record_id = "AQAGifYUnayBDAAAxj0kmw5o7BQPAAAA"  #审批记录的id
approvals_template_id = "AQACk5HxFIaxDAAAmtJ6-iCC9hRVBQAA"    #AQACd5VVkc7RCAAAtv6k8ZpP7hRPTAAA   AQACd5VVkc7RCAAAqUHnJSpM7hRmSwAA    AQAC12hSbKqGKQAAkvjFG5PQ4xTAGQAA
#Id=AQACd5VVkc7RCAAAtv6k8ZpP7hRPTAAA(first response)   AQACd5VVkc7RCAAAqUHnJSpM7hRmSwAA  CI:Id=AQAC12hSbKqGKQAAkvjFG5PQ4xTAGQAA
approvals_template_id_reject = "AQAC12hSbKrFCAAAf_1qurz63RRqAAAA"
approvals_process_id = ""
approvals_listtype=["Submit","Vote","Carboncopy","OwnerAws","Approved"]
approvals_run_id = []    #AQAC12hSbKqGKQAA_xz-5Orm4xT7HAAA
approvals_point_id = "1"
approvals_point_can_edit_fields = ["Competitor","OtherService"]
approvals_point_memberid = []   #AQAGifYUnayBDAAA1shSRKXB7BSAAAAA
approvals_point_touid = "AQAC12hSbKqGKQAAfs7klqTi4xSVGwAA"   #AQAGifYUnayBDAAA_vOicffM7BS9AAAA  01bc54a795e79def738a5e1fae0ec229

#搜索相关
global_search_keyword = "meiqia"
object_for_search = "Leads"
limit_for_search = "50"
offset_for_search = "9"

#海相关
territory_limit = "10"
territory_offset = "1"
territory_model_id = ""
territory_id = ""
territory_record_id = ""

#meta actions相关
action_merge_data_commit_name = "merge_data_commit"
action_merge_data_pre_name = "merge_data_pre"
action_merge_data_pre_mergeid = []
action_merge_data_pre_deleteid = []
action_merge_data_commit_mergeid = []
action_merge_data_commit_deleteid = []
action_leads_to_account_and_contact_pre_name = "leads_to_account_and_contact_pre"
action_leads_to_account_and_contact_commit_name = "leads_to_account_and_contact_commit"

#data相关
data_name = []
data_id = []  #AQACk5HxFIb0DQAAKStOdbrY6xS-CwAA  AQACk5HxFIb0DQAANVcukPTW6xQ5CwAA
data_version = []


new_org_name = "neworg"

#header
content_type = "application/json"

#登陆用的账户密码
login_username = gpff.get_login_username_from_config_file(gpff)
login_user_password = gpff.get_login_username_password_from_config_file(gpff)
login_username_new_password = "Aa12345678"


#LayOut流程相关
layout_jsonStr = ""
layout_tenantname = "meiqia"           #test企业test001
layout_tenantid = "00000000000000000000000000000000"     #  AQACd5VVkc7RCAAA6vXOmrnF6BSVKwAA
layout_env_IP = "10.102.1.64"
layout_env_token = ""
#"ATQAAGd45VkAADAxYmM1NGE3OTVlNzlkZWY3MzhhNWUxZmFlMGVjMjI5MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDBryL984UYZPsub0ES9aSdnRn45aUlkXvwuRLeCnmezHUiM5wrOqKegfxEiDO-H7pQ4EriUsFcZRnllAIQ5kCBe"
layout_new_fields = []
layout_json_temp = gpff.load_json_file(gpff,"layout.json")


layout_jsonStr = ""
layout_tenantname = "test企业test001"           #test企业test001
layout_env_IP_Online = "10.100.250.22"
layout_env_token = ""
#"ATQAAGd45VkAADAxYmM1NGE3OTVlNzlkZWY3MzhhNWUxZmFlMGVjMjI5MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDBryL984UYZPsub0ES9aSdnRn45aUlkXvwuRLeCnmezHUiM5wrOqKegfxEiDO-H7pQ4EriUsFcZRnllAIQ5kCBe"
layout_new_fields = []
layout_json_temp = gpff.load_json_file(gpff,"layout_test_ent_online.json")


#judge 相关
profile_id = "AQACd5VVkc7RCAAA1sIDurnF6BSXKwAA"
clonum_dict = {}
acl_group_id = "AQAGF0c59nzECAAAHJ2wAng18xQFAAAA"   #(备用)AQAGF0c59nzECAAAexg-a-4w8xQAAAAA
acl_group_name = "SgkTestGroup1102001"   #SgkTestGroup1102002(备用)
acl_group_member_type = 1
acl_group_member_id = "01bc54a795e79def738a5e1fae0ec229"
acl_group_ent_id = "00000000000000000000000000000000"
test_data_4_test = ""

#邀请相关
user_id = ""#当前登录企业下的user_id
invitation_id = ""#被邀请id
invitation_phoneNo = "+86 13601099798"#被邀请账号
invitation_pwd = "@12345678"

#mpay相关
mpay_tenant_id = "14f69e13c56b8cf0c31a0003a0000157"
mpay_customer_id = "14f69e13c56b8cf0c31a0003a0000157"  #14f69e13c56b8cf0c31a0003a0000157   14f2e5cd8b4ba013a7220005b0000159
mpay_customer_id_online = "14f33e37d07c10813ddf0000a000010f"
mpay_customer_type = "+86 17711111111"
mpay_customer_phone = "+86 17711111111"
mpay_customer_name = "Jack Jan"
mpay_customer_email = "test@meiqia.com"
mpay_customer_weixin = "Jack1234"
mpay_customer_external_id = "00000000000000000000000000000000"
mpay_account_id_shoukuan = "14f2e5f1c779f9c4fe120006k0000158"   #14f2e5f1c779f9c4fe120006k0000158
mpay_account_id_shoukuan_online = "14f5b27ca0c72a9137500004k0000153"
mpay_account_id_fukuan = "14f2e5f1cdd08d6265d10007m0000150"
mpay_account_related_customer_id = "14f2d6da8f2c8f9d369e0000b0000100"
mpay_account_related_account_type = "ALI"
mpay_account_related_account_id = "zhangsan123"
mpay_bill_id = "2017110211500248ef001e100000015a"
mpay_bill_id_online = "20171102183150084400041000000104"
mpay_bill_account_id_mq_type = "14f2ebdd2494d8d5cf1c0010k000015c"
mpay_bill_path = "TENANT_TO_MQ"   #TENANT_TO_MQ  TENANT_ACCOUNT_TO_TENANT


#file_service相关
file_service_version = "v1"
folder_id = "4a6fe88c-f66c-42b2-b34e-b80dfd8211f2"   #"4a6fe88c-f66c-42b2-b34e-b80dfd8211f2"(集成)  30326048-d7ea-4239-880c-023aacbec157
folder_id_online = "ba4c5ea3-4134-4889-9c71-e8873fa6cbff"


#boss相关
X_Meiqia_BOSS_Token = "zYbEdW1MW3ffUvvLDkaG7ind0hr9xJEciWEtFnT-FsMyF34sE3cX2IQ5rZ9cq1ltp724_dxGVVbcH2cEN-3W2QAAAAFaVd5SAAAAeA=="
url_test = "http://10.102.1.244"
account_id = "1" #查询单个账户时所需账户的account_id
page_num = 0 #查询所有账户中page_num
size = 3 #查询所有账户中size参数
app_id = 3 #APP url app_id
code = random.randint(1, 1000000000)#action url code
action_code = 366410310 #创建action时返回的的code
order_id = 97 #创建订单时的id
#customer_tenant_id的集成环境和线上环境必须为以命名为集成和线上的两个id，其他租户id不可用（线上数据请谨慎操作）
customer_tenant_id = "1" #联调环境
customer_tenant_id_shaxiang = "37220" #集成环境
customer_tenant_id_online = "49196" #线上环境
suite_id = 13


#job-service相关
cron_id = ""
job_id = ""
script = "var time = import(\"time\");var fmt = import(\"fmt\");sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));sh.Log(fmt.Sprintf(\"%s\", time.Now()));println(\"test\")"

#接口版本
api_version = "v1.0"
