import sys
input = sys.stdin.readline

n = int(input())
data = sorted(map(int, input().split()))

# print(data)
m = int(input())
find_list = list(map(int, input().split()))

def bi_search(number):
    start = 0
    end = n
    if number < data[0] or number > data[-1]:
        return 0
    while start <= end:
        mid = (start + end) // 2
        # print(mid, '!!!!!')
        if data[mid] == number:
            return 1
        elif data[mid] > number:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for i in find_list:
    print(bi_search(i))