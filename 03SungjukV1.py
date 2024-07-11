# 성적 처리 프로그램 v1
# 이름, 국어, 영어, 수학을 입력 받으면
# 총점, 평균, 학점을 계산하고 출력함
# 학점 : 수우미양가

# 이름 : 홍길동, 국어 : 99, 영어 : 98, 수학 : 99
# 총점 : 296, 평균: 99.9, 학점 : 수

# 성적 데이터 입력받은
name = input('이름은? ')
scoreK = int(input('국어는? '))
scoreE = int(input('영어는? '))
scoreMath = int(input('수학은? '))


# 성적 처리
totalScore = scoreK + scoreE + scoreMath
avgScore = totalScore / 3
grd = '수' if (avgScore >= 90) else \
      '우' if (avgScore >= 80) else \
      '미' if (avgScore >= 70) else \
      '양' if (avgScore >= 60) else '가'    # 삼항연산자


# 결과 출력
print(f'''
이름 : {name}, 국어 : {scoreK}, 영어 : {scoreE}, 수학 : {scoreMath} : 99
총점 : {totalScore}, 평균: {avgScore:.1f}, 학점 : {grd}
''')
