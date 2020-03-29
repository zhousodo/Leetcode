"""
Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

class Solution:
    import random
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        if len(strs)==0:
            return prefix
        for i in xrange()