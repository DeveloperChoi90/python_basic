'''
n개의 음이 아닌 정수가 있습니다.
이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 
예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.
사용할 수 있는 숫자가 담긴 배열 numbers, 
타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
각 숫자는 1 이상 50 이하인 자연수입니다.
타겟 넘버는 1 이상 1000 이하인 자연수입니다.
'''

from itertools import product

def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    # print(list(product(*l)))
    return s.count(target)

from collections import deque

def BFS(numbers, target):
    answer = 0
    stack = deque([(0, 0)])
    while stack:
        current_sum, num_idx = stack.popleft()
        if num_idx == len(numbers):
            if current_sum == target:
                answer += 1
        
        else:
            number = numbers[num_idx]
            stack.append((current_sum + number, num_idx + 1))
            stack.append((current_sum - number, num_idx + 1))

    return answer

answer = 0
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx == N and target == value):
        answer += 1
        return 

    if(idx == N):
        return
    
    DFS(idx + 1, numbers, target, value + numbers[idx])
    DFS(idx + 1, numbers, target, value - numbers[idx])

def solution2(numbers, target):
    global answer
    DFS(0, numbers, target, 0)
    return answer



import time

numbers = [1, 1, 1, 1, 1]
target = 3
start = time.time()
print(solution(numbers, target))
end = time.time()
print(f"{end - start:.5f} sec")

start = time.time()
print(BFS(numbers, target))
end = time.time()
print(f"{end - start:.5f} sec")

start = time.time()
print(solution2(numbers, target))
end = time.time()
print(f"{end - start:.5f} sec")
