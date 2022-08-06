import math


def solution(progresses, speeds):
    st, result, idx = [], [], 0
    for p, s in zip(progresses, speeds):
        left_day = math.ceil((100 - p) / s)    # 남은 일수 구하기
        st.append(left_day)

    for i in range(len(st)):
        if st[idx] < st[i]:            # 현재 위치의 작업일 보다 큰 수를 만나면
            result.append(i - idx)     # 현재 위치부터 큰 원소까지의 모든 원소 개수 추가
            idx = i                    # 현재 위치를 큰 수의 위치로 갱신

    result.append(len(st[idx:]))         # 끝 부분 남은거 처리
    return result


print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
