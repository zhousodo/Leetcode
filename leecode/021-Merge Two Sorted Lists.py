""":raise

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""
class ListNode():
    def __init__(self,x ):
        self.val= x
        self.next= None

class Linklist():
    def mergeTwoLists(self,l1,l2):
        """
        dummy= cur  这个是为了记住自己的头指针
        """
        date=[]
        dummy=cur= ListNode(0)
        while l1 and l2:
            if l1.val<l2.val:
                cur.next= l1
                l1= l1.next
            else:
                cur.next= l2
                l2= l2.next
            date.append(cur.val)
            print(date)
            cur= cur.next

        #如果一个链表使用完了，就自动追加剩余链表的多余部分
        cur.next= l1 or l2
        return dummy.next

