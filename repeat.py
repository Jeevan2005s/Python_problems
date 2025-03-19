#program to find the repeating value in the list
a=list(map(int,input().split()))
b=set()
for i in a:
    if i in b:
        print(i)
    else:
        b.add(i)
            
