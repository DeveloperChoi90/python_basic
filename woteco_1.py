from collections import deque

def solution(arr):
    answer = deque([])
    arr_quantity = deque([])
    dict_num = {1:0, 2:0, 3:0}
    for num in arr:
        if num == 1:
            dict_num[1] += 1
        elif num == 2:
            dict_num[2] += 1
        else:
            dict_num[3] += 1
    print(dict_num)

    for val in dict_num.values():
        arr_quantity.appendleft(val)
    num_max = max(arr_quantity)
    print(num_max)

    for idx in range(len(arr_quantity)):
        if arr_quantity[idx] <= num_max:
             answer.appendleft(num_max - arr_quantity[idx])
    return list(answer)




arr = [2, 1, 3, 1, 2, 1]
print(solution(arr))