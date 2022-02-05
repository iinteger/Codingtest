def check(p):
    count_left, count_right = 0, 0

    for i in p:
        if i == '(':
            count_left += 1
        else:
            count_right += 1

        if count_right > count_left:
            return False

    return True


def split_uv(p):
    if p == "":  # 1
        return p

    count_left, count_right = 0, 0

    for i, e in enumerate(p):
        if e == "(":
            count_left += 1
        else:
            count_right += 1

        if count_left == count_right:  # 2
            u = p[:i + 1]
            v = p[i + 1:]

            if check(u):  # 3
                u += split_uv(v)  # 3-1
                return u
            else:  # 4
                empty_string = "(" + split_uv(v) + ")"  # 4-1 ~ 4-3

                u = u[1:-1]  # 4-4 ~ 4-5
                u_converted = ""
                for j in u:
                    if j == '(':
                        u_converted += ')'
                    else:
                        u_converted += '('

                empty_string += u_converted
                return empty_string


def solution(p):
    if check(p):
        return p

    return split_uv(p)

# 문자열 조작과 재귀 함수를 이용한 간단한 문제였음