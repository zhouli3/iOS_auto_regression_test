# -*- coding: utf-8 -*-
"""解决'ascii' codec can't decode byte 0xe6"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import unittest
from TestAccount import TestAccountSignin
from TestTenant import TestTenant

r=unittest.result.TestResult()
#TestAccountSignin.TestAccountSignin(methodName='test_1_signin').run(result=r)
TestTenant.TestTenant(methodName='test_4_get_tenant_org').run(result=r)
#TestTenant.TestTenant(methodName='test_2_tenant_sign').run(result=r)
#TestTenant.TestTenant(methodName='test_5_get_account_orgs').run(result=r)
#TestTenant.TestTenant(methodName='test_8_tenant_refresh_token').run(result=r)
print r.failures,r.errors
