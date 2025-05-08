'''
[编程实现]
输入一串字符，找到字符串里的所有数字，并求出这些数字的和。如果字符串里没有数字，输出0。 
[输入格式]
一行，一串字符 
[输出格式]
一行，字符串里所有数字的和 
[样例输入]
请输入一串字符：i need 7 apples and 8 bananas. 
[样例输出]
15
'''
array = str(input("请输入一串字符："))
numSum = 0
for char in array:
    if char.isdigit():
        numSum += int(char)
print(numSum)
