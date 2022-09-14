
def BinarySearch(listInput, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if listInput[mid] >= target:
            end = mid - 1

        elif listInput[mid] < target:
            start = mid + 1

        if start == end:
            mid = start if listInput[start] >= target else start+1
            break

    return mid


a = [2, 2, 2, 2, 2, 2,
     5, 5, 5, 5, 5]

print(a)
print(BinarySearch(a, 1, 0, len(a)-1))
