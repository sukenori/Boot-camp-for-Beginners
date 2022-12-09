r,g,b,n=map(int,input().split())
import math
c=0
for i in range(int(n/r)+1):
    for j in range(int((n-r*i)/g),int(n/g)+1):
        if n>=r*i+g*j and (n-r*i-g*j)%b==0:
            c+=(n-r*i-g*j)//b
            print(n-r*i-g*j)
print(c)