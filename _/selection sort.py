import random
import time

def check(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        arr = func(*args, **kwargs)
        print(f"time: {time.time()-start:<25} result: {'correct' if arr==sorted(selection_list) else 'fail'}")
    
    return wrapper

@check
def selection_sort(arr):
    len_arr = len(arr)
    for i in range(len_arr):
        min_idx = i
        for j in range(i, len_arr):
            if arr[j]<arr[min_idx]: min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr


for _ in range(10):
    selection_list = [random.randint(0,999) for _ in range(1000)]
    selection_sort(selection_list)