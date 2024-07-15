# 성적 처리 프로그램 v3
# 이름, 국어, 영어, 수학을 입력 받으면
# 총점, 평균, 학점을 계산하고 출력함
# CRUD 기능을 지원하는 성적처리 프로그램으로  (CRUD : Create, Read, Update, Delete)
# 재작성하기 위해 메뉴 UI 추가
# 즉, 성적 입력, 조회, 상세조회, 수정, 삭제 기능을 구형
# 각 기능은 메뉴식으로 구현 - 기능별 메뉴 선택시 해당 명령 수행


import sys

# 프로그램 메뉴 정의
main_menu = '''
==============================
     성적 프로그램 v3b
==============================
    1. 성적 데이터 추가 
    2. 성적 데이터 조회 
    3. 성적 데이터 상세조회 
    4. 성적 데이터 수정
    5. 성적 데이터 삭제 
    0. 성적 데이터 종료
==============================
'''

# 성적 데이터 관련 변수 선언
names = []
scoreKs = []
scoreEs = []
scoreMaths = []
tots = []
avgs = []
grds = []

# 메뉴 출력 및 메뉴 별 처리

for i in range(100):
    #  프로그램 주 실행부
    print(main_menu, end='')
    menu = input('=> 메뉴를 선택하세요 : ')

    # 선택한 메뉴에 따라 해당 기능 수행
    if menu == '1':
        print('성적 데이터 추가')
        cnt = len(names)
        names.append(input(f'{cnt}번학생 이름은? '))
        scoreKs.append(int(input(f'{cnt}번학생 국어는? ')))
        scoreEs.append(int(input(f'{cnt}학생 영어는? ')))
        scoreMaths.append(int(input(f'{cnt}학생 수학은? ')))
        tots.append(scoreKs[cnt] + scoreEs[cnt] + scoreMaths[cnt])
        avgs.append(tots[cnt] / 3)
        grd = '수' if (avgs[0] >= 90) else \
            '우' if (avgs[0] >= 80) else \
                '미' if (avgs[0] >= 70) else \
                    '양' if (avgs[0] >= 60) else '가'
        grds.append(grd)

    elif menu == '2':
        print('성적 데이터 조회')
        for j in range(len(names)):
            print(f'이름: {names[j]}, 국어: {scoreKs[j]}, 영어: {scoreEs[j]}, 수학: {scoreMaths[j]}')

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
