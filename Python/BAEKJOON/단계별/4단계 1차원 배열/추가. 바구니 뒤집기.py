# https://www.acmicpc.net/problem/10811
import sys

N, M = map(int, input().split())
ans = [0]
for i in range(1, N + 1):
    ans.append(i)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    ans[i:j+1] = reversed(ans[i:j+1])

print(*ans[1:])
