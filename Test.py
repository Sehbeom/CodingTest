from collections import deque

# queue1 = deque( < 리스트 > )
queue1 = deque([1, 2, 3])

print(queue1)
print(queue1.popleft())
print(queue1)
# 1
# [2, 3]

print(queue1.pop())
print(queue1)
# 3
# [2]
