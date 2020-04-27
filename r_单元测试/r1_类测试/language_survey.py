from r_单元测试.r1_类测试.survey import Survey

# 定义一个问题，并创建一个表示调查的Survey对象
question = "What language did you first learn to speak?"
my_survey = Survey(question)

# 显示问题并存储答案
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# 显示调查结果
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
