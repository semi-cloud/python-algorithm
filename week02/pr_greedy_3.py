# number 에서 k 개의 수를 제거 했을 때 만들 수 있는 수 중 가장 큰 숫자
# 총 뺄 횟수에 도달 하면 나머지 남은거 넣기

arr = list(map(int, input()))
k = int(input())

result = []
for num in arr:
    # 스택의 탑보다 뒤에 숫자가 큰 경우 + 스택에 원소가 있는 경우 + 아직 뺄 횟수가 남아 있는 경우
    # 스택 탑 제거 후 푸시
    while result and k > 0 and result[-1] < num:
        result.pop()
        k -= 1
    result.append(num)     # 뒤에 숫자가 작은 경우 푸시

if k > 0:      # 모든 자리 수가 같은 경우(예외 사항)
    for i in range(k):
        result.pop()

print("".join(map(str, result)))

