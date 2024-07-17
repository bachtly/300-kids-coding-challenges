if __name__ == "__main__":
    n = int(input())
    nums = [int(num_str) for num_str in input().split(" ")]

    sum_1_n = (1 + n) * n // 2
    print(sum_1_n - sum(nums))
