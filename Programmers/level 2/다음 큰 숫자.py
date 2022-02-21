def solution(n):
    i = n+1

    while True:
        if bin(n).count("1") == bin(i).count("1"):
            return i
        i += 1