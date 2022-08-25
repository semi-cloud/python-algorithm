# 연산자 우선순위를 조작하여 받을 수 있는 가장 큰 우승상금 금액 찾기

from itertools import permutations


def solution(expression):
    operators = ["*", "+", "-"]
    answer = []
    for op in permutations(operators):
        op1 = op[0]
        op2 = op[1]
        tmp_list = []

        for partition in expression.split(op1):   # 첫 번째 연산자 기 준 분리 배열
            tmp = [f'({j})' for j in partition.split(op2)]  # 두 번째 연산자 기준 분리 후 각각에 대해 괄호 생성
            tmp_list.append(f'({op2.join(tmp)})')   # 두 번째 연산자로 붙이기

        answer.append(abs(eval((op1.join(tmp_list)))))         # 첫 번째 연산자로 다시 붙인 후 우승상금 계산
    return max(answer)        # 우승 상금중 가장 최대값 리턴


print(solution("100-200*300-500+20"))