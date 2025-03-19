import timeit

# class Solution:
#     def mergeAlternatively(word1,word2):
#         s=""
#         l=max(len(word1),len(word2))
#         for i in range(l):
#             if i<len(word1):
#                 s +=word1[i]
#             if i<len(word2):
#                 s +=word2[i]
#         return s            
# a=input()
# b=input()
# e=Solution()
# print(e.mergeAlternatively(a,b))        
# class Solution:
#     def mergeAlternatively(word1, word2):
#         s = ""
#         l = max(len(word1), len(word2))
#         for i in range(l):
#             if i < len(word1):
#                 s += word1[i]
#             if i < len(word2):
#                 s += word2[i]
#         return s

# param_1 = input()
# param_2 = input()

def productExceptSelf():
    nums = [1,2,3,4]
    l=len(nums)
    arr=[1]*l
    for i in range(1,l):
        arr[i]=arr[i-1]*nums[i-1]
    f=1    
    for i in range(l-1,-1,-1):
        arr[i]=arr[i]*f
        f*=nums[i]
    return arr  
print(timeit.timeit(productExceptSelf,number=1))
