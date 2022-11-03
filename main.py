


def get_position(n, offset=0):
    res = 0
    N = len(str(n))

    for i in range(0, N-1):
        res += (10 ** (i+1) - 10 ** i) * (i+1)

    res += N * (n - 10 ** (N-1))
    return res + offset


# Length of num is between 2 and 15 so we can never span three domains
def findPosition(num):
    N = len(num)

    pos = []

    print(num)

    # ns is number size, ad is actual digits in the beginning of num
    for ns in range(1, N+1):
        for ad in range(1, ns+1):
            # Full number at the start of num
            if ns == ad:
                okay = True

                start = int(num[0:ns])

                for j in range(1, N // ns):
                    number = int(num[j * ns:(j+1) * ns])
                    if number != start + j:
                        okay = False
                        break

                if N % ns != 0:
                    last = num[ns * (N // ns):]
                    end = start + (N // ns)
                    end_s = str(end)[0:len(last)]

                    if end_s != last:
                        okay = False

                if okay:
                    get_position(start, 0)

                continue

            # Case where we only have the last ad digits of the first number
            # Maybe the same as the previous one actually
            okay = True

            start_s = num[0:ad]
            next_s = num[ad:ad+ns]

            # We have a full number after the first incomplete one
            if len(next_s) == ns:
                next = int(next_s)
                if str(next - 1)[ns-ad:] != start_s:
                    pass






    return 0




findPosition("1234567890")





1/0



tests = [
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
    res = findPosition(num)
    if res != correct:
        print(f"ERROR - for {num} - found {res} - correct answer {correct}")





