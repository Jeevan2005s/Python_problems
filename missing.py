#to find the missing number from the array form 0 to n
# a=list(map(int,input().split()))
# a.sort()
# x=0
# for i in a:
#     if i!=x:
#        z=x
#     x+=1   
# print(z)   

# a=list(map(int,input().split()))
# b=sum(a)
# c=0
# for i in range(len(a)+1):
#     c+=i
# print(c-b)    

#  to find all the missing values in a given list and that to the list and display from 1 to n
# a=list(map(int,input().split()))
# d=set(a)
# b=[]
# for i in range(1,len(a)+1):
#     if i not in d:
#         b.append(i)
# print(b)        

#finding the two number sum from a list of given numbers
# b=list(map(int,input().split()))
b = [1,5,3,7,2]
t =5
# t=int(input())
def sla(a,t):
  c={}
  print(list(enumerate(b)))
  for i,j  in enumerate(b):
    d=t-j
    print("d",d, i)
    if d in c:
        print(c[d],i)
        return [c[d],i]
    c[j]=i
    print("dict",c)
  return []   
c=sla(b,t)
print(c)

# a=[]
# for i in range(len(b)):
#     if t-b[i] in b:
#        a.append(i)
# print(a)       