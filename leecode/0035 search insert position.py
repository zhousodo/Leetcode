""":raise
Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
"""

class Solution:
    def searchInsert(self,nums,target):
        coutn=0
        for i in range(len(nums)):
            if target<=nums[i]:
                nums.insert(i,target)
                return i
            else:
                nums.append(target)
                return len(nums)
        # print(coutn)
        # return coutnx


if __name__ == '__main__':
    s=Solution()
    nums=[1,3,5,6]
    target=7
    x=s.searchInsert(nums,target)
    print(x)