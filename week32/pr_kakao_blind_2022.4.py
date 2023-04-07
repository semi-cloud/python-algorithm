path, res = [], []

def bt(idx, lion, apeach, cnt, N, arr):  # 과녁 인덱스, 각 점수, 화살을 쏜 개수
    if idx > 10:  # 모든 과녁을 다 검사한 경우 점수 차이 계산
        if N > 0:  # 끝 까지 갔는데 N이 남아있는 경우 남은 화살을 무조건 다 쏘아야함
            path[-1] = N

        diff = lion - apeach
        if diff > 0:  # 라이언이 이기는 경우만 저장, 점수가 같아도 어피치 승)
            res.append([diff, path[:]])
        return

    # 라이언은 화살을 무조건 N개 모두 쏴야함
    if N > 0:  # 쏠 화살이 남아 있는 경우 쏠 수도 있고 안 쏠 수도 있음
        if arr[idx] + 1 <= N:
            path.append(arr[idx] + 1)  # 1. 라이언이 이기는 경우(화살을 쏘는 경우)
            bt(idx + 1, lion + (10 - idx), apeach, arr[idx] + 1, N - (arr[idx] + 1), arr)
            path.pop()
        path.append(0)  # 2. 어피치가 이기는 경우(비기거나 점수가 작은 경우 화살을 아예 쏘지 X)(근데 이때 어피치 점수가 0 이 아니여야해)
        bt(idx + 1, lion, apeach + (10 - idx) if arr[idx] > 0 else apeach, cnt, N, arr)
        path.pop()

    elif N == 0 and arr[idx] == 0:  # 3. 화살도 다 썼고 어피치 점수도 0인 경우 둘 다 점수를 얻지 못함
        path.append(0)
        bt(idx + 1, lion, apeach, cnt, N, arr)
        path.pop()
    else:
        path.append(0)  # 4. 위에서의 모든 경우가 아니라면 어피치가 이김
        bt(idx + 1, lion, apeach + (10 - idx), cnt, N, arr)
        path.pop()


def solution(n, info):
    bt(0, 0, 0, 0, n, info)
    temp, ans = [], []
    if res:
        res.sort(key=lambda x: x[0], reverse=True)
        max = res[0][0]

        for score, arr in res:
            if score == max: temp.append(arr)

        if len(temp) > 0:
            test = []
            for i, arr in enumerate(temp):
                for j in range(9, -1, -1):
                    if arr[j] > 0:
                        test.append((j, arr[j], arr))
                        break
            test.sort(key=lambda x: [x[0], -x[1]], reverse=True)  # 1. 낮은 점수를 맞춘 순으로 2. 같다면 더 많이 맞춘 순으로
            ans = test[0][2]
        else:
            ans = temp
        return ans
    else:
        return [-1]
