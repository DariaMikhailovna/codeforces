from math import sqrt, pow


def is_prime(number):
    if number == 1:
        return False
    if number != 2 and number % 2 == 0:
        return False
    i = 3
    while i * i <= number:
        if number % i == 0:
            return False
        i += 2
    return True


n = int(input())
s = list(map(int, input().split()))
for x in s:
    if pow(int(sqrt(x)), 2) != x:
        print('NO')
        continue
    if is_prime(int(sqrt(x))):
        print('YES')
    else:
        print('NO')
