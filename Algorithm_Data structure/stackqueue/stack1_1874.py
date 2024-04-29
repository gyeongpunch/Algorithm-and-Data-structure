import sys
input = sys.stdin.readline
n = int(input())
value = 1
data1 = []
data2 = []
for i in range(n):
    data = int(input())
    while value <= data:
        data1.append(value)
        value += 1
        data2.append('+')
    if data1[-1] == data:
        data1.pop()
        data2.append('-')
    else:
        value = False
        break
if value:
    print("\n".join(x for x in data2))
else:
    print('NO')