import sys
import itertools
import bisect

def sieve(limit):
    """Sang Eratosthenes: tra cuu nhanh so nguyen to trong [0, limit]."""
    is_p = bytearray([1]) * (limit + 1)
    is_p[0] = is_p[1] = 0
    for i in range(2, int(limit ** 0.5) + 1):
        if is_p[i]:
            is_p[i * i::i] = bytearray(len(is_p[i * i::i]))
    return is_p


_WITNESSES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)

def is_prime(n):
    """Miller-Rabin tat dinh - dung chinh xac 100% voi n < 3.3*10^24,
    thua du cho n toi 9 chu so trong de bai nay."""
    if n < 2:
        return False
    for p in _WITNESSES:
        if n % p == 0:
            return n == p
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in _WITNESSES:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def build_pure_primes():
    """Sinh truoc toan bo so 'thuan nguyen to' (<= 9 chu so).
    Vi chu so phai thuoc {2,3,5,7} nen tong so ung vien chi la
    4+4^2+...+4^9 = 349524 so - rat nho, duyet & kiem tra het trong < 1s."""
    sum_is_prime = sieve(70)  # tong chu so toi da la 9*7 = 63
    digit_choices = (2, 3, 5, 7)
    pure_primes = []
    for length in range(1, 10):
        for combo in itertools.product(digit_choices, repeat=length):
            num, digit_sum = 0, 0
            for d in combo:
                num = num * 10 + d
                digit_sum += d
            if sum_is_prime[digit_sum] and is_prime(num):
                pure_primes.append(num)
    pure_primes.sort()
    return pure_primes


def main():
    pure_primes = build_pure_primes()

    stdin = sys.stdin
    stdout = sys.stdout
    t = int(stdin.readline())

    out = []
    for _ in range(t):
        a_str, b_str = stdin.readline().split()
        a, b = int(a_str), int(b_str)
        if a > b:
            a, b = b, a
        lo = bisect.bisect_left(pure_primes, a)
        hi = bisect.bisect_right(pure_primes, b)
        out.append(str(hi - lo))
        if len(out) >= 20000:   # xa bo dem dinh ky de khong tich bo nho
            stdout.write('\n'.join(out))
            stdout.write('\n')
            out = []
    if out:
        stdout.write('\n'.join(out))
        stdout.write('\n')


if __name__ == '__main__':
    main()