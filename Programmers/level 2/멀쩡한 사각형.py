def solution(w, h):
    gcd = 0

    if w > h:
        w, h = h, w

    for i in range(w, 0, -1):
        if w % i == 0 and h % i == 0:
            gcd = i
            break

    per_w = w / gcd
    per_h = h / gcd

    if per_w == 1:
        per_crossed_square = per_h
    else:
        per_crossed_square = per_h + per_w - 1

    return w * h - per_crossed_square * gcd