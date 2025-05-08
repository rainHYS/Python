'''
[编程实现]
小明最近在学习算式，你们可以帮他实现简单的计算器帮助他检查自己的答案是否正确吗？
具体要求如下：
一个最简单的计算器，支持四种运算，仅需考虑输入输出为整数的情况。
1.如果出现除数为0的情况，则输出：Divided by zero!
2.如果出现无效的操作符(即不属于+、-、*、/之一），则输出：Invalid operator!
[输入格式]
三行，第一行为一个符号，第二、三行为两个数字
[输出格式]
一行，输出两个数的和，或者差，或者乘积，或者商，或者Invalid operator！
[样例输入]1
请输入计算符号：/
请输入第一个数字：3
请输入第二个数字：0
[样例输出]1
Divided by zero！
[样例输入]2
请输入计算符号：&
请输入第一个数字：3
请输入第二个数字：0
[样例输出]2
Invalid operator！
[样例输入]3
请输入计算符号：*
请输入第一个数字：3
请输入第二个数字：8
[样例输出]3
24
'''
calSign = str(input("请输入计算符号："))
firstNum = int(input("请输入第一个数字："))
secondNum = int(input("请输入第二个数字："))
if calSign == "+":
    print(firstNum+secondNum)
elif calSign == "-":
    print(firstNum-secondNum)
elif calSign == "*":
    print(firstNum*secondNum)
elif calSign == "/":
    if secondNum==0:
        print("Divided by zero！")
    else:
        print(firstNum/secondNum)
else:
    print("Invalid operator！")