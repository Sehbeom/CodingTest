# 2022.09.26
# 백준 / 1339번 단어 수학

N = int(input())
wordDic = {}
charDic = {}

for i in range(N):
    temp = list(input())
    wordDic[len(temp)] = temp

wordDic = dict(sorted(wordDic.items(), reverse=True))
