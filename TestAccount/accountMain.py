import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("..")

from GlobalVariables import gl

"""add test sutie,import order is run order"""
import TestAccountSignup
import TestAccountSignin
import TestAccountResetPwd

from HTMLTestRunner import HTMLTestRunner
import unittest

if __name__ == '__main__':
    with open('HTMLReport.html', 'w') as f:
        runner = HTMLTestRunner(stream=f,
                                title='Test Report',
                                description='generated by HTMLTestRunner.',
                                verbosity=2
                                )
        runner.run(gl.suite)