


# Length of num is between 2 and 15 so we can never span three domains
def findPosition(num):
    N = len(num)

    pos = []

    # s is the size of the first full number (if any)
    # l the size of the incomplete left hand number
    # r the size of the incomplete right hand number
    for s in range(1, N + 1):
        # Case when we span only one domain
        for l in range(0, s):
            for r in range(0, s):
                full = N - l - r
                if full % s != 0:
                    continue
                pos.append([l] + ([s] * (full // s)) + [r])



    for p in pos:
        print(p)



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





