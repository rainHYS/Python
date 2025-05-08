'''
[编程实现]
输入数字 的表示星期一至星期日，输出对应的星期几的英文名称。 
如果是1 ，输出 Monday; 
如果是2 ，输出 Tuesday; 
如果是3 ，输出 Wednesday; 
如果是4 ，输出 Thursday; 
如果是5 ，输出 Friday; 
如果是6 ，输出 Saturday; 
如果是7 ，输出 Sunday; 
如果没有星期几，则输出 No。 
ps :首字母要大写 
[输入格式]
输入共一行，一个整数 。 
[输出格式]
输出共一行，一个英文单词。 
[样例输入]
5 
[样例输出]
Friday 
'''
num=int(input())
if num==1:
    print("Monday")
elif num==2:
    print("Tuesday")
elif num==3:
    print("Wednesday")
elif num==4:
    print("Thursday")
elif num==5:
    print("Friday")
elif num==6:
    print("Saturday")
elif num==7:
    print("Sunday")
else:
    print("No")
