x = 2
y = 1
z = 0

if x > y :
    print("x는 y보다 크다.")
print("x가 y보다 크기(true)때문에 출력된다.","\n")
if x < y :
    print("x보다 y가 크다")
print("y가 x보다 크지 않기(false)때문에 출력 안된다.","\n")
if not x < y :
    print("x보다 y가 크지 않다.","\n")
print("not이 붙어서 true이기 때문에 출력된다.","\n")
if x > z and x > y :
    print("y가 z보다 크고 x가 y보다 크다.")
print("두가지 모두 맞으면 출력된다.","\n")