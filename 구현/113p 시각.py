n = int(input())

count = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            # if "3" in str(s) + str(m) + str(h):  책 풀이
            if "3" in str(s) or "3" in str(m) or "3" in str(h):
                count += 1

print(count)
