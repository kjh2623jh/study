import random
import time

def check(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        arr = func(*args, **kwargs)
        print(f"time: {time.time()-start:<25} result: {'correct' if arr==sorted(bubble_list) else 'fail'}")
    
    return wrapper

'''
@check
def bubble_sort(arr):
    for i in range(len(arr),0,-1):
        c=1
        for j in range(i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                c=0
        if c:
            return arr
'''
@check
def bubble_sort(arr):
    end = len(arr) - 1
    while end > 0:
        last_swap = 0
        for i in range(end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                last_swap = i
        end = last_swap
    return arr


for _ in range(10):
    bubble_list = [random.randint(0,999) for _ in range(1000)]
    bubble_sort(bubble_list)