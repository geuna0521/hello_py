h, m = (input().split())  # 시간, 분 입력받기, 0<=h<=23, 0<=m<=59
h = int(h)
m = int(m)

if h != 0:
    if m < 45:
        print(h - 1, m + 15)  # 15=+60-45
    else:
        print(h, m - 45)
else:
    if m < 45:
        print(23, m + 15)  # 15=+60-45
    else:
        print(0, m - 45)
