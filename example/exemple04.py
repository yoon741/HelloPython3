# 51 구구단
print('''
          Multiplication Table                          
      1   2   3   4   5   6   7   8   9
---------------------------------------
''')
for i in range(1, 9+1):
    print(f'{i} |',end='')
    for j in range(1, 9+1):
        print(f'{i * j:4d}', end='')
    print()


# 33
cardno = input('카드번호는? ')

result = '잘못된 카드 번호입니다'
if cardno[:2] == '35':
    if cardno == '356317': result = 'JCB카드 NH농협카드'
    elif cardno == '356901': result = 'JCB카드 신한카드'
    elif cardno == '356912': result = 'JCB카드 KB국민카드'
elif cardno[:1] == '4':
    if cardno == '404825': result = '비자카드 비씨카드'
    elif cardno == '438676': result = '비자카드 신한카드'
    elif cardno == '404825': result = '비자카드 KB국민카드'
elif cardno[:1] == '5':
    if cardno == '515594': result = '마스터카드 신한카드'
    elif cardno == '524353': result = '마스터카드 외환카드'
    elif cardno == '540926': result = '마스터카드 KB국민카드'

print(f'{cardno} / {result}')


# 16 개선하기 - 리스트/반복문/함수

# price = int(input('계산할 돈을 입력하세요.'))
# paid = int(input('받은 돈을 입력하세요.'))
#
# charge = paid - price
#
# units = [50000,10000,5000,1000,500,100,50,10]
# charges = []
#
# for unit in units:
#     charges.append(charge // unit)
#     charge %= unit
#
# result = f'''
# 금액 : {price:,} 원
# 지불금액 : {paid:,} 원
# 잔돈 : {(paid - price):,} 원
# ------------------------
# '''
#
# for idx, u in enumerate(units):
#     result += f'{u}원 : {charges[idx]} 장/개\n'
#
# print(result)

def comute_charge(price,  paid):
    units = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    charges = []

    charge = paid - price
    for unit in units:
        charges.append(charge // unit)
        charge %= unit

    result = f'''
금액 : {price:,} 원
지불금액 : {paid:,} 원 
잔돈 : {(paid - price):,} 원
------------------------'''
    for idx, u in enumerate(units):
        result += f'{u}원 : {charges[idx]} 장/개\n'

    print(result)

comute_charge()

# 잔돈 구하는 함수 호출 및 테스트
price = int(input('지불해야 할 금액은?'))
paid = int(input('받은 금액은?'))
comute_charge(price, paid)

