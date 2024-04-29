import sys
input = sys.stdin.readline

data = list(input().rstrip().split('-'))
# print(data)
result = 0
first = True
for i in data:
    sub_data = list(i.split('+'))
    if first:
        for j in sub_data:
            result += int(j)
        first = False
    else:
        for j in sub_data:
            result -= int(j)

print(result)