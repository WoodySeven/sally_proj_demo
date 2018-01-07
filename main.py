#!/usr/bin/env python
import HTMLTestRunner
import unittest
import time
from testcase.cases_login_logout.admin_login_logout import BugfreeAdminLoginLogout


if __name__ == '__main__':
    suite = unittest.TestSuite()     # 新建一个suite，测试套件
    loader = unittest.TestLoader()   # 新建一个加载器，自定义的方式把测试用例加载到suite里
    suite.addTests(loader.loadTestsFromTestCase(BugfreeAdminLoginLogout))  # 把测试类所有的方法都加载到suite里
    # unittest.TextTestRunner(verbosity=2).run(suite) # unittest运行suite
    fp=open('reports/report.bugfree.{0}.html'.format(time.strftime("%Y-%m-%d %H-%M-%S")),'wb')
    runner=HTMLTestRunner.HTMLTestRunner(
        stream = fp,  # /输出/
        title = 'Bugfree的测试报告',
        description = 'Bugfree的所有测试用例执行细节'
        )
    runner.run(suite)
    fp.close()




