# 问题一
# i的3阶次方 1-n 求和 这里n=100
def i_sum():
    """
    时间复杂度和n 有关系为o(n)
    :return:
    """
    n=int(input("n\n "))
    if int(n)>0:

        sum=0
        i=1
        for i in range(1,n+1):
            sum= sum+i*i*i
        print(sum)
    else:
        print('error')
#问题二
#阶乘以及Fibnacci数列 
def jiecheng():
    """
    由于只有一个for循环 所以时间复杂度为o(n)
    :return:
    """
    sum=1
    n=int(input("please input the number you want n: \n"))
    if n < 0 :
        return  False
    elif n==0:
        print('1')
    else:
        for i in  range(1,int(n)):
            sum=sum*n
    print('1!+...+%d! 的阶乘为 %d ' %(n,sum))

def Fib(n):
    """
     这里用了一个简单的递归，时间复杂度比较大为o(2^n), 二叉树
    :param n:     20
    :return:
    """

    if n<0:
        print('error')
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:

       return Fib(n-1)+Fib(n-2)
    print(Fib(n-1)+Fib(n-2))
#问题三
#最大子序列问题

def maxsubarray(numbs):
    """
    这里需要注意使用的是贪心算法  时间复杂度为一个for循环所以为o(n)
    解释一下： 贪心算法每一步都要求是局部最优解，所以 到最后就是最优解
    :param numbs: list[int]
    :return:  sum
    测试实例 maxsubarray([1,-1,2,3])

    """
    n =len(numbs)
    curr_sum= max_sum=numbs[0]
    for i in range(1,n):
        curr_sum= max(numbs[i],curr_sum+numbs[i])
        max_sum=max(max_sum,curr_sum)

    print(max_sum)
    return max_sum

# 问题四
# 二分查找

def erfen(lst, value, low, high):
    """
    二分查找时间复杂度为o(n) 递归在这里用不舒服
    :param lst:  list[int 2n个]
    :param value: int
    :param low:  0
    :param high: len(lst)-1
    :return: mid
    测试实例 erfen([5,7,8,9,7],8,0,4)
    """

    if high < low:
        return None
    mid = int((low + high) / 2)
    if lst[mid] > value:
        return erfen(lst, value, low, mid-1)
    elif lst[mid] < value:
        return erfen(lst, value, mid+1, high)
    else:
        print(mid)
        return mid

#问题五
#欧几里得算法
def gcd(m,n):
    """
    :param m:  int
    :param n: int
    :return:
    测试实例 gcd(50,15)
    """
    while n>0:
        rem=m%n
        m=n
        n= rem
    print(m)
    return m

#问题六
#取幂运算
def myPow( x: float, n: int) -> float:
    """
    时间复杂度为o(logn)
    :param x: float
    :param n: int
    :return: float
    测试实例 print(myPow(9,2))
    """
    judge = True
    if n < 0:
        n = -n
        judge = False
    final = 1
    while n > 0:
        if n % 2 == 0:
            x *= x
            n //= 2
        final *= x
        n -= 1
    return final if judge else 1 / final

# 问题七
#判断互为素数
def hs(m,n):
    """
    时间复杂度为o(logn)
    :param m:
    :param n:
    :return:
    测试实例 hs(50,4)
    """
    def gcd(m, n):

        while n > 0:
            rem = m % n
            m = n
            n = rem
        #print(m)
        return m
    if gcd(m,n)==1:
        print('互为素数')
    else:
        print('no 不互为素数')


if __name__ == '__main__':

    #i_sum()
    #jiecheng()
    #print(Fib(20))

    #maxsubarray([1,-1,2,3])
    #erfen([5,7,8,9,7],8,0,4)
    #gcd(50,15)
    #print(myPow(9,2))
    hs(50,4)