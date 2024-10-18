yen = int(input('入金金額:'))
buy = int(input('支払金額:'))

b = [5, 17, 8, 42]

ret = yen - buy


c = ret // 500
if c > b[0]:
    c = b[0]
ret = ret - (500*c)

d = ret // 100
if d > b[1]:
    d = b[1]
ret = ret - (100*d)

e = ret // 50
if e > b[2]:
    e = b[2]
ret = ret - (50*e)

f = ret // 10
if f < b[3]:
    print("500円玉:" + str(c) + "枚")
    print("100円玉:" + str(d) + "枚")
    print("50円玉:" + str(e) + "枚")
    print("10円玉:" + str(f) + "枚")

else:
    print("おつりが足りません")