X, A, B = map(int, input().split())

if A >= B:
    ans = "delicious"
elif B - A <= X:
    ans = "safe"
else:
    ans = "dangerous"

print(ans)
