money = int(input("투입한 돈: ")) # 변수 money를 선언하고 정수형으로 받는다.
price = int(input("물건 값: ")) # 변수 price를 선언하고 정수형으로 받는다.

change = money - price #거스름돈을 계산한다.
coin500s = change // 500 #500으로 나누어서 몫이 500원짜리의 개수이다.
change = change % 500 # 500으로 나눈 나머지를 계산한다.
coin100s = change // 100 # 100으로 나누어서 몫이 100원짜리의 개수이다.
print("500원 동전의 개수: ", coin500s) #거슬러줄 500원짜리의 개수를 출력한다.
print("100원 동전의 개수: ", coin100s) #거슬러줄 100원짜리의 개수를 출력한다.