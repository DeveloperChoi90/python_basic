# pickle이라는 파일 형태로 저장
# pickle을 사용하기 위해선 항상 binary형태로 읽기, 쓰기가 이루어 져야한다.

import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"name":"choi", "age":32, "hobby":["jujitsu", "coding", "sleeping"]}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()

# "rb" : read binary
# 
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

# with 사용시 따로 파일을 close할 필요가 없음
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# 파일을 바로 만들고 closde할 필요가 없음
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())