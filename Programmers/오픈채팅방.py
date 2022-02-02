def solution(record):
    id_nickname = {}

    for i, string in enumerate(record):
        splitted = string.split(" ")

        action = splitted[0]
        id = splitted[1]

        if action == "Enter" or action == "Change":
            nickname = splitted[2]
            id_nickname[id] = nickname

    answer = []
    for string in record:
        action = string.split(" ")[0]
        id = string.split(" ")[1]

        if action == "Enter":
            log = f"{id_nickname[id]}님이 들어왔습니다."
            answer.append(log)
        elif action == "Leave":
            log = f"{id_nickname[id]}님이 나갔습니다."
            answer.append(log)

    return answer


#  최종적으로 Enter or Change 할 때 사용한 닉네임이 전체 로그에 적용되므로 하나로 묶었고, 아이디 : 닉네임은 딕셔너리로 저장
#  변수 할당에 문자열 포매팅이 가능했음