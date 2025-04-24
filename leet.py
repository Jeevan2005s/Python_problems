# # grid=[[1,2,3],[1,2,3],[5,6,7]]
# # n=len(grid)
# # cols = [[grid[r][c] for r in range(n)] for c in range(n)]

# # for c in range(n):
# #     for r in range(n):
# #         a.append(grid[r][c])
# # print(cols)

# a=[1,2,3,"*"]
# for i in range(len(a)):
#     if i=="*" and i!=0:
#         a.pop(i-1)
#         a.pop(i)
# print(a)        

# def sk(asteroids):
#     stack=[]
#     for i in range(len(asteroids)):
#         print(asteroids[i])
#         print("asfd",asteroids[i-1])
#         if asteroids[i]<0 and asteroids[i]>asteroids[i-1]:
#             print("i")
#             stack.pop()
#         else:
#             stack.append(asteroids[i])
#     return  stack 

# print(sk([5,10,-5]))

def decodeString(s):
    stack = []
    curr_num = 0
    curr_str = ""

    for char in s:
        if char.isdigit():
            curr_num = int(char)
        elif char == "[":
            stack.append((curr_str, curr_num))
            curr_str, curr_num = "", 0
        elif char == "]":
            prev_str, num = stack.pop()
            print(prev_str)
            curr_str = prev_str + num * curr_str

        else:
            curr_str += char
            print(curr_str)
        # print(curr_num)    
        # print(curr_str)    

    return curr_str

a=decodeString("2[abc]3[cd]ef")
print(a)
