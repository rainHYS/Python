'''
[编程实现]
输入一串字符，如果第一个字符是大写字母，就把字符串里的字母都变成大写字母输出，
如果第一个字符是小写字母，就把字符串里的字母都变成小写字母输出，如果第一个字符不是字母，输出这个字符串。 
[输入格式]
一行，一个字符串。 
[输出格式]
一行，输出转化成大写字母的字符串，或者输出转化成小写字母的字符串，或者输出字符串本身。 
[样例输入1] [样例输入2] [样例输入3]
Tomorrow   fdsafRD17   1 apple 

[样例输出1] [样例输出2] [样例输出3]
TOMORROW   fdsafrd17   1 apple 
'''
array=str(input())
if array[0].isupper():
    print(array.upper())
elif array[0].islower():
    print(array.lower())
else:
    print(array)