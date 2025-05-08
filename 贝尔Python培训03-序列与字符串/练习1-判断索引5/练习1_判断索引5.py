'''
[编程实现]
输入一个字符串，如果这个字符串索引5上的符号是大写字母，输出‘YES’，
如果不是大写字母，输出“NO”，如果该字符串没有索引5，输出‘NULL’。(注意：所有单词字母都是大写) 
[输入格式]
一行，一串字符。 
[输出格式]
一行，输出‘YES’，或者‘NO’，或者‘NULL’ 
[样例输入]
abc 
[样例输出]
NULL 
'''
array=str(input())
if len(array)<=5:
    print("NULL")
elif array[5].isupper():
    print("YES")
else:
    print("NO")
