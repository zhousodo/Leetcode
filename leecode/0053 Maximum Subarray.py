"""":raise
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

class Solution():
    def MaxSubArray(self,nums):
        maxsum=nums[0]
        currentsum= nums[0]
        for i in nums[1:]:
            currentsum= max(i,currentsum+i)
            maxsum= max(maxsum,currentsum)

        return maxsum

if __name__ == '__main__':
    nums= [-2,1,-3,4,-1,2,1,-5,4]
    sl=Solution()
    xz=sl.MaxSubArray(nums)
    print(xz)