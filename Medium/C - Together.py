n=int(input())
a=list(map(int,input().split()))
print(max([sum([ai-1<=a[i]<=ai+1 for i in range(n)]) for ai in list(set(a))]))