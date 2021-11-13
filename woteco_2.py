def solution(log):
    answer = ''
    start_time = []
    end_time = []
    study_time = 0
    real_study_time = 0
    for idx, time in enumerate(log):
        hour, min = map(int, time.split(":"))
        time = hour*60 + min
        if idx % 2 == 0:
            start_time.append(time)
        else:
            end_time.append(time)
    # print(start_time)
    # print(end_time)
    for idx in range(len(start_time)):
        study_time = end_time[idx] - start_time[idx]
        # print(study_time)
        if study_time >= 5:
            if study_time < 105:
                real_study_time += study_time
            else:
                real_study_time += 105
        # print(real_study_time)

    # print(real_study_time)
    hour = real_study_time // 60
    min = real_study_time - hour * 60
    if hour < 10:
        hour = "0" + str(hour)
    answer = str(hour) + ":" + str(min)

    return answer




log = ["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]
print(solution(log))