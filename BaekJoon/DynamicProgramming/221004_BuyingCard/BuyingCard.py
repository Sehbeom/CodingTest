# 2022.10.04
# 백준 / 11052번 카드 구매하기

# 내가 푼 코드
N = int(input())
cards = list(map(int, input().split()))

answer = 0
maxResultList = [0] * N
maxResultList[0] = cards[0]

for i in range(1, len(cards)):
    start = -1
    end = i
    newOne = 0
    while start < end:
        start += 1
        end -= 1
        if start == end:
            if newOne < (maxResultList[start] * 2):
                newOne = maxResultList[start] * 2
        else:
            if newOne < (maxResultList[start] + maxResultList[end]):
                newOne = maxResultList[start] + maxResultList[end]

    if newOne < cards[i]:
        maxResultList[i] = cards[i]
        answer = cards[i]
    else:
        maxResultList[i] = newOne
        answer = newOne


print(answer)

# 다른 사람의 코드
# 방식은 동일하나 더 쉽게 풀 수 있음
n = int(input())
d = [0] * (n + 1)
p = [0] + list(map(int, input().split()))
d[1] = p[1]
for i in range(2, n + 1):
    print(d)
    for j in range(1, i + 1):
        if d[i] < d[i - j] + p[j]:
            d[i] = d[i - j] + p[j]
print(d[n])
