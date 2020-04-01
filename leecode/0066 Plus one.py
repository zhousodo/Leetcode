
"""
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

"""

class Solution(object):
    def plusOne(self,numbs):
        for i  in range(len(numbs)-1,-1,-1):
            if numbs[i]+1>9:
                numbs[i]=0
                if i==0:
                    numbs.insert(0,1)
                    return numbs
            else:
                numbs[i]+=1
                return numbs

