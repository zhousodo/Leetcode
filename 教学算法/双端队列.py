# 队列的两端都可以入队和出队
class Deque(object):
    def __init__(self):
        self.items=[]

    def isempty(self):
        return self.items==[]
    def add_front(self,item):
        self.items.insert(0,item)
    def add_rear(self,item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop(len(self.items)-1)
    def size(self):
        return len(self.items)
    def travel(self):
        print(self.items)

if __name__ == "__main__":
    deque = Deque()
    deque.add_front(1)
    deque.add_front(2)
    deque.add_rear(3)
    deque.add_rear(4)
    deque.travel()