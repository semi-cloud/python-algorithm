#  N개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램
from collections import defaultdict

N = int(input())
d = defaultdict(int)

for i in range(N):
    word = list(input().rstrip())           # 문자열 입력
    for idx, c in enumerate(word):
        d[c] = d.get(c, 0) + 10 ** (len(word)-1-idx)    # 알파벳 마다 자릿수 저장

arr = sorted(d.items(), key=lambda x: x[1], reverse=True)   # 자릿수 큰 순서대로 정렬

result, cnt = 0, 9
for num in arr:
    result += num[1] * cnt           # 9부터 차례대로 곱하기
    cnt -= 1
print(result)
