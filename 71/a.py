n = int(input())
s = list()
for x in range(n):
    s.append(input())
for x in s:
    r = ""
    le = len(x)
    if le <= 10:
        print(x)
        continue
    r += x[0]
    r += str(le - 2)
    r += x[le - 1]
    print(r)
