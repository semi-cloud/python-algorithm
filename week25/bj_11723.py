# 비트 마스킹 : 정수의 이진수 표현(0,1)을 자료 구조로 쓰는 기법
# 10 bit로 2^10가지의 정수를 표현 가능 하므로, 메모리 사용량을 줄이는데 효과적 + bit 연산은 O(1)이므로 성능이 빠르다
# 비트 연산자 활용 부분에는 반드시 괄호를 씌워주기(우선순위가 낮으므로)
# 비트마스크를 이용한 집합 구현 : 하나의 bit가 하나의 원소이며, bit가 1이라면 집합에 포함 0이라면 집합에 포함 X


# 일반 배열 혹은 리스트로 했다면, 최악의 경우 3,000,000 * O(M) 여서 시간 초과
# 함수를 만들어서 인자로 전달할 때도 매번 지역변수를 만들어야 하므로 메모리 초과
import sys

M = int(sys.stdin.readline())   # 수행 해야할 연산의 수
arr = 0

for _ in range(M):
    # 공집합 생성
    temp = sys.stdin.readline().split()
    if len(temp) > 1:
        op, k = temp[0], int(temp[1]) - 1   # 1을 안 빼주면 총 집합 개수는 21이 필요
        if op == "add":  # k번째 bit 켜기 : k 번째 bit만 1로 만든 후에 or 연산
            arr |= 1 << k  # 집합에 포함 되어 있지 않은 경우에만 추가 하는 로직은 필요 X
        elif op == "check":
            if arr & (1 << k):  # 켜져 있는 경우(1) 에만 참 반환
                print(1)
            else:
                print(0)
        elif op == "remove":  # k 번째 bit 끄기 : k번째 bit만 0으로 만든 후에 and 연산
            arr &= ~(1 << k)
        elif op == "toggle":  # K 번째 bit가 켜져있다면 끄고, 꺼져있다면 켜기
            arr ^= 1 << k
    else:
        op = temp[0]
        if op == "all":
            arr = (1 << 20) - 1  # {1, 2 ... 20} 집합 == 1...11(20)
        else:
            arr = 0




