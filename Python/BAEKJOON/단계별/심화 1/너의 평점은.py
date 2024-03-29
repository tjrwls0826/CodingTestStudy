# https://www.acmicpc.net/problem/25206
import sys

total = 0
score_dic = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
cnt = 0
total_score = 0

for _ in range(20):
    name, score, achieve, = sys.stdin.readline().split()
    if achieve == "P":
        cnt += 1
        pass
    else:
        total += (float(score) * (score_dic[achieve]))
        total_score += float(score)

print(round((total / total_score), 6))
