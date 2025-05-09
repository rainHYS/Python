'''
[编程实现]
花式玩数字：把数字1组成一个等腰三角形 
[输入格式]
一行，一个数字 
[输出格式]
数字1组成的n层三角形 
[样例输入]
5 
[样例输出]
    1
   111
  11111
 1111111
111111111
'''
userInput=int(input())
for i in range(1,userInput+1):
    for j in range(userInput-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("1",end="")
    print()
