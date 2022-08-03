# 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현할 수 있는지 방법
def solution(s):
    answer = len(s)

    for step in range(1, (len(s) // 2) + 1):
        result, count = [], 1
        temp = s[: step]                          # 앞에서부터 step만큼의 문자열 추출

        for j in range(step, len(s), step):       # step씩 증가시켜 가면서 같은지 검사
            if temp == s[j: j + step]:
                count += 1                        # 문자열이 반복된다면 증가
            else:                                 # 문자열이 반복되지 않는 경우
                result += str(count) + temp if count > 1 else temp
                temp, count = s[j: j + step], 1               # 패턴과 카운트 초기화

        result += str(count) + temp if count > 1 else temp
        answer = min(len(result), answer)                      # 가장 짧은 문자열 찾기
    return answer




