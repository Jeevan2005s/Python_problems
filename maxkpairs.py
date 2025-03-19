nums=[1,12,-5,-6,50,3]
k=4
x=k
s=0
r=len(nums)-k
for i in range(r+1):
    # print(sum(nums[i:k])/4)
    print(sum(nums[i:k])/x)
    if s<(sum(nums[i:k])/x):
        s=(sum(nums[i:k])/x)
    k+=1 
print(s)