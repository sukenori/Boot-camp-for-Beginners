n=int(input())
a=list(map(int,input().split()))
ad={}; sad=0
for i in list(set(a)):
    c=a.count(i)
    ad[i]=c
    sad+=c*(c-1)/2
for i in a:
    print(int(sad-ad[i]*(ad[i]-1)/2+(ad[i]-1)*(ad[i]-2)/2))