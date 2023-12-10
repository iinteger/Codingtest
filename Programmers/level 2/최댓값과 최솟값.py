# map 함수로 스플릿과 형변환을 한번에 적용
def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))

# 내 풀이
def solution(s):
    s_list = s.split(" ")
    s_list = [int(i) for i in s_list]
    
    return f"{min(s_list)} {max(s_list)}"