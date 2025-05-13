'''
[编程实现]
有列表 a = ['input', 'print', 'continue', 'break', 'if', 'else', 'while']。 交换其中2个元素的位置后再打印列表 
[输入格式]
两行。 
第一行：要交换的第一个元素的位置；如1代表input 
第二行：要交换的第二个元素的位置 
[输出格式]
一行：交换位置后的列表 
[样例输入]
1 
2 
[样例输出]
['print', 'input', 'continue', 'break', 'if', 'else', 'while'] 
'''

a = ['input', 'print', 'continue', 'break', 'if', 'else', 'while']
i, j = int(input())-1, int(input())-1
a[i], a[j] = a[j], a[i]
print(a)