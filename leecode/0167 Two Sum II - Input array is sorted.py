""":raise
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""

class Solution(object):
    def twoSum(self,nums,target):
        # num=0
        # for i in range(len(nums)):
        #     if target== nums[i]+nums[i+1]:
        #         return i+1, i+2
        #     continue

        # dic={}
        # for index ,value in enumerate(nums):
        #     if value in dic:
        #         return (dic[value],index+1)
        #     else:
        #         dic[target-value]= index+1
        #
        i,j=0,len(nums)-1
        while i<j:
            if nums[i]+nums[j]<target:
                i+=1
            elif nums[i]+ nums[j] >target:
                j-=1
            else:
                return [i+1] ,[j+1]


if __name__ == '__main__':
    sl= Solution()
    sl.twoSum([2,7,11,15],9)

    a,b=sl.twoSum([2,7,11,15],9)
    print(a,b)