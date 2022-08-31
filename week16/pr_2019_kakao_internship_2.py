# 특정 튜플을 표현하는 집합이 담긴 문자열 s => s가 표현하는 튜플을 배열에 담아 출력
def solution(s):
    num, result = [], []
    temp = s[2:-2].split('},{')
    arr = sorted(temp, key=lambda x: len(x))   # 집한 개수가 적은 순대로 정렬

    for num_lis in arr:                # 기존 집합에 없던 숫자가 다음 집합에서 나타난다면 결과 튜플에 추가
        num = map(int, num_lis.split(','))
        for n in num:
            if n not in result:
                result.append(n)
    return result

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
