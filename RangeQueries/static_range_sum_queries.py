if __name__ == "__main__":
    n, q = map(int, input().split())
    nums = map(int, input().split())

    accum_sums = [0]
    for num in nums:
        accum_sums.append(accum_sums[-1] + num)

    for _ in range(q):
        a, b = map(int, input().split())
        print(accum_sums[b] - accum_sums[a - 1])
