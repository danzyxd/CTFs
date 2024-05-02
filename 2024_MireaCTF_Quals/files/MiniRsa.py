flag = b"MIREACTF{}"
remainder = len(flag) % 5

if remainder:
    flag += b'\x00' * (5 - remainder)

flag = [int.from_bytes(flag[i - 5:i]) for i in range(5, len(flag) + 1, 5)]


e = 11

p = 1081789
q = 1081813

N = p*q


def crypt(text: list, e: int, n: int) -> bytes:
    encrypted_int = [pow(i, e, n) for i in text]

    return encrypted_int


print(N)
print(e)
c = crypt(flag, e, N)
print(c)