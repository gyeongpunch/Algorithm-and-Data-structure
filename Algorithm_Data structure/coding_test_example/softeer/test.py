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
    start = start.rjust(5, ' ') # start를 총 5글자로 생각하고 부족한 건 ' '로 왼쪽에 채우기
    end = end.rjust(5, ' ')

    # print(start, end, '!!!!!')
    result = 0

    for j in range(5):
        for k in range(7):
            if num_list[start[j]][k] != num_list[end[j]][k]:
                result += 1
    print(result)
