#  "균형잡힌 괄호 문자열" 를 주어진 알고리즘을 수행해 "올바른 괄호 문자열"로 변환한 결과 출력
import sys
from collections import Counter
sys.setrecursionlimit(10 ** 7)


def is_alright_string(s):        # '('와 ')'의 괄호의 짝이 맞는 경우
    st = []
    for char in s:
        if char == "(":
            st.append(char)
        elif char == ")" and len(st) >= 1:  # 앞서서 넣은 ( 를 만날때 까지 pop
            while True:
                if st.pop() == "(":
                    break
    return True if not st else False      # 스택이 비어 있으면 올바른 괄호 문자열


def is_weighted_string(s):          # '(' 의 개수와 ')' 의 개수가 같은 경우
    value = list(Counter(s).values())
    return True if len(value) >= 2 and value[0] == value[1] else False


def reverse_str(strings):           # 괄호 뒤집기
    return [r[s] for s in strings]


r = {"(": ")", ")": "("}
def solution(p):
    result = ""
    if not p:             # 빈 문자열인 경우 그대로 반환
        return p
    u, v = "", ""
    for i in range(len(p)):
        if is_weighted_string(p[:i + 1]):  # 균형잡힌 문자열인 경우 u,v 분리
            u += p[:i + 1]
            v += p[i + 1:]
            break
    if is_alright_string(u):           # 문자열 u가 "올바른 괄호 문자열"인 경우
        return u + solution(v)         # 문자열 v에 대해 재귀 수행, 결과를 u에 이어 붙인 후 반환
    else:                              # 문자열 u가 "올바른 괄호 문자열"이 아닌 경우
        result += "("
        result += solution(v)
        result += ")"
        result += "".join(reverse_str(u[1:len(u) - 1]))    # 앞 뒤 문자 자르고 괄호 뒤집기
    return result

print(solution("()))((()"))
