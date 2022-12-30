n=int(input())
a=list(map(int,input().split()))
s=[0]*(n+1)
for _ in a: s[_]+=1
sc0=[]; sc1=[]
import math
for _ in s:
    sc0.append(math.comb(_,2))
    if _>0:
        sc1.append(math.comb(_-1,2))
    else: sc1.append(0)
for _ in a:
    print(sum(sc0[:_]+[sc1[_]]+sc0[_+1:]))