def generate_weird_number(init_num):
    if init_num != 1:
        if init_num % 2 == 0:
            yield init_num // 2
            yield from generate_weird_number(init_num // 2)

        yield init_num * 3 + 1
        yield from generate_weird_number(init_num * 3 + 1)


if __name__ == "__main__":
    num = int(input())

    print(num, end=" ")
    while num != 1:
        num = next(generate_weird_number(num))
        print(num, end=" ")
