def product(nums):  
    l=len(nums)
    arr=[1]*l
    for i in range(1,l):
        print(nums[i-1], arr[i-1])
        arr[i]=arr[i-1]*nums[i-1]
        print(arr[i])
    f=1    
    for i in range(l-1,-1,-1):
        arr[i]=arr[i]*f
        f*=nums[i]
        print(arr)
    return arr  
# print(product([1,2,3,4]))

def products(nums):
    # j,u=1,0
    # h=0
    # for i in range(len(nums)):
    #     if nums[i]!=0:
    #         j*=nums[i]
    #     else:
    #         u+=1 
    #         h=i   
    # arr=[0]*len(nums)
    # if u>1:
    #     return arr
    # elif u==1:
    #     arr[h]=j
    #     return arr
    # else:
    #     for i in range(len(arr)):
    #         arr[i]=j//nums[i]
    #     return arr 
    val,coun=1,0
    ind=0
    for i in range(len(nums)):
        if nums[i]!=0:
            val*=nums[i]
        else:
            coun+=1
            ind=i
    if coun==0:
        arr=[0]*len(nums)
        for i in range(len(arr)):
            arr[i]=val//nums[i]
        return arr
    elif coun>1:
        return [0]*len(nums)                        
    else:
        arr=[0]*len(nums)
        arr[ind]=val
        return arr         


print(products([1,2,3,4]))       