import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K and len(scoville) > 1:  # 가장 작은 스코빌이 K이상이면 루프x
        mixed = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        answer += 1

        heapq.heappush(scoville, mixed)

    if scoville[0] < K:
        return -1

    return answer

# 리스트를 사용했을 땐 대부분 시간복잡도로 인해 불가능했는데 heapq 자료구조를 사용했더니 한번에 성공함