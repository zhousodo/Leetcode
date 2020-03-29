"""
Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
"""
def reverse_integer(x):
    b= 2**31
    neg_b= -1*b
    rev= 0
    if x>0:
        while x!=0:
            #取余数
            digit=x%10
            # 取整
            x= x//10
            rev=rev*10+digit
    else:
        x= abs(x)
        while x!=0:
            digit= x%10
            x= x//10
            rev= rev*10+digit
        rev= -1*rev

    if rev>b or rev <neg_b:
        return 0
    else:
        print(rev)
        return rev

if __name__ == '__main__':
    reverse_integer(1360254)




















