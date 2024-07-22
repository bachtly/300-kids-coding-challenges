if __name__ == "__main__":
    n, q = map(int, input().split())
    nums = map(int, input().split())

    accum_xor = [0]
    for num in nums:
        accum_xor.append(accum_xor[-1] ^ num)

    for _ in range(q):
        a, b = map(int, input().split())
        print(accum_xor[b] ^ accum_xor[a - 1])
