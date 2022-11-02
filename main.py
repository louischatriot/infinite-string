


def get_position(n, offset):
    # TODO: actually implement it
    return n




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
                    end = str(end)[0:len(last)]

                    if end != last:
                        okay = False

                if okay:
                    get_position(start, 0)



    # s is the size of the first full number (if any)
    # l the size of the incomplete left hand number
    # r the size of the incomplete right hand number

    # Case when we span only one domain
    # for s in range(1, N + 1):
        # for l in range(0, s):
            # for r in range(0, s):
                # full = N - l - r
                # if full % s != 0:
                    # continue
                # pos.append([l] + ([s] * (full // s)) + [r])

    # # Case when we span two domains
    # for s1 in range(1, N - 1):
        # s2 = s1 + 1

        # pass

    # # Actually unsure about this way of splitting




    # for p in pos:
        # print(p)



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





