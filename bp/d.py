import math


def find_l(l, r, a, q):
    if r == l:
        return r
    m = (l + r) // 2
    if a[m] >= q:
        return find_l(l, m, a, q)
    else:
        return find_l(m + 1, r, a, q)


def find_r(l, r, a, q):
    if r == l:
        return l
    m = (l + r + 1) // 2
    if a[m] > q:
        return find_r(l, m - 1, a, q)
    else:
        return find_r(m, r, a, q)


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.insert(0, -math.inf)
    a.append(math.inf)
    k = int(input())
    for i in range(k):
        l, r = map(int, input().split())
        rr = find_r(0, n + 1, a, r)
        ll = find_l(0, n + 1, a, l)
        print(rr + 1 - ll)


main()

"""
Второй способ:
def find_l(l, r, a, q):
    if r == l:
        return r
    m = (l + r) // 2
    if a[m] >= q:
        return find_l(l, m, a, q)
    else:
        return find_l(m + 1, r, a, q)


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    k = int(input())
    for i in range(k):
        l, r = map(int, input().split())
        rr = find_l(0, n, a, r + 1)
        ll = find_l(0, n, a, l)
        print(rr - ll)


main()
"""