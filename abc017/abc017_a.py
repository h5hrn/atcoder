total = 0

for _ in range(3):
    s, e = map(int, input().split())
    total += s * e // 10

print(total)
