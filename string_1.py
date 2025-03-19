# # a=" hello world " 
# # print(a.split()[::-1])

# def product_except_self(nums):
#     n = len(nums)
#     answer = [1] * n
#     left_product = 1
    
#     for i in range(n):
#         answer[i] = left_product
#         left_product *= nums[i]
#     right_product = 1
#     for i in range(n - 1, -1, -1):
#         print(answer[i]*right_product)
#         print(answer[i])
#         print(right_product)
#         answer[i] *= right_product
#         right_product *= nums[i]
   
#         print(answer)
    
#     return answer

# # Example usage
# print(product_except_self([1,2,3,4]))  # Output: [24,12,8,6]

class Solution:
    def increasingTriplet(nums):
        first = sum(nums)
        second = sum(nums)
        for num in nums:
            if num <= first:
                first = num
                print("num:",num)
                print(first)
            elif num <= second:
                second = num
                print("num2:",num)
                print(second)
            else:
                return True
        return False
print(Solution.increasingTriplet([5,4,3,2,1]))