import math

G = 6.67408 * (10 ** (-11))  # 6.67408E-11 로 표현 가능
# 화성
M = 6.42 * (10 ** 23)  # 6.42E23 으로 표현 가능
r = 3396.2 * 1000  # km -> m
V = math.sqrt(2 * G * M / r)
print("화성의 탈출 속도: %f m/s" % V)

# 달
M = 7.3 * (10 ** 22)
r = 1737.5 * 1000
V = math.sqrt(2 * G * M / r)
print("달의 탈출 속도: %f m/s" % V)

# 토성
M = 5.68 * (10 ** 26)
r = 60268 * 1000
V = math.sqrt(2 * G * M / r)
print("토성의 탈출 속도: %f m/s" % V)

A = input()  # 창 안닫히는 용

'''
수업예시

name = '화성'
M = 6.42E23
r = 3396.2 * 1000
V = math.sqrt(2 * G * M / r)
print(f"{name}의 탈출속도: {V}m/s")
'''
