import time

now = time.time()
thisyear = int(1970 + now//(365*24*3600))

print("올해는 ",thisyear,"입니다.")
age = int(input("몇 살이신지요? "))
print("2050에는 ",(age+2050-thisyear),"살 이시군요.")