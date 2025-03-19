flowerbed=[1,0,0,0,1]
n=1
u=0
for i in range(len(flowerbed)):
    t=flowerbed[u]
    if flowerbed[i]==0 and t==0:
        flowerbed[i]=1
        n-=1
    u+=1    
if n==0:
        print(True) 
else:
        print(False)
  
