# '''
# python自动化工作:
# 1、准备好自动化的测试用例    === done   test_case_api.xlsx
# 2、使用python去读取测试用例 === done   read_data()
# 4、发送请求，得到响应结果    === done   api_func()
# 5、结果的判断？ 执行结果 vs  预期结果  == 断言
# 6、得到一个最终结果，回写到测试用例   === done   write_result()
# '''
# import openpyxl
# import  requests
# # 读取测试用例
# def read_data(filename,sheetname):
#     wb = openpyxl.load_workbook(filename)
#     sheet = wb[sheetname]
#     max_row = sheet.max_row
#     case_list = []
#     for i in range(2,max_row + 1,1):
#         dict1 = dict(
#             case_id = sheet.cell(row=i,column=1).value,   # 取出测试用例id
#             url=sheet.cell(row=i, column=5).value,   # 取出url
#             data=sheet.cell(row=i, column=6).value,  # 取出请求体数据
#             expected=sheet.cell(row=i, column=7).value)   # 取出预期结果
#         case_list.append(dict1)   # 把一条条的测试用例放到列表里
#     return case_list    # 返回结果，方便后面调用
# # 发送请求
# def api_func(url,data):
#     header_login = {"X-Lemonban-Media-Type":"lemonban.v2",
#     'Content-Type':'application/json', "Authorization": "Bearer" + " " + token}   # 请求头
#
#     res = requests.post(url=url,json=data,headers=header_login)
#     token = res.json()['data']['token_info']['token']
#     response = res.json()
#
#     return response
# # 写入测试结果
# def write_result(filename,sheetname,row,column,final_result):
#     wb = openpyxl.load_workbook(filename)
#     sheet = wb[sheetname]
#     sheet.cell(row=row,column=column).value = final_result   # 将单元格的值赋给final_result
#     wb.save(filename)
#
#
# # 封装成一个执行函数并断言
# def excuse_func(filename,sheetname):
#     cases = read_data(filename,sheetname)
#     for case in cases:
#         # print(case)
#         case_id = case['case_id']
#         url = case.get('url')
#         data = case.get('data')   #  通过Excel取出的值是str类型，需要转换类型
#         data = eval(data)   # eval()：运行被字符串包括的python表达式，这里只取出引号里的内容
#         expected = case.get('expected')
#         expected = eval(expected)
#         expected_msg = expected.get('msg')  # 取出实际执行里的msg信息
#         print(case_id,url,data,expected)
#         real_result =api_func(url=url,data=data)
#         real_msg =real_result.get('msg')  #  取出实际执行里的msg信息
#         print('预期结果为:{}'.format(expected_msg))
#         print('实际结果为:{}'.format(real_msg))
#         if expected_msg == real_msg:
#             print('第{}条用例通过'.format(case_id))
#             final_res = 'pass'
#         else:
#             print('第{}条用例不通过'.format(case_id))
#             final_res = 'fail'
#             print('*' * 10)
#         write_result(filename,sheetname,case_id +1,8,final_res)
# excuse_func('test_case_api.xlsx','login')

# name = input("请输入姓名：")
# gender = input("请输入性别：")
# age = input("请输入年龄：")
# # dict1={'name':name,'gender':gender,'age':age}
# print('我的名字{}'.format(name),'今年{}岁'.format(age),'性别{}'.format(gender),",喜欢敲代码")
strs = "They look good and stick good!"
count_set = ['o']
res=strs.count('o')
print(res)