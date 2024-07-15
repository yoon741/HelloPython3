# 성적 처리 프로그램 v2
# 이름, 국어, 영어, 수학을 입력 받으면
# 총점, 평균, 학점을 계산하고 출력함
# 단, 학생 3명에 대해서 성적처리를 진행함

# 이름 : 민지, 국어 : 99, 영어 : 98, 수학 : 99
# 이름 : 혜린, 국어 : 88, 영어 : 77, 수학 : 66
# 이름 : 다니엘, 국어 : 55, 영어 : 77, 수학 : 99

# 성적 데이터 입력받은
name1 = input('1번학생 이름은? ')
scoreK1 = int(input('1번학생 국어는? '))
scoreE1 = int(input('1번학생 영어는? '))
scoreMath1 = int(input('1번학생 수학은? '))

name2 = input('2번학생 이름은? ')
scoreK2 = int(input('2번학생 국어는? '))
scoreE2 = int(input('2번학생 영어는? '))
scoreMath2 = int(input('2번학생 수학은? '))

name3 = input('3번학생 이름은? ')
scoreK3 = int(input('3번학생 국어는? '))
scoreE3 = int(input('3번학생 영어는? '))
scoreMath3 = int(input('3번학생 수학은? '))

# 성적 처리
tot1 = scoreK1 + scoreE1 + scoreMath1
avgScore = tot1 / 3
grd = '수' if (avgScore >= 90) else \
    '우' if (avgScore >= 80) else \
    '미' if (avgScore >= 70) else \
    '양' if (avgScore >= 60) else '가'

tot2 = scoreK2 + scoreE2 + scoreMath2
avgScore = tot2 / 3
grd = '수' if (avgScore >= 90) else \
    '우' if (avgScore >= 80) else \
    '미' if (avgScore >= 70) else \
    '양' if (avgScore >= 60) else '가'

tot3 = scoreK3 + scoreE3 + scoreMath3
avgScore = tot3 / 3
grd = '수' if (avgScore >= 90) else \
    '우' if (avgScore >= 80) else \
    '미' if (avgScore >= 70) else \
    '양' if (avgScore >= 60) else '가'

# 결과 출력
print(f'''
이름 : {name1}, 국어 : {scoreK1}, 영어 : {scoreE1}, 수학 : {scoreMath1} : 99
총점 : {tot1}, 평균: {avgScore:.1f}, 학점 : {grd}
''')
print(f'''
이름 : {name2}, 국어 : {scoreK2}, 영어 : {scoreE2}, 수학 : {scoreMath2} : 99
총점 : {tot2}, 평균: {avgScore:.1f}, 학점 : {grd}
''')
print(f'''
이름 : {name3}, 국어 : {scoreK3}, 영어 : {scoreE3}, 수학 : {scoreMath3} : 99
총점 : {tot3}, 평균: {avgScore:.1f}, 학점 : {grd}
''')
