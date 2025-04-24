stock ={"팥붕어빵": 10, "슈크림붕어빵": 8, "초코붕어빵": 5}

sales ={"팥붕어빵": 0, "슈크림붕어빵":0, "초코붕어빵": 0}
price = {"팥붕어빵": 1000, "슈크림붕어빵":1200, "초코붕어빵": 1500}
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
#붕어빵 관리자
def admin_mode():
    while True:
            password =input("비밀번호를 입력해주세요")
            if password == int(0000):
                print("관리자 모드에 들어갑니다")
            else:
                birthday=input("임우진의 생일은?")
                if birthday =="0317":
                    new_password = input("새로운 패스워드 입력해주세요")
                    if new_password .isdight() and len(new_password) == 4:
                        print("다시 입력 해주세요 4자리 자연수가 아닙니다")
                    else:
                        print("비밀번호가 수정되었습니다")
                
                else:
                    print("잘못되었어요")
                 
            bread_type = input("채울 메뉴를 선택해 주세요,종료,뒤로가기 눌러주세요")
            if bread_type  == ("뒤로가기"):
                    break
            if bread_type in stock:
                bread_count = int(input("창고에 추가할 게수를 입력하세요"))
                stock[bread_type]+= bread_count
                print(f"{bread_type} {bread_count}개가 추가되었음")
            else:
                 print("그런 메뉴는 없어요")
def current_mode():
    while True:
         print(stock)
         break
def calculation_sales():
    # total_sales = sum(sales[key]*price[key] for key in sales)
    total = 0
    for k in sales:
         total += (sales[key]*price[key])
    print(f"오늘의 총 매출은 {total}원 입니다")
    
    
    
    
    while True:
        mode = input("원하는 모드를 선택하세요(주문, 관리자, 종료,현상태보기,총 판매한 값: ")
        if mode == "종료":
            break
            print("시스템이 종료되었습니다")
        elif mode == "주문":
            order_bread()
        elif mode == "관리자":    
            admin_mode()
        elif mode == "현상태보기":
            current_mode()
        
calculation_sales():