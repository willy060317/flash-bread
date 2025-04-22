stock ={"팥붕어빵": 10, "슈크림붕어빵": 8, "초코붕어빵": 5}

sales ={"팥붕어빵": 0, "슈크림붕어빵":0, "초코붕어빵": 0}

def order_bread():
    while True:
        bread_type = input("주문할 붕어빵의 종류를 입력하세요(팥붕어빵, 슈크림붕어빵, 초코붕어빵)만약 뒤로가기를 원하시면 뒤로가기 눌러주세요 ")
        if bread_type == "뒤로가기":
            break
        if bread_type in stock:
            bread_count = int(input("주문할 게수를 입력하세요"))
            if stock[bread_type]>=bread_count:
                stock[bread_type]-= bread_count
                sales[bread_type]+= bread_count
                print(f"{bread_type} {bread_count}개가 판매되었음")
            else:
                print("재고가 부족합니다")
                print(f'지금 주문 할 수 있는 {bread_type}의수량은 {stock[bread_type]} 입니다')
        else:
            print("다시 주문해주세요")
while True:
    mode = input("원하는 모드를 선택하세요(주문, 관리자, 종료): ")
    if mode == "종료":
        break
        print("시스템이 종료되었습니다")
    elif mode == "주문":
        order_bread()
    elif mode == "관리자":    
        admin_mode()
    
    
