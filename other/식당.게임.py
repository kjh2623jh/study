import random
from time import sleep

def open():
    current_people_count = 0
    people_in = 0
    people_out = 0
    total_time=0
    money=0
    while total_time<day_time:
        time = random.randrange(1,people_time_distance)
        total_time+=time

        sleep(time)
        if current_people_count<table:
            people_in = random.randrange(0,coming_people)
            people_out = random.randrange(0,going_people) if current_people_count != 0 else 0
            if people_out > people_in: people_out = people_in
            current_people_count+=people_in
            current_people_count-=people_out
            if current_people_count > table:
                print(f"손님이 {people_in}명 들어오고, {people_out}명 나가셨지만, 현재 식당이 꽉 차서 {people_in}명 중 {current_people_count-table}명은 도로 돌아가셨습니다.")
                current_people_count=table
            else:
                if not people_out:print(f'손님이 {people_in}명 들어오셨습니다.') if people_in else print(f'아무일도 일어나지 않았습니다.')
                elif not people_in:print(f"손님이 {people_out}명 나가셨습니다.")
                else:print(f'손님이 {people_in}명 들어오시고, {people_out}명 나가셨습니다.')
                money+=price*people_out
        else:
            print("현재 식당이 만석이라 손님이 들어오시지 못했습니다.")
            people_out = random.randrange(1,going_people)
            print(f'손님이 {people_out}명 나가셨습니다.')
            current_people_count-=people_out
            money+=price*people_out
        print(f'현재 손님 수 : {current_people_count}')
    sleep(0.7)
    print(f'손님이 {current_people_count}명 나가셨습니다.')
    money+=price*current_people_count
    return money

def close(day, money):
    input("하루가 지나 영업을 종료하였습니다.")
    input(f"{day}일차 매출액은 {money}원 입니다.")
    if day == Dday:
        input(f"{day}일차가 되어 가게문을 닫았습니다.")
        input(f"현재까지 총 {total_money}원 벌었습니다.")
    else:
        input(f"현재까지 {total_money}원 벌었습니다.")
        input(f"가게 문 닫기까지 {Dday-day}일 남았습니다.")
        if input("상점에 입장하려면 아무 텍스트를 입력한 후 enter를 눌러주세요.\n") != '':
            shop()

def shop():
    global info

    while True:
        print(f'''
    -------------상점---------------
    0~6 사이의 숫자를 입력 해 주세요.
    아무것도 입력하지 않으면 상점에서 나가집니다.
    현재 {total_money}원 가지고 있습니다.
    0. 정보 보기
    1. 테이블 1개 : {shop_product['table']}원
    2. 음식 가격 +500원 : {shop_product['price']}원
    3. 운영 시간 +30초 : {shop_product['day_time']}원
    4. 손님 출입 간격 -1초 : {shop_product['people_time_distance']}원
    5. 최대 입장 손님 수 +1 : {shop_product['coming_people']}원
    6. 최대 퇴장 손님 수 -1 : {shop_product['going_people']}원
    --------------------------------
        ''')
        answer = input()
        try:
            answer = int(answer)
            if not answer: input(info)
            elif answer == 1:
                if price_ck('table'):
                    global table
                    table += 1
            elif answer == 2:
                if price_ck('price'):
                    global price
                    price += 500
            elif answer == 3:
                if price_ck('day_time'):
                    global day_time
                    day_time += 30
            elif answer == 4:
                global people_time_distance
                if people_time_distance==1:print('더이상 구입할 수 없습니다.')
                elif price_ck('people_time_distance'):
                    people_time_distance -= 1
            elif answer == 5:
                if price_ck('coming_people'):
                    global coming_people
                    coming_people += 1
            elif answer == 6:
                global going_people
                if going_people==1:print('더이상 구입할 수 없습니다.')
                elif price_ck('going_people'):
                    going_people -= 1
            else:input("잘못입력하셨습니다.")
            info = info_update()
        except:
            if answer == '': break
            else:input("잘못입력하셨습니다.")

def price_ck(product):
    global total_money
    price = shop_product[product]
    if total_money < price:input("돈이 부족합니다.")
    else:
        total_money-=price
        input("성공적으로 구입하였습니다.")
        shop_product[product]+=5000
        return True

def info_update():
    return (f'''
    -------------정보---------------
    가게 테이블 수 : {table}개
    인당 음식 가격 : {price}원
    운영 시간 : {day_time}초
    손님 출입 간격 : 1~{people_time_distance}초
    들어시는 손님 수 : 0~{coming_people}명
    나가시는 손님 수 : 0~{going_people}명
    넘어가기 : enter
    --------------------------------
    ''')

if __name__ == "__main__":
    shop_product = {
        'table':15000,
        'price':15000,
        'day_time':20000,
        'people_time_distance':10000,
        'coming_people':15000,
        'going_people':15000
        }

    total_money = 0
    Dday = int(input("몇일 동안 일하실지 입력해주세요.\n"))
    table = 6
    price = 1000
    day_time = 30
    people_time_distance = 10
    coming_people = 3
    going_people = 3
    info = info_update()

    input(info)
    for day in range(1, Dday+1):
        input(f"가게를 열었습니다.  {day} 번째 날.")
        money=open()
        total_money+=money
        close(day, money)