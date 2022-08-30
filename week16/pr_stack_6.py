# 초 단위로 기록된 주식 격이 담긴 배열이 주어졌을 때, 가격이 떨어지지 않은 기간은 몇 초인지 반환
def solution(prices):
    result = [len(prices) - i - 1 for i in range(len(prices))]    # 몇초 후 가격이 떨어지는지 저장하는 배열
    st = [0]

    for i, p in enumerate(prices):
        for j in st[::-1]:
            if prices[j] > p:               # 스택의 탑보다 추가 하려는 수가 작다면(감소 하면)
                result[j] = i - j           # 추가 하려는 수의 인덱스 - 더 큰 수의 인덱스
                st.pop()                    # 결과가 정해진 값은 제거
            else:
                break
        st.append(i)      # 인덱스 저장
    return result

print(solution([1, 2, 3, 2, 3]))






