# https://www.cnblogs.com/king-ding/p/pythonchaintable.html

class Node(object):
    def __int__(self,date,pnext=None):
        """

        :param date: 数据
        :param pnext:  指向下一个元素的指针
        :return:
        """
        self.data=date
        self._next= pnext

    def __repr__(self):
        """

        :return: 返回原始数据
        """
        return  str(self.data)

class ChainTable(object):
    def __init__(self):
        self.head= None
        self.length=0

    def isEmpty(self):
        return (self.length==0)
    def append(self, data_or_node):
        item= None
        if isinstance(data_or_node,Node):
            item= data_or_node
        else:
            item=Node
        if not self.head:
            self.head= item
            self.length+=1
        else:
            node= self.head
            while node._next:
                node=node._next
            node