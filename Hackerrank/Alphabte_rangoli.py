import string


def print_rangoli(size):
    alpha = string.ascii_lowercase

    # Top part (FIXED)
    for i in range(size - 1, -1, -1):
        s = "-".join(alpha[i:size])
        print((s[::-1] + s[1:]).center(4 * size - 3, "-"))

    # Bottom part
    for i in range(1, size):
        s = "-".join(alpha[i:size])
        print((s[::-1] + s[1:]).center(4 * size - 3, "-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)