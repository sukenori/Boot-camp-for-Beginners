n=int(input())
a=list(map(int,input().split()))
aset=set(a)
adic={i:a.count(i) for i in list(aset) if a.count(i)>1}
import math
for i in list(a):
    aidic=adic.copy()
    if i in adic: aidic[i]=adic[i]-1
    print(sum(math.comb(aidic[j],2) for j in adic))