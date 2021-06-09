else:
    Lookup = -tmp
    start = 0
    end = len(numlist) - 1
    key = int((start + end) / 2)
    while True:
        if start > end:
            print("찾는 값이 없습니다.")
            break
    if numlist[key] == lookup:
        print("{}(은)는 {}번째 위치에 있습니다.".format(Lookup, key))
        break
    elif numlist[key] < lookup:
        start = key + 1
        key = int((start + end) / 2)
    else:
        end = key - 1
        key = int((start +end) / 2)