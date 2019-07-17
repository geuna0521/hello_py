# boj https://www.acmicpc.net/problem/10871

num, stand = input().split()
series = input().split()
num = int(num)
stand = int(stand)

for i in range(num):
    if int(series[i]) < stand:
        print(series[i])
