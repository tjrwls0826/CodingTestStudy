# https://www.acmicpc.net/problem/1620
import sys

n, m = map(int, sys.stdin.readline().strip().split())
pokename = dict()
pokenum = dict()
for i in range(n):
    pokename[i] = sys.stdin.readline().strip()
    pokenum[pokename[i]] = i

for y in range(m):
    x = sys.stdin.readline().strip()
    try:
        print(pokename.get(int(x) - 1))
    except:
        print(pokenum.get(x) + 1)

''' # 시간초과 발생 index는 O(N)이 걸리는 아주 느린 함수
n, m = map(int, sys.stdin.readline().strip().split())
poke = []

for _ in range(n):
    poke.append(sys.stdin.readline().strip())

for y in range(m):
    x = sys.stdin.readline().strip()
    try:
        print(poke[int(x) - 1])
    except:
        print(poke.index(x) + 1)  
'''
