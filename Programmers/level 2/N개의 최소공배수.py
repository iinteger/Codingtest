def solution(arr):
    maxvalue = max(arr)

    i = 0
    while True:
        i += 1
        LCM = maxvalue * i

        for j in arr:
            if LCM % j != 0:
                break

        else:
            return LCM
        
# 쉬운 문제
# 최소공배수는 가장 큰 값의 배수만 체크하면 됨
# for - else 문