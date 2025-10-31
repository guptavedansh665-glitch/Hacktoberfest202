a = int(input())
b = int(input())

for n in range(a, b + 1):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    if s == n:
        print(n, end=" ")
