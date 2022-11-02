



def findPosition(num):
    return 0





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





