class OperationUpdateNode:
    def __init__(self, node, subordinates, adjacent):
        self.node = node
        self.subordinates = subordinates
        self.adjacent = adjacent

    def __call__(self):
        children = self.adjacent.get(self.node, [])
        self.subordinates[self.node] = sum([subordinates[i] for i in children]) + len(children)
        # print("update", locals())


class OperationVisitNode:
    def __init__(self, stack, node, subordinates, adjacent):
        self.stack = stack
        self.node = node
        self.subordinates = subordinates
        self.adjacent = adjacent

    def __call__(self):
        children = self.adjacent.get(self.node, [])
        self.stack.append(OperationUpdateNode(self.node, self.subordinates, self.adjacent))
        for child in children:
            if child in adjacent:
                self.stack.append(OperationVisitNode(self.stack, child, self.subordinates, self.adjacent))
        # print("visit", locals())


if __name__ == "__main__":
    n = int(input())
    managers = map(int, input().split())

    adjacent = dict()
    top_managers = [1]
    for i, manager in enumerate(managers):
        if manager != 0:
            if manager in adjacent:
                adjacent[manager].append(i + 2)
            else:
                adjacent[manager] = [i + 2]
        else:
            top_managers.append(i + 2)

    subordinates = [0] * (n + 1)
    stack = []
    for top_manager in top_managers:
        stack.append(OperationVisitNode(stack, top_manager, subordinates, adjacent))

    while stack:
        stack_item = stack.pop()
        stack_item()

    print(' '.join(map(str, subordinates[1:])))
