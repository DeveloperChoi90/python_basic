"""
처음과 끝이 이어져 있는 문자열을 상상해봅시다. 당신은 해당 문자열 내의 "같은 글자가 연속해 있는" 구간들을 추출하고자 합니다.
문자열 s가 매개변수로 주어집니다. 
s 내의 모든 "같은 글자가 연속해 있는" 구간의 길이를 각각 배열에 담아 오름차순으로 정렬하여 return 하도록 solution 함수를 완성해주세요.

입출력 예
s	result
"aaabbaaa"	[2,6]
"wowwow"	[1,1,2,2]
"""

# dq_s 가 비어있어 인덱싱이 잘못되는 경우가 생김 -> 어떻게 처리를 해야할까?
# 하나씩 세어 나가고, 처음이랑 마지막만 비교하여 count하면 된다.
from collections import deque

def solution(s):
    answer = []
    idx = 0
    length = len(s)
    count = 1
    
    for idx in range(length):
        if (idx + 1) < length:
            if s[idx] == s[idx + 1]:
                count += 1
            else:
                answer.append(count)
                count = 1
        else:
            if s[0] == s[idx]:
                answer[0] = answer[0] + count
            else:
                answer.append(count)
    
    answer = sorted(answer)
    return answer


s = ["aaabbaaa", "wowwow"]
print(solution(s[1]))