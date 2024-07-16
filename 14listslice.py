# 슬라이싱(slicing)
# 연속적인 객체들 (리스트, 튜플, 문자열)에 범위를 지정하고
# 선택해서 부분적으로 객체를 가져오는 방법 및 표기법
# 리스트 객체에서 필요한 부분의 항목만 뽑아 사용하는 것
# 시퀀스 자료형에 지원되는 기능(순서를 기억함) 중에 하나
# 객체명[시작 : 끝-1 : 스텝]

# 리스트 슬라이싱 예제
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# 역순 출력
print(alphabet[::-1])

# 요구사항에 맞게 슬라이싱
print(f'''
{alphabet[2:6]},
{alphabet[0:5]},
{alphabet[3:8]},
{alphabet[5:]},
{alphabet[3:9]},
{alphabet[::2]},
{alphabet[:]}
''')


# 주민번호에서 생년월일과 성별코드 추출
# 문자열 슬라이스 : 문자열의 일부 추출 가능
jumin = '123456-1234567'

birth = jumin[0:6]
gender = jumin[7:8]

print(birth, '/' , gender)


#