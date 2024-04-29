import sys
input = sys.stdin.readline
from queue import PriorityQueue

N = int(input())
data_m = PriorityQueue()
data_p = PriorityQueue()
cnt_1 = 0
cnt_0 = 0

for i in range(N):
    tmp = int(input())
    if tmp > 1:
        data_p.put(tmp * (-1))
    elif tmp < 0:
        data_m.put(tmp)
    elif tmp == 0:
        cnt_0 += 1
    elif tmp == 1:
        cnt_1 += 1
    
# print('!!!!')

# while data_m:
#     print(data_m.get())
# while data_p:
#     print(data_p.get())
# print(cnt_1)
# print(cnt_0)

result = 0

while data_m.qsize() > 1:
    a = data_m.get()
    b = data_m.get()
    result += a * b
# print(result, '!!!!')
if data_m.qsize() == 1:
    if cnt_0 == 0:
        result += data_m.get()

# print(result, '!!!!')
while data_p.qsize() > 1:
    a = data_p.get()
    b = data_p.get()
    # print(a, b, '@@@@@@@')
    result += a * b
# print(result, '!!!!')
if data_p.qsize() == 1:
    result -= data_p.get()

# print(result, '!!!!')
result += cnt_1

print(result)