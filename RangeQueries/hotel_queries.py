class SegmentTree:
    def __init__(self, arr, combine, default_value):
        """
        Parameters
        ----------
        arr :
           The base array
        combine :
           Method to aggregate two nodes (e.g. max, sum)
        """

        self.n = len(arr)
        self.tree = [0] * (4 * len(arr))
        self.combine = combine
        self.default_value = default_value

        for idx, num in enumerate(arr):
            self.update(idx + 1, num)

    def update(self, position, value):
        # print(locals())
        self._update(1, 1, self.n, position, value)
        # self.print_prefix_sum()

    def _update(self, idx, left, right, position, value):
        # print(locals())

        if not left <= position <= right:
            return

        if left == right:
            self.tree[idx] = value
            return

        mid = (left + right) // 2
        self._update(idx * 2, left, mid, position, value)
        self._update(idx * 2 + 1, mid + 1, right, position, value)
        self.tree[idx] = self.combine(self.tree[idx * 2], self.tree[idx * 2 + 1])

    def get(self, left, right):
        return self._get(1, 1, self.n, left, right)

    def _get(self, idx, left, right, query_left, query_right):
        # print(locals())
        if query_left <= left and right <= query_right:
            return self.tree[idx]

        if query_left > right or query_right < left:
            return self.default_value

        mid = (left + right) // 2
        left_branch = self._get(idx * 2, left, mid, query_left, query_right)
        right_branch = self._get(idx * 2 + 1, mid + 1, right, query_left, query_right)
        return self.combine(left_branch, right_branch)

    def print_prefix_sum(self):
        for i in range(1, self.n + 1):
            print(self.get(1, i), end=' ')
        print()


if __name__ == "__main__":
    n, m = map(int, input().split())
    hotels = [int(i) for i in input().split()]

    tree = SegmentTree(hotels, max, 0)

    groups = map(int, input().split())
    for group in groups:
        if group > tree.get(1, n):
            print('0', end=' ')
            continue

        left = 1
        right = n
        while left < right:
            mid = (left + right) // 2
            max_prefix = tree.get(1, mid)
            if max_prefix >= group:
                right = mid
            else:
                left = mid + 1

        # now left is first matched
        hotels[left - 1] -= group
        tree.update(left, hotels[left - 1])

        # tree.print_prefix_sum()
        print(left, end=' ')
