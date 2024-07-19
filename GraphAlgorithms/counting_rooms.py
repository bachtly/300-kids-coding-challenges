import time
from sys import stdin

WALL_CHARACTER = ord("#")
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def bfs(building, visited, i, j):
    n = len(building)
    m = len(building[0])
    stack = [(i, j)]
    visited[i][j] = True

    while len(stack) > 0:
        i, j = stack.pop()

        for direction in DIRECTIONS:
            a, b = i + direction[0], j + direction[1]
            if a < 0 or a >= n or b < 0 or b >= m or visited[a][b] or building[a][b] == WALL_CHARACTER:
                continue

            stack.append((a, b))
            visited[a][b] = True


if __name__ == "__main__":
    n, m = [int(i) for i in stdin.buffer.readline().split()]
    building = [''] * n
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        building[i] = stdin.buffer.readline().replace(b'\n', b'')

    rooms_count = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] or building[i][j] == WALL_CHARACTER:
                continue

            rooms_count += 1
            start = time.time_ns()
            bfs(building, visited, i, j)

    print(rooms_count)
