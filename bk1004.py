"어린 왕자"
"""
빨간 실선은 어린 왕자가 출발점에서 도착점까지 도달하는데 있어서 필요한 행성계 진입/이탈 횟수를 최소화하는 경로이며, 원은 행성계의 경계를 의미한다.
이러한 경로는 여러 개 존재할 수 있지만 적어도 3번의 행성계 진입/이탈이 필요하다는 것을 알 수 있다.
위와 같은 은하수 지도, 출발점, 도착점이 주어졌을 때 어린 왕자에게 필요한 최소의 행성계 진입/이탈 횟수를 구하는 프로그램을 작성해 보자. 
행성계의 경계가 맞닿거나 서로 교차하는 경우는 없다. 또한, 출발점이나 도착점이 행성계 경계에 걸쳐진 경우 역시 입력으로 주어지지 않는다.
"""
"""
입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 
그 다음 줄부터 각각의 테스트케이스에 대해 첫째 줄에 출발점 (x1, y1)과 도착점 (x2, y2)이 주어진다. 
두 번째 줄에는 행성계의 개수 n이 주어지며, 세 번째 줄부터 n줄에 걸쳐 행성계의 중점과 반지름 (cx, cy, r)이 주어진다.
"""
"""
풀이
- 출발점과 도착점이 원의 중심과 일치할 경우 count
- 출발점이 원에 속하고 도착점은 원에 속하지 않을때
- 출발점은 원에 속하지 않고 도착점이 원에 속할때
- 출발점과 도착점이 모두 원에 속하지 않을때
"""
import math

T = int(input())
for _ in range(T):
    cnt = 0
    x1, y1, x2, y2 = map(int, input().split())
    start = (x1, y1)
    end = (x2, y2)
    plante_num = int(input())
    for _ in range(plante_num):
        c_x, c_y, r = map(int, input().split())
        circle_center = (c_x, c_y)
        dist1 = math.dist(start, circle_center) - r
        dist2 = math.dist(end, circle_center) - r
        if dist1 * dist2 < 0:
            cnt += 1
    print(cnt)
    
