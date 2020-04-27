import unittest  # 1.导入测试包
from r_单元测试.r1_类测试.survey import Survey  # 2.导入要测试的类


class TestAnonmyousSurvey(unittest.TestCase):  # 3.创建一个继承unittest.TestCase的类，并编写测试代码

    def test_store_single_response(self):  # 4.测试方法必须以 "test_" 开头
        """测试单个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = Survey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)  # 方法assertIn()来核实它包含在答案列表中
        # self.assertIn('math', my_survey.responses)  # 方法assertIn()来核实它包含在答案列表中

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = Survey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)
