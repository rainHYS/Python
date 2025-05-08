'''
[编程实现]
输入一串字符，输出这串字符中所有大写字母。如果没有大写字母，输出‘NULL’。 
[输入格式]
一行，一串字符 
[输出格式]
一行，字符串中的所有大写字母，或者是‘NULL’ 
[样例输入]
aPP I cDf G
[样例输出]
PPIDG 
'''
array = str(input())
status= 1
for i in range(len(array)):
    if array[i].isupper():
        print(array[i],end="")
        status=0
if status:
    print("NULL")
else:
    print()
