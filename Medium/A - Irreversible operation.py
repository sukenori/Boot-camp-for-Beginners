s=input()
c=0
while True:
    ns=s.replace("BW","WB",1)
    if ns!=s:
        c+=1
        s=ns
    else:
        print(c)
        break