# https://www.acmicpc.net/problem/9506
import sys

N = 0

while True:
    N = int(sys.stdin.readline())
    A = []
    if N == -1:
        break

    for i in range(1, N + 1):
        if N % i == 0:
            A.append(i)

    if sum(A[:-1]) == N:
        print(N, "=", end=' ')
        for y in A[:-2]:
            print(y, "+", end=' ') # print(*l,sep=' + ') 언팩킹 후 sep로 출력하는 방법도 존재
        print(A[-2])

    else:
        print(N, "is NOT perfect.")
