# 현재 시점에 들어온 요청 중에 가장 짧은 작업 시간이 걸리는 것을 택

from heapq import heappush, heappop

def solution(jobs):
    q, ans = [], 0
    jobs.sort(key=lambda x: x[0])      # 기본은 요청 순서에 따른 처리
    # cur = jobs[0][0] + jobs[0][1]    # 첫 요청이 끝난 시점 저장

    cur, i, start = 0, 0, -1
    while i < len(jobs):     # 모든 작업이 끝날때 까지 반복
        for job in jobs:     # 현재 시점에서 처리 가능한 작업들 힙에 추가
            if start < job[0] <= cur:  # 요청이 들어오는 범위 체크
                heappush(q, (job[1], job[0]))

        # 더 짧은 시간을 가진 요청이 들어올 수 있기 때문에 큐에 있는 것들을 한꺼번에 처리하면 안됌
        if len(q) >= 1:   # 1개 이상 있다면 그 중 가장 짧은 작업 시간이 걸리는 요청 처리
            time, req = heappop(q)
            start = cur     # 이전의 작업이 끝난 시점을 저장
            cur += time     # 현재 시점을 작업 완료 시점으로 갱신
            ans += cur - req  # 요청 - 종료까지 걸린 시간들 저장(이전 마친 시간 + 걸리는 작업 시간 - 요청 시점)
            i += 1          # 처리한 작업 개수 증가
        else:     # 처리할 요청이 없는 경우 시간만 증가시키기
            cur += 1

    return ans // len(jobs)  # 평균 시간 구해서 리턴

    # while q:
    #     time, start = heappop(q)
    #     cur += time                # 현재 시점의 위치 갱신
    #     ans.append(cur - start)    # 요청 - 종료까지 걸린 시간들 저장
    #
    #     for job in jobs:
    #         if job[0] <= cur:      # 현재 작업이 끝난 시점 보다 더 빨리 요청이 들어와서 대기 중인 요청들 힙에 푸시
    #             heappush(q, (job[1], job[0]))  # 작업 시간이 적은 순으로 정렬
    #             jobs.remove(job)  # 작업된 요청은 배열에서 제거 => 반복 중에는 배열 건드리지 말아야함
    #     print("q", q)

print(solution([[0, 3], [1, 9], [2, 6]]))

