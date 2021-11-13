import re

def solution(time, plans):
    answer = ''
    mon_arrival = 13
    fri_depart = 18
    remain_time = 0
    for plan in plans:
        depart_time = 0
        arrival_time = 0
        for w in plan[1]:
            if w == "P":
                depart_time = int(re.sub(r"[^0-9]", "", plan[1]))
                if depart_time < 13:
                    depart_time = depart_time + 12

                else:
                    depart_time_hour, min  = divmod(depart_time, 100)
                    if min:
                        depart_time = depart_time_hour + 12.5
                    else:
                        depart_time = depart_time_hour + 12
            elif w == "A":
                depart_time = int(re.sub(r"[^0-9]", "", plan[1]))
                if depart_time < 13:
                    depart_time = depart_time + 12
                else: 
                    depart_time_hour, min  = divmod(depart_time, 100)
                    if min:
                        depart_time = depart_time_hour + 0.5
                    else:
                        depart_time = depart_time_hour

        for w in plan[2]:
            if w == "P":
                arrival_time = int(re.sub(r"[^0-9]", "", plan[2]))
                if arrival_time < 13:
                    arrival_time = arrival_time + 12

                else: 
                    arrival_time_hour, min  = divmod(arrival_time, 100)
                    if min:
                        arrival_time = arrival_time_hour + 12.5
                    else:
                        arrival_time = arrival_time_hour + 12
            elif w == "A":
                arrival_time = int(re.sub(r"[^0-9]", "", plan[2]))
                if arrival_time < 13:
                    arrival_time = arrival_time
                else:
                    arrival_time_hour, min  = divmod(arrival_time, 100)
                    if min:
                        arrival_time = arrival_time_hour + 0.5
                    else:
                        arrival_time = arrival_time_hour

        print(depart_time, arrival_time) 
        remain_time_depart = (depart_time - fri_depart)
        remain_time_arrival = (mon_arrival - arrival_time)
        remain_time = remain_time_depart + remain_time_arrival
        if remain_time < 0:
            remain_time += time
        
        print(plan[0], remain_time_depart, remain_time_arrival)
        print(remain_time)
        if remain_time > 0:
            answer = plan[0] 
    return answer


time = 3.5
plans = [ ["홍콩", "11PM", "9AM"], ["엘에이", "3PM", "2PM"] ]
print(solution(time, plans))