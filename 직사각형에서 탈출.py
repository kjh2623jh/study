x, y, w, h = map(int, input().split())
a = w-x if x>w-x else x
b = h-y if y>h-y else y
print(a if a<b else b)