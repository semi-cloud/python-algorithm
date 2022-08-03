# 최종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태로 출력
from collections import defaultdict

def solution(record):
    result = []            # [(uid, 상태 정보)]
    d = defaultdict(str)      # key: 아이디, value : 닉네임

    for idx, data in enumerate(record):
        datas = data.split(" ")
        if "Enter" == datas[0]:         # 채팅에 입장할 경우
            d[datas[1]] = datas[2]      # 사용자 정보 저장
            result.append((datas[1], "님이 들어왔습니다."))
        elif "Leave" == datas[0]:       # 채팅에 나가는 경우
            result.append((datas[1], "님이 나갔습니다."))
        else:
            d[datas[1]] = datas[2]      # 닉네임 변경한 경우

    return list(map(lambda x: d[x[0]] + x[1], result))   # 변하지 않는 아이디 값을 기준으로 최종 닉네임 값으로 변환

test = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(test))