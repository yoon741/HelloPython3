import yoon.empDAO as empdao

def displayMenu():
    main_menu = '''
    ==============================
         - 사원 관리 프로그램 -
    ==============================
        1. 사원 데이터 추가 
        2. 사원 데이터 조회 
        3. 사원 데이터 상세조회
        4. 사원 데이터 수정
        5. 사원 데이터 삭제
        0. 사원 데이터 종료
    ==============================
    '''
    print(main_menu, end='')
    menu = input('=> 메뉴를 선택하세요 : ')
    return menu

# 사용자로부터 값 입력 함수
def readEmp():
    emp = []
    cnt = empdao.getTotalEmp()
    emp.append(input(f'{cnt}번 사원 번호는? '))
    emp.append(input(f'{cnt}번 사원 이름은? '))
    emp.append(input(f'{cnt}번 사원 성은? '))
    emp.append(input(f'{cnt}번 사원 이메일은? '))
    emp.append(input(f'{cnt}번 사원 전화번호는? '))
    emp.append(input(f'{cnt}번 사원 입사일은? '))
    emp.append(input(f'{cnt}번 사원 직책은? '))
    emp.append(input(f'{cnt}번 사원 급여는? '))
    emp.append(input(f'{cnt}번 사원 수당은? (없으면 0)'))
    emp.append(input(f'{cnt}번 매니저 번호는? (없으면 0)'))
    emp.append(input(f'{cnt}번 사원 부서번호는? (없으면 0)'))
    return emp

# 입력받은 사원 데이터를 처리하고 테이블에 저장
# 입력받은 수당, 매니저번호, 부서번호는 적절한 형변환 필요!
def addEmp():
    emp = readEmp()
    # emp[8] = float(emp[8]) if emp[8] != '0' else 'null'
    emp[8] = float(emp[8]) if emp[8] != '0' else None
    emp[9] = int(emp[9]) if emp[9] != '0' else 'null'
    emp[10] = int(emp[10]) if emp[10] != '0' else 'null'
    empdao.newEmp(emp)

# 테이블에 저장된 사원 데이터들 중 기본 데이터만 모아서 출력
def showEmp():
    result = ''
    emps = empdao.readAllEmp()
    for emp in emps:
        result += f'사원번호: {emp[0]}, 이름: {emp[1]}, 이메일: {emp[2]}, 직책: {emp[3]}, 부서번호: {emp[4]}\n'
    print(result)

# 사원번호로 사원데이터 조회후 출력
def showOneEmp():
    empid = input('조회할 사원 번호은?')
    result = '데이터가 존재하지 않습니다!'
    emp = empdao.readOneEmp(empid)
    if emp:      # 조회한 데이터가 존재한다면
        result = (f'사원번호: {emp[0]}, 이름: {emp[1]}, 성: {emp[2]}, 이메일: {emp[3]}, 전화번호: {emp[4]} \n'
                  f'입사일: {emp[5]}, 직책: {emp[6]}, 월급: {emp[7]}, 커미션: {emp[8]}, 상사: {emp[9]}, 부서번호: {emp[10]}')
    print(result)
