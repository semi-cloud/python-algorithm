# 베스트 앨범에 들어갈 노래의 고유 번호를 출력
from collections import defaultdict

def solution(genres, plays):
    result = []
    data = defaultdict(list)               # dict value 가 list 형태
    for idx, [g, p] in enumerate(zip(genres, plays)):
        data[g].append((idx, p))           # (인덱스, 재생 횟수)

    temp_list = sorted(data.items(), key=lambda x: sum(dict(x[1]).values()), reverse=True)   # 속한 노래가 많이 재생된 장르 순으로 정렬
    for temp in temp_list:
        for idx, _ in sorted(temp[1], key=lambda x: (x[1], -x[0]), reverse=True)[:2]:      # 장르 내에서 많이 재생된 노래 순으로 정렬
            result.append(idx)
    print(result)

data1 = ["classic", "pop", "classic", "classic", "pop"]
data2 = [500, 600, 150, 800, 2500]
solution(data1, data2)


