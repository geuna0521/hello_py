# boj https://www.acmicpc.net/problem/2439

line_num = int(input())
for lines in range(line_num):
    line = "*" * (int(lines) + 1)
    blank=" " * (line_num - (int(lines)+1))
    print(blank + line)