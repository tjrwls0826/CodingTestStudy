# https://www.acmicpc.net/problem/10871
import sys

total, _num = map(int, input().split())
list = sys.stdin.readline().split()
answer = ""

for i in range(total):
    if int(list[i]) < _num:
        answer += f"{list[i]} "
print(answer)
