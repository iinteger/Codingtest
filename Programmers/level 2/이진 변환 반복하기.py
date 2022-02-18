def binarize(s):
    zero_count = s.count("0")
    s = s.replace("0", "")
    length = len(s)
    s = bin(length)[2:]
    return s, zero_count


def solution(s):
    zero_sum = 0
    binarize_count = 0
    while s != "1":
        s, zero_count = binarize(s)
        zero_sum += zero_count
        binarize_count += 1

    return [binarize_count, zero_sum]

# 쉬운 문제