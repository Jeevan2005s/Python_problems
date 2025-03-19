a=list(map(int,input().split()))
count=0
for i in range(0,len(a)-1):
    c=False    
    for j in range(len(a)-1-i):       
        if a[j]>a[j+1]:
           a[j],a[j+1]=a[j+1],a[j]
           c=True
        count+=1    
    if c==False:
        break     
print(count)        
print(*a)

# a=list(map(int,input().split()))
# a=[1,5,4,3,2]
# n=0
# while True:
#     for j in range(0,len(a)-1):          
#         if a[j]>a[j+1]:
#            a[j],a[j+1]=a[j+1],a[j]
#            print(a)
#     n+=1    
#     if n==len(a)-1:
#         break       
# print(*a)    