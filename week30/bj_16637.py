# 1. 괄호 안에는 연산자 하나 2. 중첩 괄호 사용 불가능 3. 괄호 추가 개수 제한 X(0~)
# 괄호를 적절히 추가해 만들 수 있는 식의 결과의 최댓값 구하기
# 즉 괄호 최대 개수인 9개 중 9C1 + 9C2 + ...9C5 의 모든 결과중 최대값 구하기
# 1. 괄호로 묶지 않고 바로 다음 숫자와 연산
# 2. 괄호로 묶고 다음 숫자와 다다음 숫자를 연산한 결과와의 연산

# 2. DFS + 재귀
def cal(n1, n2, op):
    return eval(str(n1) + op + str(n2))

# 재귀가 2가지 경우로 분리되므로 모든 경우의 수 안에 C1, C2, C3... CN의 경우 확인 가능
def dfs(idx, sum):  # idx : 현재 연산자의 위치
    global ans
    if idx >= len(op):  # 연산자 탐색을 모두 완료 했다면 최대값 갱신
        ans = max(ans, sum)
        return

    # 1. 괄호가 없을 떄의 일반적인 진행 과정
    dfs(idx + 1, cal(sum, num[idx + 1], op[idx]))

    # 2. 괄호가 있을 때의 과정 : 괄호를 추가한 값을 계산
    if idx + 1 < len(op):   # 괄호를 뒤에 칠 수 있는 상황인 경우
        res = cal(num[idx + 1], num[idx + 2], op[idx + 1])   # 뒤에 있는 괄호 친 연산 먼저 수행 후 현재 앞의 값이랑 연산 다시 수행
        dfs(idx + 2, cal(sum, res, op[idx]))

N = int(input())  # 19
formula = input()
op, num = [], []
ans = -int(1e9)  # 0으로 하면 값이 음수가 나올 경우 최대 값을 찾지 못함

for idx, f in enumerate(formula):
    if f in ['+', '-', '*']:
        op.append(f)  # 연산자 모음 저장
    else:
        num.append(int(f))

dfs(0, num[0])
print(ans)

#
# def dfs(index, value):
#     global result
#
#     if index == n - 1:
#         result = max(result, value);
#         return
#
#     if index + 2 < n:
#         dfs(index + 2, myOperator(value, s[index + 1], int(s[index + 2])))
#
#     if index + 4 < n:
#         dfs(index + 4, myOperator(value, s[index + 1], myOperator(int(s[index + 2]), s[index + 3], int(s[index + 4]))))


# 1. DFS + 완전 탐색 + 큐(괄호를 직접 추가)
# from collections import deque
#
# def operate():
#     q, i = deque(), 0
#     # 1. 스택 처럼 괄호 안의 값을 우선으로 처리해서 값을 넣어줌
#     while i < len(formula):
#         if i % 2 != 0 and check[i % len(op)]:  # 수식 자리이고 괄호가 켜져 있다면 계산 후 다시 푸시
#             q.append(cal(q.pop(), formula[i], formula[i+1]))
#             i += 2
#         else:
#             q.append(formula[i])      # 숫자이거나 괄호가 없는 수식이라면 그냥 푸시
#             i += 1
#
#     # 2. 다음 큐 처럼 앞에서부터 순서대로 처리
#     while len(q) > 1:
#         q.appendleft(cal(q.popleft(), q.popleft(), q.popleft()))
#     return q.pop()   # 마지막으로 계산된 최종 결과값 반환
#
# def dfs(depth, visit):
#     global ans
#     if depth <= len(op):  # 괄호 켜진 인덱스 먼저 계산 0 2
#         ans = max(ans, operate())
#
#     for i in range(depth, len(op)):  # 1. DFS 로 연산자의 조합 구현
#         if not visit[i]:     # 중복 제거 위해 이미 방문 처리 완료된 연산자는 다시 방문하지 X
#             visit[i] = True
#             check[i] = True  # 해당 연산자에 우선순위 괄호 체크
#             dfs(depth + 2, visit[:])  # 인접한 다음 연산자는 괄호 불가능
#             check[i] = False
#             # dfs(depth + 1, cal(ans, num[i + 1], op[i]))  # 괄호 안의 값을 계산해서 재귀로 넘기기
#
# check = [False for _ in range(len(op))]  # 괄호가 켜져 있는 연산자
# visit = [False for _ in range(len(op))]

# 2. 다이나믹 프로그래밍
# 3. 조합을 이용하는 방식 : 연속해서 연산자를 택할 수 없는 조건을 처리하기 까다로워짐


