# https://www.acmicpc.net/problem/9063
import sys

N = int(input())
xlist = []
ylist = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    xlist.append(x)
    ylist.append(y)

print((max(xlist) - min(xlist)) * (max(ylist) - min(ylist)))
