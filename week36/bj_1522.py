# a를 연속으로 만들기 위해 필요한 교환의 최소 횟수
# 총 a의 개수 = 윈도우 사이즈 크기
# 해당 윈도우 내부에 b + a 값이 총 a의 개수가 되었을 때 b 개수의 최소값 찾기(b 개수 = 교환 횟수)
# 원형 반례 : aaaabbbbba => 교환할 필요 X
# 원형 이면 i값이 N-1까지 갈 때까지 가능(j 값은 회전)

string = input()

totalA, curA, curB, res = 0, 0, 0, float("inf")
for s in string:
    if s == 'a':
        totalA += 1

i, j = 0, 0
while i < len(string):
    while curA + curB < totalA:    # 총 A 개수가 될 때 까지 j 증가
        if string[j] == 'a': curA += 1
        else: curB += 1
        j = (j + 1) % len(string)

    res = min(res, curB)  # 교환의 최소값 저장
    if string[i] == 'a': curA -= 1
    else: curB -= 1
    i += 1

print(res)


