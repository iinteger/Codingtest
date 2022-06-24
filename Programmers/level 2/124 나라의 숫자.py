def solution(n):
    converted = ""

    while n > 0:
        n, mod = divmod(n, 3)

        if mod == 1:
            converted = "1" + converted
        elif mod == 2:
            converted = "2" + converted
        else:
            converted = "4" + converted

            if n == 1 and mod == 0:
                break

            n -= 1

    return converted

