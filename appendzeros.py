a=[0,0,1]
for i in range(len(a)):
    print("bef",a)
    if a[i]==0:
        a.pop(i)
        a.append(0)
    print(a)    
print(a)        