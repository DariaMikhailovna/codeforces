n = int(input())
a = list(map(int, input().split()))
s = sum(a)
c = s / 3
if int(c) != c or n < 3:
    print(0)
    exit()
if n == 3 and not a[0] == a[1] == a[2]:
    print(0)
    exit()
i = 0
ss = 0
f = True
while ss < c and i < n:
    f = False
    ss += a[i]
    i += 1
if f:
    ss += a[i]
    i += 1
if ss > c:
    print(0)
    exit()
ss = 0
while ss < c and i < n:
    ss += a[i]
    i += 1
if f:
    ss += a[i]
    i += 1
if ss > c:
    print(0)
    exit()
r = 1
while a[i] == 0 and i < n:
    r += 1
    i += 1
print(r)
