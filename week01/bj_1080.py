def reverse(x, y):      # 배열 3X3 뒤집기
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            arr1[i][j] = 1 - arr1[i][j]

def check_equal(arr1, arr2):    # 전체 배열 검사
    for i in range(n):
        for j in range(m):
            if arr1[i][j] != arr2[i][j]:
                return False
    return True


n, m = map(int, input().split())   # 입력

arr1 = [list(map(int, input())) for _ in range(n)]
arr2 = [list(map(int, input())) for _ in range(n)]

count = 0
for i in range(0, n-2):
    for j in range(0, m-2):
        if arr1[i][j] != arr2[i][j]:
            reverse(i, j)
            count += 1

if check_equal(arr1, arr2):
    print(count)
else:
    print(-1)






