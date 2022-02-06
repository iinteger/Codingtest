def solution(s):
    stack = []

    for i in s:
        if len(stack) == 0:
            stack.append(i)

        elif stack[-1] == i:
            del stack[-1]
        else:
            stack.append(i)

    if len(stack) == 0:
        return 1
    else:
        return 0

# 시간초과
#     a_ord = ord('a')
#     z_ord = ord('z')

#     while s != "":

#         for i in range(a_ord, z_ord+1):
#             string = chr(i) + chr(i)
#             string_index = s.find(string)
#             if string_index != -1:
#                 s = s[:string_index] + s[string_index+2:]
#                 break

#         else:
#             return 0

#     return 1


# 시간초과
#     i = 0
#     length = len(s)
#     while i < length-1:
#         i += 1

#         for j in range(len(s)-2):
#             if s[j] == s[j+1]:
#                 if j == len(s)-2:
#                     s = s[:j]
#                 else:
#                     s = s[:j] + s[j+2:]
#                 break

#     if len(s) == 2 and s[0] == s[1]:
#         return 1
#     else:
#         return 0

# 전체 문자열을 버블소트처럼 비교하며 일일히 제거 -> 시간초과
# find를 사용해서 문자열을 탐색하여도 정답률은 올랐지만 여전히 시간초과
# 스택을 사용해서 스택 -1의 문자열과 직접 비교하는 방법 -> 성공
# 일단 넣고 스택 내에서 [-1] [-2]를 비교하였더니 시간초과됨