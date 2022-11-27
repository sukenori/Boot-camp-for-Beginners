s=input()
a=[0]
for i,si in enumerate(s):
    a.append(a[i]+(si=="<")-(si==">"))
print(a)