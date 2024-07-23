from yoon.oop.models import SungJuk
from yoon.oop.dao import SungJukDAO as sjdao

# 성적 서비스 클래스
class SungJukService:
    # 데코레이터 : 함수에 추가기능을 구현할 때 사용
    @staticmethod # 정적static 메서드 : 객체화 없이 바로 사용가능한 메서드
                  #     정적 메서드로 정의된 함수는 self 매개변수 지정 X
                  # 호출방법 : 클래스명.함수명
    def display_manu():
        main_menu = '''
        ==============================
             성적 프로그램 v8
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

    @staticmethod
    def read_sungjuk():
        name = input(f'새로운 학생 이름은? ')
        kor = int(input(f'새로운 학생 국어는? '))
        eng = int(input(f'새로운 학생 영어는? '))
        mat = int(input(f'새로운 학생 수학은? '))
        return SungJuk(name, kor, eng, mat)

    @staticmethod
    def add_sungjuk():
        sj = SungJukService.read_sungjuk()
        SungJukService.compute_sungjuk(sj)
        cnt = sjdao.insert_sungjuk(sj)
        result = f'{cnt} 건의 데이터 추가 성공!!'
        print(result)

    @staticmethod
    def compute_sungjuk(sj):
        sj.tot = sj.kor + sj.eng + sj.mat
        sj.avg = sj.tot / 3
        sj.grd = '가'
        if (sj.avg >= 90): sj.grd = '수'
        elif (sj.avg >= 80): sj.grd = '우'
        elif (sj.avg >= 70): sj.grd = '미'
        elif (sj.avg >= 60): sj.grd = '양'

    @staticmethod
    def show_sungjuk():
        result = ''
        sjs = sjdao.select_sungjuk()
        for sj in sjs:
            result += f'번호: {sj.sjno}, 이름: {sj.name}, 국어: {sj.kor}, '\
                      f'영어: {sj.eng}, 수학: {sj.mat}, 등록일: {sj.regdate}\n'
        print(result)

    @staticmethod
    def showone_sungjuk():
        pass

    @staticmethod
    def modify_sungjuk():
        pass

    def readagain_sungjuk(self):
        pass

    @staticmethod
    def remove_sungjuk():
        pass
