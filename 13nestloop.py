# 중첩 반복문
# 2개 이상의 반복문을 이용해서 반복실행할 수도 있음
# 하나의 반복문안에 다른 반복문을 포함시킨 것을 의미
# 이것을 통해 좀 더 복잡한 반복패턴을 구현 할 수 있음
# 2차원 배열처리나 달력 출력, 복잡한 패턴 생성시 주로 이용

# *
# **
# ***
# ****
# *****

# 5 x 5 반복 출력
for i in range(5):    # 행
    for j in range(5):   # 열
        print('*', end='')
    print()           # 줄바꿈

# 각 반복마다 1, 2, 3, 4, 5 번 출력
for i in range(1, 5+1):    # 행
    for j in range(i):   # 열
        print('*', end='')
    print()           # 줄바꿈


# *****
# ****
# ***
# **
# *

for i in range(5, 0, -1):    # 행
    for j in range(i):   # 열
        print('*', end='')
    print()           # 줄바꿈



#구구단 출력
for i in range(1, 9+1):                        # 행/큰바늘
    for j in range(1, 9+1):                    # 열/작은바늘
        print(f'{j:1d} x {i:1d} = {j * i:2d}   ', end='')
    print()