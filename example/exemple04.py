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


