import sys
input = sys.stdin.readline

num_list = {
    '0' : '1110111',
    '1' : '0010010',
    '2' : '1011101',
    '3' : '1011011',
    '4' : '0111010',
    '5' : '1101011',
    '6' : '1101111',
    '7' : '1110010',
    '8' : '1111111',
    '9' : '1111011',
    ' ' : '0000000'
}
N = int(input())
for i in range(N):
    start, end = map(str, input().split())

    start_zero, end_zero = 5 - len(start), 5- len(end)
    start = ' ' * start_zero + start
    end = ' ' * end_zero + end

    result = 0

    for j in range(5):
        for k in range(7):
            if num_list[start[j]][k] != num_list[end[j]][k]:
                result += 1
    print(result)