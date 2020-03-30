""":raise

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""
class Solution():
    def isAnagram(self,s,t):
        import collections
        a= collections.Counter(s)
        b= collections.Counter(t)
        if a ==b:
            return True
        else:
            return False
        # ls=list(s.split(" "))
        # lt=list(s.split(" "))
        #
        # if len(ls)>len(lt):
        #     maxlength=len(ls)
        #     minlength=len(lt)
        # else:
        #     maxlength = len(lt)
        #     minlength = len(ls)
        #
        # for i in range(maxlength):
        #     for j in range(minlength):
        #         if  ls[j]==lt[j]:
        #             continue
        #         else:
        #             break

if __name__ == '__main__':
    s=Solution()
    ls='nagaram'
    lt='anagram'
    x=s.isAnagram(ls,lt)
    print(x)