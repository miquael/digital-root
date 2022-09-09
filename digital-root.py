# digital root
# from Wikipedia: https://en.wikipedia.org/wiki/Digital_root

def digit_sum(x: int, b: int) -> int:
    total = 0
    while x > 0:
        total = total + (x % b)
        x = x // b
    return total

def digital_root(x: int, b: int) -> int:
    seen = set()
    while x not in seen:
        seen.add(x)
        x = digit_sum(x, b)
    return x

def additive_persistence(x: int, b: int) -> int:
    seen = set()
    while x not in seen:
        seen.add(x)
        x = digit_sum(x, b)
    return len(seen) - 1