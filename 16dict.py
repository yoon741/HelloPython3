# 딕셔너리
# 이름key과 값velues으로 구성된 연관배열의 일종
# 자료구조를 만들때는 {}를 사용하고
# 이름과 값은 :으로 구분해서 정의함
# 다른 언어의 JSON과 유사한 구조
# 키를 통해 자료를 찾는 해시테이블을 이요하므로 검색속도가 빠름

# 중간고사 성적을 dict로 선언
sj = {'C/C++':'A', 'Java':'B+', '네트워크':'C',
      '보안':'A+', '해킹':'F', '클라우드':'C+'}
print(sj)

# 회원정보를  dict로 선언
# key : 이름,아이디,비번,이메일,주소,취미
member = { 'name':'홍길동', 'userid':'abc123',
           'passwd':'987xyz', 'email':'abc123@987xyz.co.kr',
           'addr':'서울 관악구 봉천동',
           'hobby':['운동','게임','여행']}
print(member)

# 딕셔너리 다루기
# 조회 : 변수명[키], 변수명.get(키)
print(member['userid'], member['passwd'])
print(member.get('email'), member.get('addr'))

# 존재하지 않는 키 지정시
print(member['zipcode'])          # 오류
print(member.get('zipcode'))      # none

# 새로운 항목 추가 : 변수명['새로운키'] = 값
member['zipcode'] = '12345'

# 기존 항목 수정 : 변수명 ['키'] = 수정할값
member['zipcode'] = '98765'
member['addr'] = '서울 광진구 자양동'

# 기존 항목 삭제 : 변수명.pop(키)
member.pop('zipcode')
member.pop('addr')

# dict의 모든 키 조회 : 변수명.keys()
# dict의 모든 값 조회 : 변수명.values()
print(member.keys())
print(member.values())

# dict 전체항목 조회
for k in member.keys():
    print(f'{member[k]}', end=' ')

# 열거형enumerate으로 dict 조회 : 인덱스, 키
for idx, k in enumerate(member):
    print(idx, k)

# key와 value를 한번에 출력 : 변수명.items
for k, v in member.items():
    print(k, v)


# 예제 

# 중간고사 성적 관리 p.33
# 시나리오 #1
mids = {'C/C++':'A', 'Java':'B+', '모바일':'C',
      '보안':'A+', '해킹':'F', '시스템':'C+'}
print(mids)

# 시나리오 #2
print(f"Java : {mids['Java']}")
print(f"시스템 : {mids['시스템']}")

# 시나리오 #3
mids['파이썬'] = 'A'
mids['OS'] = 'A+'
print(mids)

# 시나리오 #4
mids['Java'] = 'F'
mids['시스템'] = 'A'
print(mids)

# 시나리오 #5
for k, v in mids.items():
    print(f'{k} : {v}')

for k, v in mids.items():  # \t tap역할 정렬할수 있음
     print(k, '\t :  ', v)


# 수학시험 프로그램 p.37
quizs = []
answers = []
scores = []

quizs = ['3+2', '5/2의 몫', '10-2', '10의2제곱x2',
         '1-(10나누기4의 나머지)', '2의4제곱', '4/2']
answers = [5,2,8,200,-1,16,2]
scores = [3,5,3,5,5,3,3]
myAnswers = []

trueCount = 0
falseCount = 0
totalScore = 0

# 문제풀고 내 정답 입력
for i in range(len(quizs)):
    print(f'문제 : {quizs[i]} ?')
    myAnswers.append(int(input('정답을 입력하세요 : ')))

# 문제 풀이 및 채점
for i in range(len(answers)):
    if answers[i] == myAnswers[i]:
        trueCount+= 1
        totalScore += scores[i]
    else:
        falseCount += 1

# 결과 출력
print(f'''
{'-'*20}
정답 개수: {trueCount}
오답 개수: {falseCount}
Total Score: {totalScore}
{'-'*20}
''')


# 수학 시험 프로그램 2
quizs = ( ('3+2',5, 3), ('5/2의 몫',2,5),
          ('10-2',8,3), ('10의2제곱x2',200,5),
          ('1-(10나누기4의 나머지)',-1,5),
          ('2의4제곱',16,3), ('4/2',2,3) )     # 튜플 : 수정이 불가능하다
myAnswers = []

trueCount = 0
falseCount = 0
totalScore = 0

# 문제풀고 내 정답 입력
for q in quizs:
    print(f'문제 : {q[0]} ?')
    myAnswers.append(int(input('정답을 입력하세요 : ')))

# 문제 풀이 및 채점
# enumerate : 반복가능한 객체를 순회하면서,
# 각 요소의 위치값(인덱스)와 값을 함께 반환하는 함수
for idx, q in enumerate(quizs):
    if q[1] == myAnswers[idx]:
        trueCount+= 1
        totalScore += q[2]
    else:
        falseCount += 1

# 결과 출력
print(f'''
{'-'*20}
정답 개수: {trueCount}
오답 개수: {falseCount}
Total Score: {totalScore}
{'-'*20}
''')

# 로또 당첨 게임 
from random import sample
# 숫자입력받기
lotto = []
matchs = []

# 숫자입력받기
print('1부터 45까지의 정수 6개를 입력하세요. ')
for i in range(6):
    lotto.append(int(input(f'Number {i+1} : ')))

# 로또 매직 넘버 생성
magic = sample(range(1, 45+1), 6)

# 당첨 여부 확인
# for i in range(6):
#     if lotto[i] in magic:
#         matchs += 1

for l in lotto:
    if l in magic:
        matchs.append(l)

# 결과출력
print(f'''
이번주 로또 번호 {magic}
내가 선택한 번호 {lotto}
일치하는 숫자 : {matchs}
''')

