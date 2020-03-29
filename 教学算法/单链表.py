
class Singlelinknode(object):
    """
    节点类
    """
    def __init__(self,item):

        self.item= item
        self._next= None

class Singlelinklist(object):
    """
    单链表抽象结构
    """
    def __init__(self):
        self._head =None

    def isempty(self):
        #判断链表是否为空

        #return self._head is None
        if self._head ==None:
            print('the linklist is none')

        else:
            print('链表不是空的，放心增删吧！！')


    def length(self):
        """
        采用count++ 的统计方式来计算link 的长度
        :return:
        """
        #pass
        cur= self._head
        count= 0
        while cur!= None:
            count= count+1
            cur= cur._next
        #print("the linklist length is :", count)
        print('链表长度为：',count)
        return count



    def travel(self):
        cur= self._head

        while  cur != None:
            print(cur.item)

            cur= cur._next

        print('遍历结束....')

    def start_node_add(self,item):
        """
        一个空链表，等于说新建一个链表
        :param item:
        :return:
        """
        node= Singlelinknode(item)
        node._next= self._head
        self._head= node

    def end_node_add(self,item):
        """
        在尾部加入元素，
        :param item:
        :return:
        """
        node = Singlelinknode(item)
        # 判断是否是空表， 如果是 将——head 只想新的节点 nodes
        if self.isempty():
            self._head= node
        else:
            cur= self._head
            while  cur._next!= None:
                cur= cur._next
            cur._next= node

    def node_insert(self, position , item):
        # 再指定的位置插入元素 需要知道该位置的前一个位置信息

        if position< 0:
            self.start_node_add(item)
        elif position> (self.length()-1):
            self.end_node_add(item)

        else:
            node =Singlelinknode(item)
            count= 0
            # pre  用来指向position 的前一个位置
            pre=self._head
            while count< (position-1):
                count= count+1
                pre=pre._next

            node._next= pre._next
            pre._next= node
        print('插入成功！！！')

    def remove(self,item):
        """
        移除元素， 需要知道前一个元素的位置 pre 表示
        :param item:
        :return:
        """


        cur = self._head
        pre = None
        while cur != None:
            # 找到了指定元素
            if cur.item == item:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self._head = cur._next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur._next
                break
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur._next

    def search_node(self,item):
        cur= self._head
        while  cur!= None:
            if cur.item== item:
                return True
            cur= cur._next

    def clear(self):
        self._head= None

    #链表长度 可以直接调用该函数
    # def __len__(self):
    #     print(self.length())
    #     return self.length()

    # get set 方法

    def __getitem__(self, item):
        pass
    def __setitem__(self, key, value):
        pass




if __name__ == '__main__':
    ll=Singlelinklist()
    ll.start_node_add(1)
    ll.start_node_add(1)
    ll.start_node_add(1)
    ll.start_node_add(1)
    ll.start_node_add(1)
    ll.start_node_add(1)
    ll.length()
    ll.end_node_add(3)
    ll.length()
    # ll.search_node(1)
    # ll.start_node_add(4)
    # ll.isempty()
    ll.node_insert(2,9)
    ll.travel()
    #ll.length()

