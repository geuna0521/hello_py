# boj https://www.acmicpc.net/submit/11022
test_case=int(input())
sum_list=[]
get_a=[]
get_b=[]
for cycle in range(test_case):
    a,b=input().split()
    get_a.append(int(a))
    get_b.append(int(b))
    sum=int(a)+int(b)
    sum_list.append(sum)
for result in range(test_case):
    print("Case #"+str(result+1)+": "+str(get_a[result])+" + "+str(get_b[result])+ " = "+str(sum_list[result]))