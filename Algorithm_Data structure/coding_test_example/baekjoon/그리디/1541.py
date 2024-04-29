# import sys
# input = sys.stdin.readline

data = list(input().split('-'))
# print(data)
result = 0
cnt = 0
for i in data:
    a = i.split('+')
    # print(a)
    if cnt == 0:
        for j in a:
            result += int(j)
            cnt += 1
    else:
        for j in a:
            result -= int(j)
print(result)