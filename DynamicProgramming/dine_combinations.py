from collections import deque

if __name__ == "__main__":
    n = int(input())

    dp = deque([0] * 6)
    for i in range(1, n + 1):
        dp.append((sum(dp) + (1 if i <= 6 else 0)) % int(1e9 + 7))
        dp.popleft()

    print(dp[-1])
