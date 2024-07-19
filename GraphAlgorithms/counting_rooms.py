from collections import deque

WALL_CHARACTER = "#"
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def bfs(building, visited, i, j):
    n = len(building)
    m = len(building[0])
    queue = deque([(i, j)])
    visited[i][j] = True

    while len(queue) > 0:
        i, j = queue.popleft()

        for direction in DIRECTIONS:
            a, b = i + direction[0], j + direction[1]
            if a < 0 or a >= n or b < 0 or b >= m or visited[a][b] or building[a][b] == WALL_CHARACTER:
                continue

            queue.append((a, b))
            visited[a][b] = True


if __name__ == "__main__":
    n, m = [int(i) for i in input().split()]
    building = []
    visited = []

    for _ in range(n):
        building += [input()]
        visited += [[False] * m]

    rooms_count = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] or building[i][j] == WALL_CHARACTER:
                continue

            rooms_count += 1
            bfs(building, visited, i, j)

    print(rooms_count)
