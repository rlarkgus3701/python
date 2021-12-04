import turtle
t = turtle.Turtle()
t.shape("turtle")

def square(lenght):#lenght는 한변의 길이
    for i in range(6):
        t.forward(lenght)
        t.left(60)
t.up() #펜을 든다.
t.goto(-200,0) #(-200,0)으로 이동한다.
t.down() #펜을 내린다.
square(100); #함수를 호출한다.
t.up()
t.goto(0,0)
t.down()
square(100);
t.up()
t.goto(200,0)
t.down()      
square(100);        