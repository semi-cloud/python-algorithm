# 각 숫자는 양수/음수의 상태 두 가지를 가질 수 있음(그래프 형식 으로 표현)

arr = list(map(int, input().split()))
target = int(input())
count = 0

def dfs(level, sum):
    global count

    if level == len(arr):     # 끝 노드에 도착 하면 총합이 일치 하는지 검사
        if sum == target:     # 일치 하면 카운트 증가
            count += 1
        return

    dfs(level + 1, arr[level] + sum)     # 합을 인자로 전달(양수)
    dfs(level + 1, -arr[level] + sum)    # 합을 인자로 전달(음수)

dfs(0, 0)
print(count)
