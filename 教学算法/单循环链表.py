###就是最后一个节点指向第一个节点

class Node(object):
    def __init__(self,item):
        self.item= item
        self._next= None


class synclinklist(object):
    def __init__(self):
        self.head= None

    def isempty(self):
        return self.head==None

    def length(self):
        # cur= self.head
        # count=0
        #需要注意，这里没有一个空指针，也就是所最后一个指针同样有效，指向第一个节点
        if self.isempty():
            return 0
        else:
            count=1
            cur= self.head._next

            while cur!=self.head:
                count+=1
                #print(count)
                cur=cur._next
            #print(count)
            return count
    def travel(self):
        """:raise
            这里遍历和其他的链表不一样，因为首尾相连接
            所以需要考虑一下第一个节点和最后一个节点
        """
        if self.isempty():
            # print('表是空的，你让我遍历个锤子！！！ ')
            return

        cur= self.head
        print(cur.item)
        while cur._next!=self.head:

            cur= cur._next
            print(cur.item)

    def start_add(self, item):
        """头部添加节点"""
        node = Node(item)
        if self.isempty():
            self.head = node
            node._next = self.head
        else:

            # node._next = self.head
            # cur = self.head
            # while cur._next != self.head:
            #     cur = cur._next
            # cur._next = node
            # # _head指向添加node的
            # self.head = node
            node._next=self.head
            cur=self._head
            while cur._next!= self.head:
                cur= cur._next
            cur._next= node
        self._head= node


    def end_add(self,item):
        node = Node (item)
        if self.isempty():
            self.head= node
            node._next= self.head
        else:
            cur= self.head
            while  cur._next != self.head:
                cur= cur._next

            cur._next= node
            node._next= self.head

    def insert(self,pos, item):
        if pos<0:
            self.start_add(item)
        elif pos>(self.length()-1):
            self.end_add(item)

        else:
            node= Node(item)
            cur= self.head._next
            count=1
            while count<(pos-1):
                count+=1
                cur= cur._next
            node._next= cur._next
            cur._next= node

    def remove(self,item):
        if self.isempty():
            raise  ValueError('this is a null link list ')

        elif item == 0:
            cur = self.head
            if cur._next != self.head:
                while cur._next != self.head:
                    cur = cur._next
                cur._next = self.head._next
                self.head = self.head._next
        else:
            cur = self.head
            num = 1
            while cur._next != self.head:
                if num == item:
                    break
                cur = cur._next
                num += 1
            cur._next = cur._next._next

    def search(self,item):
        if self.isempty():
            return False
        cur = self.head
        if cur.item== item:
            return True
        while  cur._next != self.head:
            cur= cur._next
            if cur.item== item:
                return True

        return False

    def __getitem__(self, item):
        pass
    def __setitem__(self, key, value):
        pass


if __name__ == '__main__':

    ll= synclinklist()
    ll.start_add(0)
    ll.start_add(2)
    ll.start_add(3)
    ll.end_add(3)
    ll.end_add(3)
    x= ll.length()
    print('长度为：',x )
    print('.............')
    ll.insert(3,99)
    ll.travel()
    print('移除第三个元素元素后序列为：')
    ll.remove(3)
    print('.............')
    ll.travel()





