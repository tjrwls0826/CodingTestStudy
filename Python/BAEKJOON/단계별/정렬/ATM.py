# https://www.acmicpc.net/problem/11399
import sys

n = int(input())
p = list(map(int,sys.stdin.readline().split()))
p.sort()
# print(p)
ans = []
for i in range(len(p)):
    for y in p[:i+1]:
        # print(y)
        ans.append(y)

print(sum(ans))