# 사원 등록 프로그램


import sys
from yoon.oop.services import EmpService as empsrv


while True:
    menu = empsrv.display_manu()

    if menu == '1':
        print('사원 데이터 추가')
        empsrv.add_emp()

    elif menu == '2':
        print('사원 데이터 조회')
        empsrv.show_emp()

    elif menu == '3':
        print('사원 데이터 상세 조회')
        empsrv.showone_emp()

    elif menu == '4':
        print('사원 데이터 수정')
        empsrv.modify_emp()

    elif menu == '5':
        print('사원 데이터 삭제')
        empsrv.remove_emp()

    elif menu == '0':
        print('프로그램 종료')
        sys.exit(0)
    else:
        print('메뉴를 잘못 선택하셨습니다!')