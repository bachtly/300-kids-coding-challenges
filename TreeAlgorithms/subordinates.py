def visit(node, subordinates):
    cnt = 0
    for child in adjacent.get(node, []):
        visit(child, subordinates)
        cnt += subordinates[child - 1] + 1

    subordinates[node - 1] = cnt


if __name__ == "__main__":
    n = int(input())
    managers = map(int, input().split())

    adjacent = dict()
    top_managers = [1]
    for i, manager in enumerate(managers):
        if manager != 0:
            adjacent[manager] = adjacent.get(manager, []) + [i + 2]
        else:
            top_managers.append(i + 2)

    subordinates = [0] * n

    for i in top_managers:
        visit(i, subordinates)

    print(' '.join(map(str, subordinates)))
