# 성적 처리 프로그램 v2b
# 이름, 국어, 영어, 수학을 입력 받으면
# 총점, 평균, 학점을 계산하고 출력함
# 단, 리스트를 이용해서 학생 3명에 대해서 성적처리를 진행함

# 이름 : 민지, 국어 : 99, 영어 : 98, 수학 : 99
# 이름 : 혜린, 국어 : 88, 영어 : 77, 수학 : 66
# 이름 : 다니엘, 국어 : 55, 영어 : 77, 수학 : 99

# 성적 데이터 관련 변수 선언
names = []
scoreKs = []
scoreEs = []
scoreMaths = []
tots = []
avgs = []
grds = []

# 성적 데이터 입력받은
names.append(input('1번학생 이름은? '))
scoreKs.append(int(input('1번학생 국어는? ')))
scoreEs.append(int(input('1번학생 영어는? ')))
scoreMaths.append(int(input('1번학생 수학은? ')))

names.append(input('2번학생 이름은? '))
scoreKs.append(int(input('2번학생 국어는? ')))
scoreEs.append(int(input('2번학생 영어는? ')))
scoreMaths.append(int(input('2번학생 수학은? ')))

names.append(input('3번학생 이름은? '))
scoreKs.append(int(input('3번학생 국어는? ')))
scoreEs.append(int(input('3번학생 영어는? ')))
scoreMaths.append(int(input('3번학생 수학은? ')))


# 성적 처리

tot = scoreKs[0] + scoreEs[0] + scoreMaths[0]
avg = tots[0] / 3
grd = '수' if (avgs[0] >= 90) else \
      '우' if (avgs[0] >= 80) else \
      '미' if (avgs[0] >= 70) else \
      '양' if (avgs[0] >= 60) else '가'

tots.append(tot)
avgs.append(avg)
grds.append(grd)

tot = scoreKs[1] + scoreEs[1] + scoreMaths[1]
avg = tots[1] / 3
grd = '수' if (avgs[1] >= 90) else \
      '우' if (avgs[1] >= 80) else \
      '미' if (avgs[1] >= 70) else \
      '양' if (avgs[1] >= 60) else '가'

tots.append(tot)
avgs.append(avg)
grds.append(grd)

tot = scoreKs[2] + scoreEs[2] + scoreMaths[2]
avg = tots[2] / 3
grd = '수' if (avgs[2] >= 90) else \
    '우' if (avgs[2] >= 80) else \
        '미' if (avgs[2] >= 70) else \
            '양' if (avgs[2] >= 60) else '가'

tots.append(tot)
avgs.append(avg)
grds.append(grd)

# 결과 출력
print(f'''
이름: {names[1]}, 국어: {scoreKs[1]}, 영어: {scoreEs[1]}, 수학: {scoreMaths[1]}
# 총점: {tots[1]}, 평균: {avgs[1]:.1f}, 학점: {grds[1]}
이름: {names[2]}, 국어: {scoreKs[2]}, 영어: {scoreEs[2]}, 수학: {scoreMaths[2]}
# 총점: {tots[2]}, 평균: {avgs[2]:.1f}, 학점: {grds[2]}
이름: {names[3]}, 국어: {scoreKs[3]}, 영어: {scoreEs[3]}, 수학: {scoreMaths[3]}
# 총점: {tots[3]}, 평균: {avgs[3]:.1f}, 학점: {grds[3]}
''')

이그잼 03
실습문제 풀이 추가

성적첯리 06
성적처리 프로그램 v2 - 학생 3명 성적 처리

07리스트
파이썬 자료 구조 리스트

08성적
성적처리 프로그램 v2b - 리스트 자료 구조로 학생 3명 성적 처리