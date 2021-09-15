# 터렛
# 두 원사이의 관계
"""
-10,000 =< x1,x2,y1,y2 =< 10,000
0 =< r1, r2 =< 10,000
"""

import math

n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt(math.pow((x1 - x2),2) + math.pow((y1 - y2), 2))
    if distance == 0 and r1 == r2:
        print(-1)
    elif distance == abs(r1 - r2)  or distance == r1 + r2:
        print(1)
    elif abs(r1 - r2) < distance < r1 + r2:
        print(2)
    else:
        print(0)