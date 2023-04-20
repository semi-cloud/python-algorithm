def check_right(arr):
    st = []
    for a in arr:
        if not st:  # 스택이 비어있는 경우는 시작 끝 상관 없이 무조건 넣기
            st.append(a)
            continue

        if a in end.keys():  # 끝점을 만난 경우 스택 탑하고 비교해서 맞다면 pop
            if st[-1] in start.keys() and start[st[-1]] == end[a]:  # 같은 유형의 괄호면 빼내기
                st.pop()
        else:
            st.append(a)  # 시작 괄호를 만나는 경우 넣기

    if st: return False  # 스택에 남은 데이터가 있는 경우 올바르지 않은 괄호
    return True

start = {'[': 0, '(': 1, '{': 2}
end = {']': 0, ')': 1, '}': 2}

def solution(s):
    N = len(s)
    arr = list(s)
    ans = 0

    flag = False
    for k in range(N):  # 왼쪽으로 x칸 만큼 회전 시키면서 검사
        res = [0 for _ in range(N)]
        for i in range(N):
            res[(i - k + N) % N] = arr[i]
        if check_right(res):
            ans += 1
            flag = True
    return ans if flag else 0

