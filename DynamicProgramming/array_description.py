if __name__ == "__main__":
    MOD = int(1e9 + 7)

    n_nums, upper_bound = [int(i) for i in input().split()]
    nums = [int(i) for i in input().split()]

    # the number of arrays that match conditions at current index
    dp = {i: 0 for i in range(1, upper_bound + 1)}

    # init the dp
    if nums[0] == 0:
        dp = {i: 1 for i in range(1, upper_bound + 1)}
    else:
        dp[nums[0]] = 1

    for num in nums[1:]:
        if num == 0:
            new_dp = {i: (dp.get(i - 1, 0) + dp.get(i, 0) + dp.get(i + 1, 0)) % MOD for i in range(1, upper_bound + 1)}
            dp = new_dp
        else:
            count = dp.get(num - 1, 0) + dp.get(num, 0) + dp.get(num + 1, 0)
            dp = {num: count % MOD}

    print(sum(dp.values()) % MOD)
