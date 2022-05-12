import sys
input = sys.stdin.readline

n = int(input())
cran_weight = sorted(list(map(int, input().split())), reverse=True)

m = int(input())
box_weight = sorted(list(map(int, input().split())), reverse=True)

count = 0

if cran_weight[0] < box_weight[0]:    # 박스를 옮기지 못할 때
    print(-1)
else:
    while len(box_weight) > 0:
        count += 1
        for i in range(len(cran_weight)):    # 크레인 개수
            for j in range(len(box_weight)):  # 박스 개수
                if cran_weight[i] >= box_weight[j]:    # 들고 갈 수 있으면 제거
                    box_weight.pop(j)
                    break
    print(count)
