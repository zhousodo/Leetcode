""":raise
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
"""

class Solution():
    def removeElement(self,nums,val):
        i=1
        while i<=len(nums):
            if nums[i-1]==val:
                nums.pop(i-1)

            else:

                i += 1
        return len(nums)

    ### 方法二
    # while True:
    #     try:
    #         nums.remove(val)
    #     except ValueError:
    #         break



if __name__ == '__main__':
    s=Solution()
    numbs=[3,2,2,3,4]
    val=3
    x=s.removeElement(numbs,val)
    print(x)