# 栈可以用顺序表实现也可以用链表来实现

class Stack(object):
    # 这里用顺序list 实现
    def __init__(self):
        self.items= []
    def isempty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    # def pop(self,item):
    #     self.items.pop(item)
    # 出栈只有一种可能 所以不用再设定item
    def pop(self):
        self.items.pop()

    def peek(self):
        """
        返回栈顶元素
        :return:
        """
        print('栈顶元素为',self.items[len(self.items) - 1])
        return self.items[len(self.items)-1 ]


    def search(self,pos):
        if self.items==[]:
            return False
        else:

            print(self.items[pos])
            return self.items[pos]


    def size(self):
        # 得到栈的大小
        return len(self.items)


if __name__ == '__main__':
    stack = Stack()
    stack.push("hello")
    stack.push("world")
    stack.push("itcast")

    print(stack.size())

    stack.peek()

    stack.search(2)
    # stack.pop()
    # 
    # stack.pop()
    # 
    # stack.pop()
    print(stack.size())

   # stack.peek()