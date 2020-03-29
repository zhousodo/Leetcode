# 双向链表就是 节点和节点之间有两个指针相连的链表

#这里有必要说明一下 头指针和头节点的 问题，
""":param
    头指针：指向第一个存储数据节点的指针
    头节点：有两种说法：只是一个节点，一般来说本身不存放内容
                       第二种说法是：头节点是一个正常的节点
"""

class Node(object):
    """节点信息"""
    def __init__(self,item):
        """
        item : 数据项
        _next : 向后指针
        pre: 向前指针

        """
        self.item= item
        self._next= None
        self.pre=None



class doublelinklist(object):
    def __init__(self):
        # 头指针
        self._head= None

    #############################
    #定义几个函数，增删改查，长度，空，（修改元素暂时不写）
    #############################
    def isempty(self):
        return self._head==None

    def length(self):
        cur= self._head
        count= 0
        while  cur!= None:
            count= count+1
            cur= cur._next

        #print('此时链表长度为：',count)
        return count

    def travel(self):
        cur= self._head
        while cur!= None:
            print(cur.item)
            cur= cur._next


    def start_add(self,item):
        node= Node(item)
        if self.isempty():
            self._head= node
        else:
            node._next=self._head
            self._head.pre= node
            self._head=node

    def end_add(self,item):
        node= Node(item)
        if self.isempty():
            self._head= node
        else:
            cur= self._head
            while  cur._next!= None:
                cur= cur._next
            cur._next=node
            node.pre= cur

    def insert(self,pos, item):
        if pos<=0:
            self.start_add(item)
        elif pos>(self.length()-1):
            self.end_add(item)

        else:
            node= Node(item)
            cur= self._head
            count= 0
            while  count<(pos-1):
                count+=1
                cur= cur._next
            # 将node的prev指向cur
            node.prev = cur
            # 将node的next指向cur的下一个节点
            node._next = cur._next
            # 将cur的下一个节点的prev指向node
            cur._next.prev = node
            # 将cur的next指向node
            cur._next = node

    # def remove(self,item):
    #     if self.isempty():
    #         return
    #
    #     else:
    #         cur= self._head
    #         if cur.item== item:
    #             # 首位元素是要找的节点
    #             if cur.pre==None:
    #                 cur= cur._next
    #                 cur._next.pre=None
    #             # 末尾元素是要找的元素
    #             elif cur.next== None:
    #                 #self._head= None
    #                 cur.pre._next=None
    #                 cur=None
    #
    #             # 其他元素是要找的节点， 只需要断开就可以
    #             else:
    #                 # cur._next.pre= None
    #                 #
    #                 # self._head= cur._next
    #                 cur.pre._next=cur._next
    #                 cur._next.pre=cur.pre



    def remove(self, item):

        """删除元素"""
        """:raise
           这里需要解释一下为啥
           如果首节点是要删除的节点，（此时还有一个无效节点！！！！）或者是尾节点 只要要指针给指空就可以
            如果是首节点，但是后面仍然有有效节点，那么就是正常的操作了， 第二个有效节点的pre = none
            _head 指到第二个节点 
            如果要删除的节点在中间，这个就需要正常操作了，
        
        """
        if self.isempty():
            return
        else:
            cur = self._head
            if cur.item == item:
                # 如果首节点的元素即是要删除的元素
                if cur._next == None:
                    # 如果链表只有这一个节点
                    self._head = None
                else:
                    # 将第二个节点的pre设置为None
                    cur._next.pre = None
                    # 将_head指向第二个节点
                    self._head = cur._next
                return
            while cur != None:
                if cur.item == item:
                    # 将cur的前一个节点的next指向cur的后一个节点
                    cur.pre._next = cur._next
                    # 将cur的后一个节点的pre指向cur的前一个节点
                    cur._next.pre = cur.pre
                    break
                cur = cur._next



    def search(self,item):
        cur= self._head
        while  cur!= None:
            if cur.item== item:
                return  True
            cur= cur._next

        return False

if __name__ == '__main__':
    ll = doublelinklist()
    ll.start_add(1)
    ll.start_add(2)
    ll.end_add(3)
    ll.isempty()
    print("列表长度为：",ll.length())

    print('遍历结果为：')
    ll.travel()
    print('.........')
    ll.insert(4, 4)
    ll.travel()
    print('.......')
    ll.remove(3)
    ll.travel()
    # ll.insert(4, 5)
    # ll.insert(0, 6)





