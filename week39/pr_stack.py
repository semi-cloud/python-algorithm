# 스택에 하나씩 넣어 가면서, 스택 탑(이전에 넣은 수)보다 넣으려는 수가 크면 가까우면서 큰 수를 찾을 수 있음

def solution(numbers):
    N = len(numbers)
    st = [0]
    res = [0 for _ in range(N)]

    for i in range(1, N):  # 1 - N-1
        while st and numbers[st[-1]] < numbers[i]:  # 현재 수보다 스택 탑이 더 작다면 계속 팝
            num_idx = st.pop()
            res[num_idx] = numbers[i]  # 자신 보다 큰 수 중 가장 가까운 수 기록
        st.append(i)

    while st:  # 뒤에 큰 수가 없는 경우
        idx = st.pop()
        res[idx] = -1

    return res

print(solution([9, 1, 5, 3, 6, 2]))
print(solution([2, 3, 3, 5]))

# 시간 초과 : O(N^2)
#     for i in range(N-1, -1, -1):  # 스택에 뒤에서부터 넣기
#         st.append(numbers[i])
#         origin.append(numbers[i])   # 원본

#     for i in range(N):
#         while st and st[-1] <= numbers[i]:    # 현재 수보다 큰 수가 나올때 까지 pop
#             st.pop()    # 작거나 같으면 pop

#         if not st:
#             res.append(-1)     # 만약 자신보다 큰 수가 없어서 스택이 빈 경우
#         else:
#             res.append(st[-1])   # 자신보다 큰 수 중 가장 가까운 수 기록
#         st = origin[:N-i-1]    # 지나간 수 이후부터 배열 원상 복구
