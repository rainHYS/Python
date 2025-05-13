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
    if n == 0:
        return 1
    return 1/recursionFactorial(n) + recursionE(n-1)


def recursionFactorial(n):
    if n == 0 or n == 1:
        return 1
    return n*recursionFactorial(n-1)


n = int(input())
print(recursionE(n))