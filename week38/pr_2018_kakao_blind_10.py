# 사무실로 갈 수 있는 제일 늦은 도착 시간 출력
# 같은 시간에 도착했다면 가장 뒤에 서야함(중요)

from collections import deque
import datetime

def format_date_time2(num):  # 시간 이렇게도 포맷팅 가능
    hour = str(num // 60).zfill(2)  # hh, zfill : 빈 공간 앞에 0 채우기
    minute = str(num % 60).zfill(2)  # MM
    return hour + ':' + minute

def format_date_time(num):
    time = datetime.time(num // 60, num % 60)
    return time.strftime('%H:%M')

def solution(n, t, m, timetable):  #
    temp = []
    start = 9 * 60  # 셔틀 시작 시간

    for time in timetable:
        hour, minute = map(int, time.split(":"))
        crew_arrive = hour * 60 + minute
        temp.append(crew_arrive)

    temp.sort()  # 도착한 순대로 정렬
    q = deque(temp)

    last_arrive = 0
    for i in range(n):  # 총 운행 횟수
        cnt, limit = 0, 0

        while q:
            if q[0] <= start:  # 현재 출발 시각보다 먼저 도착한 크루들 태우기
                limit = q.popleft()  # 최대 탑승 가능한 늦은 시간 기록
                cnt += 1
            else:
                break  # 더 태울 수 없다면 중지

            if cnt >= m: break  # 만약 탑승 가능 크루보다 최대 탑승객 수가 작다면 탑승 중지

        if i == n - 1:          # 마지막 셔틀 버스라면 탈 수 있는 가장 마지막 시간 구해야함
            if limit == 0 or cnt == 0:       # 만약 아무도 못타는 상황인 경우(늦어서)
                return format_date_time(start)
            if cnt < m and limit < start:     # 자리가 남음 + 최대 한계 시점이 출발 시각 보다 빠른 경우
                return format_date_time(start)
            last_arrive = limit - 1          # 콘은 무조건 뒤로 보내지므로 최대 한계 시점보다 1초 앞서야함
        start += t

    return format_date_time(last_arrive)