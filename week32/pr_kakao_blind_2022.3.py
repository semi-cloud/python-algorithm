import math
from collections import defaultdict

def calculate(fees, time):
    if time > fees[0]:  # 기본 시간을 초과했을 경우
        return fees[1] + (math.ceil((time - fees[0]) / fees[2]) * fees[3])
    else:
        return fees[1]

def solution(fees, records):  # 시각 차량번호 내역
    info = defaultdict(list)  # 각 차량의 누적 시간 계산
    res, ans = [], []  # 차량 번호가 작은 자동차부터 청구할 주차 요금 구하기

    for record in records:
        record = list(record.split(" "))
        time, car, status = list(map(int, record[0].split(":"))), record[1], record[2]
        time = (time[0] * 60) + time[1]
        info[car].append(time)

    for k, times in list(info.items()):
        total = 0
        for i in range(0, len(times) - 1, 2):  # 입차와 출차 두개 씩 묶어서 계산
            total += times[i + 1] - times[i]

        if len(times) % 2 != 0:  # 홀수인 경우 남은 하나를 23:59랑 계산
            total += (23 * 60 + 59) - times[-1]
        res.append((k, calculate(fees, total)))

    res.sort(key=lambda x: x[0])
    for r in res: ans.append(r[1])
    return ans