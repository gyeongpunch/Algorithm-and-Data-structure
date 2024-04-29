import sys
input = sys.stdin.readline

result = 0
for i in range(5):
    start, end = input().split()
    start_h, start_m = start.split(':')
    end_h, end_m = end.split(':')
    start_h, start_m, end_h, end_m = int(start_h), int(start_m), int(end_h), int(end_m)

    # print(start_h, '!!!')
    # print(end_h, '!!!')
    # print(start_m, '!!!')
    # print(end_m, '!!!')

    if start_m > end_m:
        end_h -= 1
        end_m += 60
    
    result += (end_h - start_h) * 60 + (end_m - start_m)

print(result)