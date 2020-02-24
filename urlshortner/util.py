_BASE = 62

base_list = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
base = len(base_list)


def encode(num: int):
    result = []
    if num == 0:
        result.append(base_list[0])

    while num > 0:
        result.append(base_list[num % base])
        num //= base

    return "".join(reversed(result))


def decode(code: str):
    num = 0
    code_list = list(code)
    for index, code in enumerate(reversed(code_list)):
        num += base_list.index(code) * base ** index
    return num
