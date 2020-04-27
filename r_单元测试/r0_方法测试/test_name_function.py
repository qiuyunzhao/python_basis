import unittest  # 1.导入测试包
from r_单元测试.r0_方法测试.name_function import get_formatted_name, get_middle_name  # 2.导入要测试的代码


class GetFormattedNameTest(unittest.TestCase):  # 3.创建一个继承unittest.TestCase的类，并编写测试代码

    def setUp(self) -> None:
        """
        测试之前的准备工作
        """
        print("测试之前的准备工作")

    def tearDown(self) -> None:
        """
        测试之后的收尾,如关闭数据库
        """
        print("测试之后的收尾")

    # 成功的测试
    def test_get_formatted_name(self):  # 4.测试方法必须以 "test_" 开头
        formatted_name = get_formatted_name('janis', 'joplin')
        print(formatted_name)
        self.assertEqual(formatted_name, 'Janis Joplin')  # 调用unittest的方法assertEqual()

    # 失败的测试
    def test_get_middle_name(self):
        formatted_name = get_middle_name('janis', 'joplin')
        print(formatted_name)
        self.assertEqual(formatted_name, 'Janis Joplin')  # 调用unittest的方法assertEqual()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GetFormattedNameTest('test_get_formatted_name'))
    suite.addTest(GetFormattedNameTest('test_get_middle_name'))

    runner = unittest.TextTestRunner()
    runner.run(suite)
