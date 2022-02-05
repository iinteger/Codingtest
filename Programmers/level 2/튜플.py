def solution(s):
    s = eval(s.replace("{", "[").replace("}", "]"))

    s.sort(key=lambda x: len(x))

    answer = []
    for i in s:
        for element in i:
            if element not in answer:
                answer.append(element)

    return answer


#  대괄호를 중괄호로 바꾸고 eval을 사용해 리스트로 바꾸는 방법을 사용함
#  다른 풀이는 정규식이나 문자열 조작을 사용해서 푼 풀이가 많았음