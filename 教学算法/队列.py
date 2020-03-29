class Queue(object):
    def __init__(self):
        self.items=[]

    def isempty(self):
        return self.items==[]
    def inqueue(self,item):
        self.items.insert(0,item)

    # def inqueue2(self,pos, item):
    #     self.items.insert(pos,item)
    def outqueue(self):
        return self.items.pop()

    def size(self):
        print('此时队列的size为：')
        return len(self.items)

if __name__ == '__main__':

    q=Queue()
    q.inqueue(1)
    q.inqueue(1)
    q.inqueue(1)
    q.inqueue(1)
    q.inqueue(1)
    print(q.size())
    q.outqueue()
    q.outqueue()
    q.outqueue()

    print(q.size())


