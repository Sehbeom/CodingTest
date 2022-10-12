# 2022.10.12
# 백준 / 2579번 계단 오르기

n = int(input())
stairs = []
for i in range(n):
    stairs.append(int(input()))

ansList = [[0] * 3 for i in range(n)]
ansList[0][0] = stairs[0]
ansList[0][1] = stairs[0]
ansList[0][2] = stairs[0]

if n > 1:
    ansList[1][0] = stairs[0] + stairs[1]
    ansList[1][1] = stairs[0] + stairs[1]
    ansList[1][2] = stairs[1]

    for i in range(2, n):
        curValue = stairs[i]
        ansList[i][1] = curValue + ansList[i-1][2]
        ansList[i][2] = curValue + max([ansList[i-2][1], ansList[i-2][2]])
        ansList[i][0] = max([ansList[i][1], ansList[i][2]])

print(ansList[n-1][0])
