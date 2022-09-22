import random
import time

def check(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        s_merge_list = sorted(merge_list)
        arr = func(*args, **kwargs)
        # print(arr)
        # print()
        # print(sorted(merge_list))
        # for i in zip(arr,sorted(merge_list)):
            # print(f"{i} {'1' if i[0]==i[1] else '0'}")
        # print(f"time: {time.time()-start:<25} result: {'correct' if arr==sorted(merge_list) else 'fail'}")
        print(f"time: {time.time()-start:<25} result: {'correct' if merge_list==s_merge_list else 'fail'}")
    
    return wrapper

@check
def MergeSrot(arr):
    return merge_sort(arr)
'''
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr
'''
'''
def merge_sort(arr):
    len_arr = len(arr)
    if len_arr==1: return arr
    mid=len_arr//2
    # lo,hi = merge_sort(arr[:mid]),merge_sort(arr[mid:])
    # result=[0]*len_arr
    # p1=p2=cnt= 0
    # while cnt<len_arr:
    #     try:
    #         if lo[p1]<hi[p2]:
    #             result[cnt]=lo[p1]
    #             p1+=1
    #         else:
    #             result[cnt]=hi[p2]
    #             p2+=1
    #         cnt+=1
    #     except IndexError:
    #         if p1<p2:
    #             result[cnt]=lo[p1]
    #             p1+=1
    #         else:
    #             result[cnt]=hi[p2]
    #             p2+=1
    #         cnt+=1
    arr = merge_sort(arr[:mid])+merge_sort(arr[mid:])
    lo,hi,j = 0,mid,0
    for i in range(len_arr-1):
        if arr[lo]<arr[hi]:
            arr[i],arr[lo]=arr[lo],arr[i]
            lo,j = i,0
            lo+=1
        else:
            arr[i],arr[hi]=arr[hi],arr[i]
            if not j: lo,j =hi,1
            hi=hi+1 if hi<len_arr else hi
        if lo>=hi or hi>=len_arr: break
    return arr
    # return result
'''
# in-place sort
def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))

for _ in range(10):
    merge_list = [random.randint(0,999) for _ in range(1000)]
    MergeSrot(merge_list)