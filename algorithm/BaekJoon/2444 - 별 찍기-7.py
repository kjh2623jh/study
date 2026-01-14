# https://www.acmicpc.net/problem/2444

number = int(input())

star_arr = []

for i in range(number):
    a = i+1
    star_arr.append(" " * (number-a) + "*" * (a+i))
# for i in range(number-1):
#     a = i+1
#     print(" " * a + "*" * ((number-a)+(number-(a+1))))
[star_arr.append(star_arr[number-x]) for x in range(2, number+1)]
print("\n".join(star_arr))

# 100점