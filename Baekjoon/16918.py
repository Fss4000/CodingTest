'''
16918 봄버맨
가장 처음에 봄버맨은 일부 칸에 폭탄을 설치해 놓는다. 모든 폭탄이 설치된 시간은 같다.
다음 1초 동안 봄버맨은 아무것도 하지 않는다.
다음 1초 동안 폭탄이 설치되어 있지 않은 모든 칸에 폭탄을 설치한다. 즉, 모든 칸은 폭탄을 가지고 있게 된다. 폭탄은 모두 동시에 설치했다고 가정한다.
1초가 지난 후에 3초 전에 설치된 폭탄이 모두 폭발한다.
3과 4를 반복한다.
'''

#R x C 배열에 N초후 상황
    #1.폭탄 설치
    #2. 1초동안 아무것도 안함
    #3. 1초후 나머지 빈칸에 폭탄설치
    #4. 폭발 queue로 상하좌우 폭발
    
    
r, c, n = map(int, input().split())
arr = [list(input()) for _ in range(r)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
bombs = []
find_bomb = lambda li: [(i, j) for j in range(c) for i in range(r) if li[i][j] == 'O']  # 현재 폭탄 위치


def pung(): # 폭탄 펑!
    global arr, bombs
    for bx, by in bombs:
        arr[bx][by] = '.'
        for i in range(4):
            nx, ny = bx + d[i][0], by + d[i][1]
            if nx in range(r) and ny in range(c):
                arr[nx][ny] = '.'


def fill_bombs(): # 폭탄으로 채우기
    global arr
    arr = [['O'] * c for _ in range(r)]


def print_answer(li): # 결과 출력
    for line in li:
        print(''.join(line))


for second in range(1, n): # 1초 ~ N-1초 수행
    if second % 2 == 1:
        bombs = find_bomb(arr) # 폭탄 위치 찾고
        fill_bombs() # 폭탄 채우기
    else:
        pung() # 폭탄 펑!

print_answer(arr)