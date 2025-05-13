'''
[编程实现]
有两个列表： 
a = ['输入', '打印', '如果', '继续', '否则'] 
b = ['input', 'print', 'if', 'continue', 'else'] 
其中中英文位置一一对应。 
程序要求通过输入查找第几个，查出对应中英文 
[输入格式]
列表中的第几个 
[输出格式]
对应的英文如： 
a列表中第1个元素是输入。对应的b中的元素是：input 
[样例输入]
2 
[样例输出]
a列表中第2个元素是打印。对应的b中的元素是：print 
'''
a = ['输入', '打印', '如果', '继续', '否则']
b = ['input', 'print', 'if', 'continue', 'else']
userInput = int(input())
print("a列表中第", userInput, "个元素是", a[userInput-1], "。对应的b中的元素是：", b[userInput-1])