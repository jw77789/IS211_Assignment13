def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

  def compareTo(s1, s2):
    if not s1 and not s2:
        return 0
    elif not s1:
        return -ord(s2[0])
    elif not s2:
        return ord(s1[0])
    elif s1[0] != s2[0]:
        return ord(s1[0]) - ord(s2[0])
    else:
        return compareTo(s1[1:], s2[1:])
