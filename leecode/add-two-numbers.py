"""
输入：（2-> 4-> 3）+（5-> 6-> 4）
 输出： 7-> 0-> 8
 说明： 342 + 465 = 807。

"""
class listNode:
    def __init__(self,x ):
        self.val= x
        self.next=None
# class Solution:
#     def addnumber( self,l1,l2):
#         if l1==None:
#             return l2
#         if l2==None:
#             return l1
#         val1,val2=[l1.val],[l2.val]
#
#         while l1.next:
#             val1.append(l1.next.val)
#             l1=l1.next
#         while l2.next:
#             val2.append(l2.next.val)
#             l2=l2.next
#
#         num1= ''.join([str(i) for i in val1[::-1]])
#         num2= ''.join([str(i) for i in val2[::-1]])
#         tmp= str(int(num1)+int(num2))[::-1]
#         res= listNode(int(tmp[0]))
#         run_res= res
#         for i in range(1,len(tmp)):
#             run_res.next= listNode(int(tmp[i]))
#             run_res= run_res.next
#         print(res)
#         return res
#
#
# if __name__ == '__main__':
#     l1=[]
#     #l1.append(int(243))
#     l1.append(2)
#     l1.append(4)
#     l1.append(3)
#     print(l1)
#
#     l2=[]
#     l2.append(5)
#     l2.append(6)
#     l2.append(4)
#     #l2.append(int(564))
#     print(l2)
#     sl= Solution()
#     sl.addnumber(l1.val,l2.val)
#
#
