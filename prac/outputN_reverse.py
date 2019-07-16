#boj https://www.acmicpc.net/problem/2742

num=int(input())
result= num +1
for number in range(num):
    result -= 1
    print(result)