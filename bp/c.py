import math


def find(l, r, a, q):
    if r == l:
        return r
    m = (l + r) // 2
    if a[m] >= q:
        return find(l, m, a, q)
    else:
        return find(m + 1, r, a, q)


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, -math.inf)
    a.append(math.inf)
    q = list(map(int, input().split()))
    for i in range(k):
        print(find(0, n + 1, a, q[i]))


main()
