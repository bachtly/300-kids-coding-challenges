class SegmentTreeMax:
    def __init__(self, arr, default_value):
        """
        Parameters
        ----------
        arr :
           The base array
        """

        self.n = len(arr)
        self.tree = [0] * (4 * len(arr))
        self.default_value = default_value

        for idx, num in enumerate(arr):
            self.update(idx + 1, num)

    def update(self, position, value):
        # print(locals())

        # remove recursion by a stack (idx, left, right)
        stack = [(1, 1, self.n)]
        while stack:
            if isinstance(stack[-1], tuple) and len(stack[-1]) == 3:
                idx, left, right = stack.pop()

                if left == right:
                    self.tree[idx] = value
                    continue

                else:
                    # when see integer in stack, it is the tree node, update that node
                    stack.append(idx)
                    mid = (left + right) // 2
                    if left <= position <= mid:
                        stack.append((idx * 2, left, mid))
                    if mid + 1 <= position <= right:
                        stack.append((idx * 2 + 1, mid + 1, right))
            else:
                tree_idx = stack.pop()
                self.tree[tree_idx] = max(self.tree[tree_idx * 2], self.tree[tree_idx * 2 + 1])

    def max(self):
        return self.tree[1]

    def left_most_ge(self, value):
        if value > self.tree[1]:
            return 0

        # remove recursion by a stack (idx, left, right)
        stack = [(1, 1, self.n)]
        while stack:
            idx, left, right = stack.pop()

            if left == right:
                return left

            mid = (left + right) // 2
            if self.tree[idx * 2] >= value:
                stack.append((idx * 2, left, mid))
                continue
            else:
                stack.append((idx * 2 + 1, mid + 1, right))
                continue

        return self.default_value


if __name__ == "__main__":
    n, m = map(int, input().split())
    hotels = [int(i) for i in input().split()]

    tree = SegmentTreeMax(hotels, 0)

    groups = map(int, input().split())
    for group in groups:
        if group > tree.max():
            print('0', end=' ')
            continue

        # now left is first matched
        left_most_ge = tree.left_most_ge(group)
        hotels[left_most_ge - 1] -= group
        tree.update(left_most_ge, hotels[left_most_ge - 1])

        print(left_most_ge, end=' ')
