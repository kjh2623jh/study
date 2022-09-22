# def solution(price, money, count):
#     for i in range(1,count+1):
#         money-=price*i
#     return -money if money<0 else 0

solution=lambda p,m,c:a-m if (a:=sum([p*i for i in range(1,c+1)]))-m>0 else 0
#100점


if __name__ == "__main__":
    print(solution(3, 20, 4)) # 10



''' 등차수열의 합
def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)


solution=lambda p,m,c:max(0,p*(c+1)*c//2-m)
'''