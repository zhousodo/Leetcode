"""
Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.

"""
class Solution:
    def removeDuplicates(self,nums):
        ## 这样写错在了i 一直停留在1 无法自增自减
        # a=[]
        # for i in range(len(nums)):
        #     while  i<len(nums):
        #         if nums[i]==nums[i+1]:
        #             continue
        #         else:
        #             a.append(nums[i])
        # print(len(a))
        # return len(a)

        #########################
        ### 这种做法考虑到了最后一位的情况，  用后一位和前一位比较， 能够知道数组的界限， 而不是用前一位和后一位比较，
        i=1
        while i<len(nums):
            if (nums[i]==nums[i-1]):
                nums.pop(i)
            else:
                i+=1

        return len(nums)



if __name__ == '__main__':
    print('adaf')
    ls=[0,0,1,1,1,2,2,3,3,4]
    s=Solution()
    x=s.removeDuplicates(ls)
    print(x)
