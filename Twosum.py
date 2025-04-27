def twosum(arr,val):
    sol={}
    for i,j in enumerate(arr):
        ans=val-j
        if ans in sol:
            return [sol[ans],i]
        sol[j]=i
    return None 
print(twosum([2,7,11,15],9))

