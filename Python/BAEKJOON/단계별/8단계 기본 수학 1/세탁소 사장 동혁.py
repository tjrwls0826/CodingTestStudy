# https://www.acmicpc.net/problem/2720

times = int(input())

for _ in range(times):
    totalM = int(input())
    output = []
    quarter = totalM // 25
    totalM = totalM % 25
    dime = totalM // 10
    totalM = totalM % 10
    nickel = totalM // 5
    totalM = totalM % 5
    output = [quarter, dime, nickel, totalM]
    print(*output)
