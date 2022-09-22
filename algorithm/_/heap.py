import random
import time


"""
힙(Heap): 완전 이진 트리의 일종으로 우선순위 큐를 위하여 만들어진 자료구조
최댓값, 최솟값을 쉽게 추출할 수 있는 자료구조
"""
class MyHeap:
    def __init__(self, arr=[]):
        self.heap = [None, ]
        for i in arr:
            self.append(i)
    
    def __repr__(self):
        return f"<MyHeap: {self.heap[1:]}>"
    
    def __len__(self):
        return len(self.heap[1:])

    def __getitem__(self, n):
        return self.heap[n+1]
    
    def __sum__(self):
        return sum(self.heap[1:])

    def __list__(self):
        return self.heap[1:]
    
    def __set__(self):
        return set(self.heap())
    
    def __sorted__(self, reverse: bool = False):
        temp=self.heap
        result=[0]*len(self.heap[1:])
        if reverse:
            self.heap=self.min_heap()
            for i in range(len(result)):
                result[i]=self.pop()
        else:
            for i in range(len(result)):
                result[i]=self.pop()
        self.heap=temp
        return result

    def __reversed__(self):
        return self.heap[::-1]
    
    def min_heap(self):
        result = [None,]
        for i in self.heap[1:]:
            result.append(i)
            child = len(result)-1
            while child!=1 and result[child] < result[(parent:=child//2)]:
                result[child],result[parent]=result[parent],result[child]
                child=parent
        
        return result[1:]
    
    def max(self):
        return self.heap[1]

    def min(self):
        return list(MyHeap.min_heap(self))[0]

    def append(self, num):
        self.heap.append(num)
        child = len(self.heap)-1
        while child!=1 and self.heap[child] > self.heap[(parent:=child//2)]:
            self.heap[child],self.heap[parent]=self.heap[parent],self.heap[child]
            child=parent

    def pop(self, num=1):
        result = self.heap[num]
        self.heap[num]=self.heap[-1]
        self.heap.pop()
        parent = num

        while 1:
            if self.heap[parent]<self.heap[(child:=parent*2)] or \
               self.heap[parent]<self.heap[(child:=parent*2+1)]:
                self.heap[parent],self.heap[child]=self.heap[child],self.heap[parent]
                parent=child
            else:
                break
        
        return result

if __name__=="__main__":
    a = MyHeap()
    a.append(2)
    a.append(50)
    a.append(20)
    a.append(2)
    a.append(2)
    a.append(2)
    a.append(2)
    a.append(2)
    print(a)
    print('len:',len(a))
    for i in a:
        print(i,end=', ')
    print()
    print('sum:',sum(a))
    print()

    b=MyHeap()
    start = time.time()
    for i in range(random.randint(99,99999)):
        b.append(random.randint(0,9999))
    print('len:',len(b))
    print('max:',b.max())
    print('min:',b.min())
    # print(b)
    print('time:',time.time()-start)
    print()

    c = MyHeap([1,5,23,6,2,78,2])
    print(c)
    print(reversed(c))

    d = MyHeap([1,1,415,5,6,3,23,46,3,23,45,32,2])
    print(f'''
{d} :d
{sorted(d)} :sorted
{d} :d
{sorted(d, reverse=True)} :sorted, reverse=True
{d} :d
    ''')