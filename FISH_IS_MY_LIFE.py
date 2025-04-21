붕어빵=[팥_붕어빵:10, 슈크림_붕어빵:10, 초코_붕어빵:10]
while True:
    mode = input("원하는 모드를 선택하세요(주문, 관리자, 종료): ")
    if mode == "종료":
        break
        print("시스템이 종료되었습니다")
    elif mode == "주문": 
        맛 = input("맛의 종류를 입력하세요")

        수량  = input("수량을 입력하세요")
    elif mode == "주문":
        order_bread()
    elif mode == "관리자":    
        admin_mode()