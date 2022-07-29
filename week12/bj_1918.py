prec = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}    # 연산자 우선순위 지정
infix = list(input())
st = []
result = []

for idx, num in enumerate(infix):
    if num == '(':                # 괄호 시작
        st.append(num)
    elif num == ')':              # 닫힌 괄호를 만날 경우
        while True:
            temp = st.pop()
            if temp == '(':       # 앞서서 넣은 '('를 만날 때 까지 팝
                break
            result.append(temp)
    elif num in prec:             # 연산자인 경우
        while st:
            if prec[st[-1]] >= prec[num]:    # 자신보다 같거나 높은 우선순위를 가진 연산자는 팝
                result.append(st.pop())
            else:
                break
        st.append(num)        # 연산자 스택에 추가
    else:
        result.append(num)     # 숫자인 경우는 바로 출력

# 남아 있는 연산자 모두 팝한 뒤 출력
while st:
    result.append(st.pop())

print("".join(result))


