from fishbread_model import Breadshop

shop= Breadshop()

while True:

    mode = input("원하는 모드를 선택하세요(주문, 관리자, 종료,현상태보기,총 판매한 값: ")
    if mode == "종료":
        shop.calculate_sales()
        break
        print("시스템이 종료되었습니다")
    elif mode == "주문":
            order_bread()
    elif mode == "관리자":    
            admin_mode()
    elif mode == "현상태보기":
            current_mode()
        
