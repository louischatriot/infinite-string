logging = False

def log(s):
    if logging:
        print(s)

def get_position(n):
    res = 0
    N = len(str(n))

    for i in range(0, N-1):
        res += (10 ** (i+1) - 10 ** i) * (i+1)

    res += N * (n - 10 ** (N-1))
    return res

# n is a full number (not a part of the left most number)
def is_compatible(n, s):
    i = 0
    while i < len(s):
        n_s = str(n)

        if len(s) - i < len(n_s):
            n_s = n_s[0:len(s)-i]
            if n_s != s[i:]:
                return False
        else:
            if s[i:i+len(n_s)] != n_s:
                return False

        i += len(n_s)
        n += 1

    return True

# Length of num is between 2 and 15 so we can never span three domains
def find_position(num):
    N = len(num)
    pos = []

    if num == '0' * N:
        return get_position(int('1' + num)) + 1


    # ns is number size, ad is actual digits in the beginning of num
    for ns in range(1, N+1):
        for ad in range(1, ns+1):
            first_s_end = num[0:ad]

            if ns == ad:
                first_s = first_s_end
                if first_s[0] != "0":
                    pos.append((int(first_s), num, 0))

                continue

            if num[ad] == "0":
                continue

            if first_s_end == '9' * ad:
                missing = ns-ad
                next_s_beg = num[ad:ad+missing]

                if len(next_s_beg) == missing and next_s_beg == '1' + '0' * (missing - 1):
                    next_s = '1' + '0' * ns
                else:
                    next_s = next_s_beg + '0' * ad

                pos.append((int(next_s), num[ad:], ad))
                continue

            # first_s_end is not only nines
            missing = ns-ad
            next_s_beg = num[ad:ad+missing]
            first_s = next_s_beg + '0' * (missing - len(next_s_beg)) + first_s_end
            next = int(first_s) + 1

            pos.append((next, num[ad:], ad))

    res = 1e30 + int(num)
    for n, s, offset in pos:
        if is_compatible(n, s):
            res = min(res, get_position(n) - offset)

    return res







tests = [
    ("00", 190),
    ("040", 1091),
    ("456", 3),
    ("454", 79),
    ("455", 98),
    ("910", 8),
    ("9100", 188),
    ("99100", 187),
    ("00101", 190),
    ("001", 190),
    ("123456789", 0),
    ("1234567891", 0),
    ("123456798", 1000000071)
]


for num, correct in tests:
    res = find_position(num)
    if res != correct:
        print(f"ERROR - for {num} - found {res} - correct answer {correct}")





