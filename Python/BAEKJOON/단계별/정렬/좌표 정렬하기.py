# https://www.acmicpc.net/problem/11650
import sys

n = int(input())
lst = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    lst.append([x, y])

lst.sort()

for i in range(len(lst)):
    print(*lst[i])
