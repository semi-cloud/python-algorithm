# 같은 색으로 칠해져 있지 않다면 N/2 × N/2 개로 나눠서 잘라진 하얀색 색종이와 파란색 색종이의 개수를 구하기(분할 정복)

def is_full(x, y, n):
    color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != color:
                return False
    return True

def divide(x, y, k):
    global white, blue
    if is_full(x, y, k):   # 색종이를 분할이 끝났다면 개수 갱신하고 재귀 종료
        if paper[x][y] == 0:
            white += 1
        else:
            blue += 1
        return

    k //= 2
    divide(x, y, k)     # 분할되는 네 개의 색종이의 시작점
    divide(x, y+k, k)
    divide(x+k, y, k)
    divide(x+k, y+k, k)

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
white, blue = 0, 0
divide(0, 0, N)  # 시작 위치
print(white)
print(blue)



