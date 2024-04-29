import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)

def Execute(a, b):
    ret = [0] * 2
    if b == 0:
        ret[0] = 1
        ret[1] = 0
        return ret
    q = a // b
    v = Execute(b, a % b)
    ret[0] = v[1]
    ret[1] = v[0] - v[1] * q
    return ret

mgcd = GCD(A, B)

if C % mgcd != 0:
    print(-1)
else:
    mok = C // mgcd
    ret = Execute(A, B)
    print(ret[0] * mok, ret[1] * mok)