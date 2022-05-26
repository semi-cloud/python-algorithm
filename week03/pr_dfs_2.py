n = int(input())
computers = [list(map(int, input())) for _ in range(n)]
visited = [False] * n

def dfs(num):
    st = [num]    # 스택에 푸시, 연결된 노드들 푸시
    while st:
        a = st.pop()
        for j in range(len(computers)):
            if not visited[j] and computers[a][j] == 1:    # 연결 되어 있으면 스택에 푸시
                visited[j] = True
                st.append(j)     # j와 연결 되어 있음

count = 0
for i in range(n):
    if not visited[i]:
        dfs(i)        # 한 노드씩 방문 하고, 연결이 끝나면 돌아 와서 카운트 증가
        count += 1
print(count)
