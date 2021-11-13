from datetime import time
from collections import deque


s = "aaooaa"
dq_s = deque(s)
while True:
    dq_s.pop()

print(s[0])
print(dq_s[-1])