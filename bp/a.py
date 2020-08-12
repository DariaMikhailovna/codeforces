def find(l, r, a, q):
    if l > r:
        return False
    m = (l + r) // 2
    if a[m] == q:
        return True
    if a[m] > q:
        return find(l, m - 1, a, q)
    if a[m] < q:
        return find(m + 1, r, a, q)


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    q = list(map(int, input().split()))
    for i in range(k):
        if find(0, n - 1, a, q[i]):
            print('YES')
        else:
            print("NO")


main()
