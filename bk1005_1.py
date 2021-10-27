# 우선순위 큐
import sys
import heapq
from collections import defaultdict

def solve(precede_list, build_next, time, target):
    # 조건 없이 바로 만들 수 있는 건물들 찾기
    queue = [(time[idx], idx) for idx in range(1, len(precede_list)) if precede_list[idx] == 0]
    # 시간순서로 정렬, 가장 시간 짧은 것부터 뽑아내는 min heap 사용
    heapq.heapify(queue)

    while queue:
        # 현재 시간에 건설 끝난 건물.
        finished_time, building = heapq.heappop(queue)
        # 완성한 건물이 target 건물이면 그동안 building한 시간 반환
        if building == target:
            return finished_time
        
        # 지을 수 있는 다음 건물들 정보를 확인
        for next_possible in build_next[building]:
            # 조건에 해당하는 건물 제거
            precede_list[next_possible] -= 1

            # 지금까지 걸린 시간 + 건물 완성할 때까지 걸리는 시간, 건물을 heappush
            if precede_list[next_possible] == 0:
                heapq.heappush(queue, (finished_time + time[next_possible], next_possible))


test_case = int(sys.stdin.readline())
for _ in range(test_case):
    N, K = map(int, sys.stdin.readline().split())
    # 해당 index 건물을 짓기 위한 prerequsite 개수
    precede_list = [0 for _ in range(N+1)]

    # 해당 건물을 지으면 해금할 수 있는 건물 dictionary
    build_next = defaultdict(list)
    # 해당 index 건물을 짓는 데 걸리는 시간
    time = list(map(int, sys.stdin.readline().split()))
    time.insert(0, 0)

    for _ in range(K):
        precede, antecede = map(int, sys.stdin.readline().split())
        precede_list[antecede] += 1
        build_next[precede].append(antecede)
    
    target = int(sys.stdin.readline())
    print(solve(precede_list, build_next, time, target))