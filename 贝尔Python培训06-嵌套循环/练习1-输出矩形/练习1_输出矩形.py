'''
[编程实现]
我们学习过双重循环，可以完成一个矩形的输出。 
[输入格式]
输入两个行，第一行表示矩形的行数 ，第二行表示每行有多少个“*”字符。 
[输出格式]
如下图形 
[样例输入]
4 
5 
[样例输出]
***** 
***** 
***** 
***** 
'''
row=int(input())
column=int(input())
for i in range(row):
    for i in range(column):
        print("*",end="")
    print()
