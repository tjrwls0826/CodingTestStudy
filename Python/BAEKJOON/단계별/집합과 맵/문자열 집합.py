# https://www.acmicpc.net/problem/14425
import sys

n, m = map(int, input().split())
own = []
compare = []
count = 0

for _ in range(n):
    own.append(sys.stdin.readline().strip())

for _ in range(m):
    compare.append(sys.stdin.readline().strip())

for i in compare:
    if i in own:
        count += 1

print(count)
