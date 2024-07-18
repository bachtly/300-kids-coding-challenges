# The issue with this problem is when I tried getting the input array by [int(i) for i in input().split()] which caused
# TLE when submission. Interestingly, the length of the whole text input of the TLE test is not more complicated than
# other passed test. No idea what happened!

if __name__ == "__main__":
    n = int(input())
    nums = [i for i in input().split()]

    print(len(set(nums)))
