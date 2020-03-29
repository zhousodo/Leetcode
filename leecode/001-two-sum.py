"""
给定一个整数数组，返回两个数字的索引，以便它们加起来成为一个特定的目标。

您可以假设每个输入都只有一个解决方案，并且您可能不会两次使用同一元素。

例：

给定nums = [2，7，11，15]，目标= 9，

因为nums [ 0 ] + nums [ 1 ] = 2 + 7 = 9，
返回[ 0，1 ]。
"""

# 方法一
# def two_sum(list, target):
#     length= len(list)
#     for i , num1 in enumerate(list):
#         for j ,num2 in enumerate(list[i+1:],i+1):
#             if num1+num2==target:
#                 print(i,j)
#                 return i,j
#


#方法二
def two_sum(nums,target):
    for i in range(len(nums)):
        sum=nums[i]
        for j in range(i+1,len(nums)):
            if sum+nums[j]==target:
                print(i,j)
                return i,j


if __name__ == '__main__':
    ls=[3,2,4]
    two_sum(ls,6)
