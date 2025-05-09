'''
[编程实现]
利用公式 e=1+1/1!+1/2!+1/3!+⋯+1/n!，求 e 的值。 
[输入格式]
输入只有一行，该行包含一个整数 n，表示计算 e 时累加到 1/n!。 
[输出格式]
输出只有一行，该行包含计算出来的 e 的值。 
[样例输入]
10 
[样例输出]
2.7182815255731922 
'''
def recursionE(n):
    if n==1:
        return 1
    return 1/recursionE

def recursionFactorial(n):
