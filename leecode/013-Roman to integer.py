"""
Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

"""
class Solution:
    def romanToInt(self, s: str) -> int:
        """
        如果MDCLXVI是顺序出现的说明是加， 如果顺序不一样说明是减法
        :param s:
        :return:
        """


        roman={"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
        z=0
        for i in range(0,len(s)-1):
            if roman[s[i]]<roman[s[i+1]]:
                z= z-roman[s[i]]
            else:
                z= z+roman[s[i]]
        print(z+roman[s[-1]])
        return  z+roman[s[-1]]



sl =Solution()
sl.romanToInt("MCMXCIV")




