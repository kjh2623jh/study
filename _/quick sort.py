import random
import time

def check(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        s_quick_list=sorted(quick_list)
        arr = func(*args, **kwargs)
        # print(f"time: {time.time()-start:<25} result: {'correct' if arr==sorted(quick_list) else 'fail'}")
        print(f"time: {time.time()-start:<25} result: {'correct' if quick_list==s_quick_list else 'fail'}")
    
    return wrapper


'''
# @check  : return 한 번 하면 끝나는데 재귀함수식이라 바로 decorator 넣으면 안됨.
def quick_sort(array=[]) -> list:
    arr = array.copy()
    if len(arr) < 2: return arr
    pivot = arr.pop()
    lo = 0
    hi = len(arr)-1
    while 1:
        while lo<=hi and arr[lo]<=pivot: lo+=1
        while lo<=hi and arr[hi]>pivot: hi-=1
        if lo>hi: break
        arr[lo],arr[hi]=arr[hi],arr[lo]

    return quick_sort(arr[:lo]) + [pivot] + quick_sort(arr[lo:])
'''
'''
재귀함수는로 구현하면 간결하고 이해하기 쉽지만 매번 재귀 호출될 때 마다 새로운 리스트를 생성하여 리턴하기 때문에 메모리 사용 측면에서 비효율적이다.
큰 사이즈의 입력 데이터를 다뤄야하는 상용 코드에서는 이러한 단점은 치명적으로 작용할 수 있기 때문에 추가 메모리 사용이 적은 in-place 정렬이 선호된다.
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)
'''
def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)


@check
def quick_sort_c(arr):
    return quick_sort(arr)

for _ in range(10):
    quick_list = [random.randint(0,999) for _ in range(1000)]
    quick_sort_c(quick_list)