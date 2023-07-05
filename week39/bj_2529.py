# 같은 부등호를 만족시키는 숫자 중에 최대 / 최소값 찾기

def is_possible(i, j, idx):  # 맞는 부등호 인지 확인
    if arr[idx] == "<":
        return i < j     # j가 새로 비교할 값
    else:
        return i > j

def bt(idx, num, result):  # 백트래킹
    global min_res, max_res

    if idx == k+1:   # 부등호 배열 인덱스
        if min_res == "":
            min_res = result  # 가장 처음에 나오는 값이 최소
        else:
            max_res = result  # 가장 마지막에 나오는 값이 최대
        return

    for new in range(0, 10):     # 매 깊이 마다 0-9 숫자 탐색해서 맞는거 고르기
        if idx == 0 or is_possible(num, new, idx-1):   # 부등호가 성립 한다면 재귀적으로 탐색 진행(맨 처음 문자는 패스)
            if not visited[new]:  # 이미 방문한 숫자라면 더 깊게 탐색 X
                visited[new] = True
                bt(idx + 1, new, result + str(new))
                visited[new] = False

k = int(input())
arr = list(input().split(" "))  # > < > >
visited = [False for _ in range(10)]  # 0-9
min_res, max_res = "", ""
bt(0, 0, "")
print(max_res)
print(min_res)

# 방법 2: https://myeongju00.tistory.com/34
