# s="ickkvio"
# c= s
# vow=["a","e","i","o","u"]
# st,en=0,len(s)-1
# o,k=-1,-1
# p,q = -1,-1
# m = []
# for i in range(len(c)):
#     if s[i] in vow and p==-1:
#         p=i
#     if s[len(c)-1-i] in vow and q ==-1:
#         q = len(c)-1-i
#     print("Value", p, q)
#     if p>=0 and q>=0 and p not in m and q not in m and p!=q:
#         print(s[:p]+s[q]+s[p+1:q]+s[p]+s[q+1:])
#         s = s[:p]+s[q]+s[p+1:q]+s[p]+s[q+1:]
#         m.extend([p,q])
#         p,q=-1,-1
# print("Answer ", s)
# while st!=int(len(s)/2):
#     print('rtyu')
#     if s[st].lower() in vow and o==-1:
#         o=st
#     if s[en].lower() in vow and k==-1:
#         k=en
#     if o>0 and k>0:
#         print(o,k)
#         print(
#            s[:o]+s[k]+s[o+1:k]+s[o]+s[k+1:]
#         )
#         s=s[:o]+s[k]+s[o+1:k]+s[o]+s[k+1:]
#         o,k=-1,-1
#     st+=1
#     en-=1  
# print("jd")
# print(s)

s="Icecream"
