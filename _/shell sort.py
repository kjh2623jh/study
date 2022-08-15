import random
import time


def check(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        arr = func(*args, **kwargs)
        print(f"time: {time.time()-start:<25} result: {'correct' if arr==sorted(shell_list) else 'fail'}")
    
    return wrapper

@check
def shell_sort(arr):
    k=len(arr)//2
    if k%2==0: k+=1
    while 1:
        for i in range(k):
            ...
        if k==1: break
        k//=2
        if k%2==0:k+=1

def shell_sort(arr):
    N = len(arr)
    h = N // 2
    while h > 0:
        for i in range(h, N):
            temp = arr[i]
            j = i - h
            while j >= 0 and arr[j] > temp:
                arr[j + h] = arr[j]
                j -= h
            arr[j + h] = temp
        h //= 2
    return arr

# 출처: https://tosuccess.tistory.com/124 [EI_HJ]



for _ in range(10):
    shell_list = [random.randint(0,999) for _ in range(1000)]
    shell_sort(shell_list)

# a=insertion_sort.insertion([random.randint(0,999) for _ in range(1000)])
# a.sort()
# print(a)