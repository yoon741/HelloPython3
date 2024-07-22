import yoon.sungjukv7bDAO as sjv7dao

def displayMenu():
    main_menu = '''
    ==============================
         성적 프로그램 v7b
    ==============================
        1. 성적 데이터 추가 
        2. 성적 데이터 조회 
        3. 성적 데이터 상세조회 
        4. 성적 데이터 수정
        5. 성적 데이터 삭제 
        0. 성적 데이터 종료
    ==============================
    '''
    print(main_menu, end='')
    menu = input('=> 메뉴를 선택하세요 : ')
    return menu

# 성적 데이터 관련 변수 선언
def readSungJuk():
    sj = []
    cnt = sjv7dao.getTotalSungJuk()
    sj.append(input(f'{cnt}번 학생 이름은? '))
    sj.append(int(input(f'{cnt}번 학생 국어는? ')))
    sj.append(int(input(f'{cnt}번 학생 영어는? ')))
    sj.append(int(input(f'{cnt}번 학생 수학은? ')))
    return sj

# 입력받은 성적 데이터를 처리하고 테이블에 저장
def addSungJuk(sj):
    computeSungJuk(sj)
    sjv7dao.newSungJuk(sj)

# 테이블에 저장된 성적 데이터들 중 기본 데이터만 모아서 출력
def showSungJuk():
    result = ''
    sjs = sjv7dao.readAllSungJuk()
    for sj in sjs:
        result += f'번호: {sj[0]}, 이름: {sj[1]}, 국어: {sj[2]}, 영어: {sj[3]}, 수학: {sj[4]}, 등록일 {sj[5]}\n'
    print(result)

# 학생 이름으로 성적데이터 조회 후 출력
def showOneSungJuk():
    # name = input('조회할 학생 이름은?')
    sjno = input('조회할 학생 번호은?')
    result = '데이터가 존재하지 않습니다!'
    sj = sjv7dao.readOneSungJuk(sjno)
    if sj:      # 조회한 데이터가 존재한다면
        result = (f'번호: {sj[0]}, 이름: {sj[1]}, 국어: {sj[2]}, 영어: {sj[3]}, 수학: {sj[4]} \n'
                  f'총점: {sj[5]}, 평균: {sj[6]:.1f}, 학점: {sj[7]}, 등록일: {sj[8]}')
    print(result)

# 입력한 성적데이터에 대해 성적처리하는 함수
def computeSungJuk(sj):
    sj.append(sj[1] + sj[2] + sj[3])
    sj.append(round(sj[4] / 3))

    grd = '수' if (sj[5] >= 90) else \
          '우' if (sj[5] >= 80) else \
          '미' if (sj[5] >= 70) else \
          '양' if (sj[5] >= 60) else '가'
    sj.append(grd)
    return sj
