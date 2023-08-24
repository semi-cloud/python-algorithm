# 한 자리에서 스위치를 누르는 경우 / 누르지 않는 경우 => 2^N(시간 초과)
# 최소한의 방법 보장 => 다른 부분이 있는 경우에만 변호나 작업 수행
# 첫 번째 자리 스위치 결정 여부 -> 두 번째 자리 결정 여부에 영향 -> 세 번째 자리 결정 여부에 영향
# 그리디하게 i-1번째 전구만 보면서 눌러야 할 지 안 눌러야 할 지를 결정(매번 모든 경우의 수를 따지지 X)
# 즉, N 번째 자리의 상태를 바꿔야 한다면 N을 누르지 않고 무조건 N+1을 눌러서 N-1에 영향이 가지 않도록 해야함
# 0번째 자리는 앞에 상태가 없으므로 누르는 경우와 누르지 않는 경우를 모두 체크 필요
# (0)00 -> 11(0) -> 1(0)1 -> 010

def change(n):
    if n == 0: return 1
    else: return 0

def switch_bulb(i, arr):
    cnt = 0
    if arr[i-1] != expect[i-1]:     # 원본과 기대하는 값이 다른 경우에만 스위치 누르기 결정
        arr[i-1], arr[i] = change(arr[i-1]), change(arr[i])  # 가장 자리
        if i != N-1:
            arr[i+1] = change(arr[i+1])  # 중간 자리인 경우
        cnt += 1
    return cnt

N = int(input())  # 100,000
now = list(map(int, list(input())))
expect = list(map(int, list(input())))
res = 0

push, no_push = [n for n in now], [n for n in now]
push_cnt, no_push_cnt = 1, 0
push[0], push[1] = change(now[0]), change(now[1])   # 첫 번째는 무조건 누르고 시작

for i in range(1, N):  # 한 칸 뛰고 시작
    no_push_cnt += switch_bulb(i, no_push)       # 2-1. 첫 번째 자리에서 스위치를 누르지 않는 경우
    push_cnt += switch_bulb(i, push)             # 2-2. 첫 번째 자리에서 스위치를 누르는 경우

# 기대하던 값처럼 전구가 켜졌다면 답
if no_push == expect:
    print(no_push_cnt)
elif push == expect:
    print(push_cnt)
else:
    print(-1)