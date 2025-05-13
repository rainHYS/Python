'''
[编程实现]
使用turtle绘制如下图所示图形，要求： 
1）绘制一个正方形且内切一个填充的圆； 
2）正方形边长为100且轮廓线为红色； 
3）内切圆轮廓线为红色，并且填充为黄色； 
4）绘制过程中隐藏画笔，并能清楚地看到图形绘制过程。 
[输入格式]
无 
[输出格式]
如下图 
'''
import turtle
pen=turtle.Pen()
pen.hideturtle()
pen.penup()
pen.goto(-50,50)
pen.pendown()
for i in range(4):
    pen.forward(100)
    pen.right(90)
pen.penup()
pen.goto(0,-50)
pen.pendown()
pen.color("red")
pen.fillcolor("yellow")
pen.begin_fill()
pen.circle(50)
pen.end_fill()
turtle.done()


