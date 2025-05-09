'''
[编程实现]
一个系统，账号是Python，密码是1234，输入正确的账号和密码，输出“登陆成功”，如果输入的账号或密码错误，输出“账号或者密码错误，请重新输入”。 
[输入格式]
两行，第一行输入账号，第二行输出密码。 
[输出格式]
一行，输出‘登陆成功’，或者输出‘账号或者密码错误，请重新输入’ 
[样例输入]
请输入账号：Python 
请输入密码：1234 
[样例输出]
登陆成功 
'''
account, password = "Python", "1234"

while True:
    userAccount = input("请输入账号：")
    userPassword = input("请输入密码：")
    
    if userAccount == account and userPassword == password:
        print("登陆成功")
        break
    else:
        print("账号或者密码错误，请重新输入")