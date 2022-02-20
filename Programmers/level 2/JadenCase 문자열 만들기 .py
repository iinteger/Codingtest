def solution(s):
    answer = ""

    for word in s.split(" "):
        if word == "":
            answer += " "

        else:
            word = word.lower()
            up = word[0].upper()
            answer += up + word[1:] + " "

    return answer[:-1]

# 쉬운 문제
# 문자열 마지막이 공백으로 끝나는 경우를 처리해야 함