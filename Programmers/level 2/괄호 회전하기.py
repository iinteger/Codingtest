def check(s):
    big_left = 0
    big_right = 0
    medium_left = 0
    medium_right = 0
    small_left = 0
    small_right = 0

    left_list = []
    # ({)} <- 이 경우를 걸러야 함

    for i in s:
        if i == "{":
            big_left += 1
            left_list.append("{")
        elif i == "[":
            medium_left += 1
            left_list.append("[")
        elif i == "(":
            small_left += 1
            left_list.append("(")

        elif i == "}":
            big_right += 1
            if len(left_list) == 0 or left_list[-1] != "{":
                return False
            del left_list[-1]

        elif i == "]":
            medium_right += 1
            if len(left_list) == 0 or left_list[-1] != "[":
                return False
            del left_list[-1]

        elif i == ")":
            small_right += 1
            if len(left_list) == 0 or left_list[-1] != "(":
                return False
            del left_list[-1]

        if big_right > big_left or medium_right > medium_left or small_right > small_left:
            return False

    if big_right != big_left or medium_right != medium_left or small_right != small_left:
        return False

    return True


def solution(s):
    answer = 0

    for i in range(len(s)):
        turned_s = s[i:] + s[:i]
        if check(turned_s):
            answer += 1

    return answer