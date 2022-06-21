# 두 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액을 찾기
def binary_search():
    global result
    start = 0
    end = n-1
    min_num = 2000000001

    while start < end:
        temp = arr[start] + arr[end]    # 두 수 더한 값

        if min_num > abs(temp):        # 더 작은 값이 나타 나면 결과값 갱신
            min_num = abs(temp)
            result = [arr[start], arr[end]]
            if min_num == 0:
                break

        if temp > 0:       # 0 보다 크므로 더 작은 수 더해서 0에 가까워지기
            end -= 1
        else:              # 0 보다 작으므로 더 큰 수 더해서 0에 가까워지기
            start += 1

n = int(input())
arr = sorted(list(map(int, input().split(' '))))
result = []
binary_search()
print(result[0], result[1])




