'''
[编程实现]
输入一个正整数（N），输入1到N之间所有偶数的和（包含N）。 
[输入格式]
一行，一个正整数。 
[输出格式]
一行，1到N之间所有偶数的和。 
[样例输入]
6 
[样例输出]
12 
'''
N = int(input())
evenSum = 0
for i in range(1, N+1):
    if i % 2 == 0:
        evenSum += i
print(evenSum)
