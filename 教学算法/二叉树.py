class Node(object):
    def __init__(self,value=-1,lchild=None,rchild= None ):
        self.value= value
        self.lchild= lchild
        self.rchild= rchild


# 创建树的类， 并给出一个root节点  一开始为空，随后添加节点，

class Tree(object):
    def __init__(self,root= None):
        self.root= root

    def add(self,value):
        "为树添加节点"
        node = Node(value)
        if self.root== None:
            self.root= node
        else:
            # 用队列存储每一个节点的信息， 然后找到位置，再加入节点
            queue=[]
            queue.append(self.root)

            while  queue:
                # 弹出第一个元素
                cur= queue.pop(0)
                if cur.lchild== None:
                    cur.lchild= node
                    return
                elif cur.rchild== None:
                    cur.rchild=node
                    return
                else:
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

