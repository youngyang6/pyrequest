import time,sys
sys.path.append('./db_fixture')
sys.path.append('./interface')
from HTMLTestRunner import HTMLTestRunner
import unittest
from db_fixture import test_data

#添加测试用例路径
test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')

if __name__ == "__main__":
    test_data.init_data()

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'

    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Guest Manage System Interface Test Report',
                            description='Implementation Example with: ')

    runner.run(discover)
    fp.close()
