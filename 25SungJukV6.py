# 성적 처리 프로그램 v6
# 이름, 국어, 영어, 수학을 입력 받으면
# 총점, 평균, 학점을 계산하고 출력함
# CRUD 기능을 지원하는 성적처리 프로그램으로  (CRUD : Create, Read, Update, Delete)
# 재작성하기 위해 메뉴 UI 추가
# 즉, 성적 입력, 조회, 상세조회, 수정, 삭제 기능을 구형
# 각 기능은 메뉴식으로 구현 - 기능별 메뉴 선택시 해당 명령 수행
# 학생의 성적 데이터는 개별 변수가 아닌 리스트 안에 리스트 형태로 저장

# 리스트 형태로 저장된 성적데이터는 csv형식으로 변환해서
# sungjuk.dat에 저장해 둠

import sys
import yoon.sungJukv6 as sjv6


# 메뉴 출력 및 메뉴별 처리
while True:
    # 메뉴 입력받음
    menu = sjv6.displayMenu()

    if menu == '1':
        print('성적 데이터 추가')
        sj = sjv6.readSungJuk()
        sjv6.addSungJuk(sj)
        sjv6.loadSungJuk()

    elif menu == '2':
        print('성적 데이터 조회')
        sjv6.showSungJuk()

    elif menu == '3':
        print('성적 데이터 상세조회')
        pass
    elif menu == '4':
        print('성적 데이터 수정')
        pass
    elif menu == '5':
        print('성적 데이터 삭제')
        pass
    elif menu == '0':
        print('프로그램 종료')
        sys.exit(0)
    else:
        print('메뉴를 잘못 선택하셨습니다!!')



