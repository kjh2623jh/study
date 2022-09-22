import random
import time


class insertion:
    def __init__(self, arr):
        self.arr=arr

    def __repr__(self):
        return str(self.arr)

    def sort(self):
        self.insertion_sort(self.arr)

    def insertion_sort(self, arr):
        for end in range(1, len(arr)):
            to_insert = arr[end]
            i = end
            while i > 0 and arr[i - 1] > to_insert:
                arr[i] = arr[i - 1]
                i -= 1
            arr[i] = to_insert
        # return 안해줘도 <list>.sort() 같이 in-place sort 할 수 있음.

    def check(self):
        start = time.time()
        s_insertion_list = sorted(self.arr)
        self.insertion_sort(self.arr)
        print(f"time: {time.time()-start:<25} result: {'correct' if self.arr==s_insertion_list else 'fail'}")


if __name__=="__main__":
    for _ in range(10):
        insertion_list = insertion([random.randint(0,999) for _ in range(1000)])
        insertion_list.check()