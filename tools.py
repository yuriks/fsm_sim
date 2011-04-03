def compare(bl, s, reverse=True):
    for bit, char in zip(bl, reverse and s[::-1] or s):
        if char != '-' and bit != bool(int(char)):
            return False
    return True

def string_to_bools(s):
    return [bool(int(i)) for i in s[::-1]]

def bools_to_int(bs):
    val = 0
    for i in bs[::-1]:
        val <<= 1
        if i:
            val += 1
    return val
