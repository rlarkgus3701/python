elif s == "삼각형":
    s = turtle.textinput("","변: ")
    l= int(s)
    t.forward(l)
    t.left(120)
    t.forward(l)
    t.left(120)
    t.forward(l)
elif s == "원":
     s = turtle.textinput("","반지름: ")
     r= int(s)
     t.circle(r)
else:
    pass