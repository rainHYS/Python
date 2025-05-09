"""
[编程实现]
输入一串字符，将其反向输出。
[输入格式]
一行，一串字符。
[输出格式]
一行，反向输出的字符串
[样例输入]
12345
[样例输出]
54321
"""

array = str(input())
length = len(array) - 1
while length >= 0:
    print(array[length],end="")
    length -= 1
print()

#或者这么写
print(array[::-1])      # 使用切片反向输出