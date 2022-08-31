# 2022.08.31
# 백준 / 15649번 N과 M(1)

def findSequence(stack):
    exitFlag = True
    while exitFlag:
        ptr = 1
        while len(stack) < M:
            if not ptr in stack:
                stack.append(ptr)
            ptr += 1

        print(*stack)
        flag = True
        while flag:
            topNum = stack.pop() + 1
            while topNum in stack:
                topNum += 1

            if topNum <= N:
                stack.append(topNum)
                flag = False

            if not stack:
                exitFlag = False
                flag = False


N, M = map(int, input().split())

findSequence([1])
