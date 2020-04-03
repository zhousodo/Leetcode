"""
Input: "Hello World"
Output: 5
"""
class Solution(object):
    def lengthOfLastword(self,s):
        reverseListOfworlds=s.split(" ")[::-1]
        for world in reverseListOfworlds:
            if world!=" ":
                return len(world)
            else:
                continue
        #print(len(world))
        return

if __name__ == '__main__':
    sl=Solution()
    str="hello world"
    x=sl.lengthOfLastword(str)
    print(x)


