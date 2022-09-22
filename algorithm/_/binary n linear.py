from statistics import linear_regression
import time
import random

start=time.time()
number = random.randint(10**5,10**7)
print(f'number: {number}')
arr = list(range(10**7))


def check(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        num = func(*args, **kwargs)
        print(f"time: {time.time()-start:<25} result: {num}")
    
    return wrapper


@check
def PyIndex(arr):
    return arr.index(number)

@check
def LinearSearch(arr):
    for i in range(len(arr)):
        if arr[i]==number:
            return i
    else:
        return -1

@check
def BinarySearch(*args):
    return binary_search(*args)
def binary_search(arr, number, start, end):
    mid = (start+end)//2
    if start>=end:
        return mid
    if arr[mid] < number:
        return binary_search(arr,number,mid+1,end)
    elif arr[mid] > number:
        return binary_search(arr,number,start,mid-1)
    
    return mid
'''
def BinarySearch(arr, number): # 오름차순
    start = 0
    end = len(arr)-1
    while start<end:
        mid = (start+end)//2
        if arr[mid] < number:
            start = mid+1
        elif arr[mid] > number:
            end = mid-1
        else:
            return mid
'''

import bisect
@check
def bisectSearch(arr):
    return bisect.bisect(arr,number)


if __name__=="__main__":
    PyIndex(arr)
    LinearSearch(arr)
    BinarySearch(arr,number,0,len(arr)-1)
    bisectSearch(arr)