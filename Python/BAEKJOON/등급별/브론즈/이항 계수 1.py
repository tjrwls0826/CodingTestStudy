# https://www.acmicpc.net/problem/11050
import sys


def facto(x):
    if x == 0:
        return 1
    else:
        return x * facto(x - 1)


n, k = map(int, sys.stdin.readline().split())

print(int(facto(n) / (facto(k) * facto(n - k)))) # https://ko.wikipedia.org/wiki/이항_계수


