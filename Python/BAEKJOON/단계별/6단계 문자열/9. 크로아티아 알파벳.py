# https://www.acmicpc.net/problem/2941


inp = input()
cro_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
ans = 0

for i in cro_alpha:
    if i in inp:
        ans += inp.count(i)
        inp = inp.replace(i, ' ')

print(ans + len(inp.replace(' ', '')))

# 개선한 풀이

inp = input()
cro_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in cro_alpha:
    inp = inp.replace(i,' ')
print(len(inp))