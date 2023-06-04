'''
파일명: Ex06-4-while4.py

2x1=2 3x1=3 4x1=4
...
2x9=18 3x9=27 4x9=36
5x1=5 6x1=6 7x1=7
...
8x1=8 9x1=9
...

'''
dan = 2
while dan <= 9:
    n = 1
    while n <= 9:
        print('{}x{}={} '.format(dan, n, dan * n), end='')
        n += 1
    dan += 1
    print()

