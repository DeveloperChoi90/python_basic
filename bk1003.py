"""
<입력>
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.
"""

"""
각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.
"""


zero = [1, 0, 1]
one = [0, 1, 1]

def fibonacci(num):
    if num >= len(zero):
        for idx in range(len(zero), num+1):
            zero.append(zero[idx-2]+zero[idx-1])
            one.append(one[idx-2]+one[idx-1])
    print("{0} {1}".format(zero[num], one[num]))

try:        
    n = int(input())
    if n < 0 or n > 40:
        print("N이 0보다 작거나 40보다 큰 수 입니다.")
        raise StopIteration

    for i in range(n):
        num = int(input())
        fibonacci(num)
        # print("{0} {1}".format(count[0], count[1]))

except StopIteration:
    print("중단")