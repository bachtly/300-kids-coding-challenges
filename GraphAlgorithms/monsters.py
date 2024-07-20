CELL_MONSTERS = "M"
CELL_PLAYER = "A"
CELL_WALL = "#"
CELL_EMPTY = "."
DIRECTIONS = [(-1, 0, 'U'), (1, 0, 'D'), (0, 1, 'R'), (0, -1, 'L')]


def is_valid_cell(i, j, n, m):
    return 0 <= i < n and 0 <= j < m


def is_border_cell(i, j, n, m):
    return is_valid_cell(i, j, n, m) and (i == n - 1 or i == 0 or j == 0 or j == m - 1)


def print_result(final_i, final_j, init_i, init_j, player_moves_tracing, n, m):
    tracing_moves = []
    i, j = final_i, final_j
    while i != init_i or j != init_j:
        i, j, move = player_moves_tracing[i * m + j]
        tracing_moves.append(move)

    print('YES')
    print(len(tracing_moves))
    for i in range(len(tracing_moves)):
        print(tracing_moves[len(tracing_moves) - i - 1], end='')


def main():
    n, m = map(int, input().split())
    labyrinth = [list(input()) for _ in range(n)]

    monsters_positions = [(i, j) for i in range(n) for j in range(m) if labyrinth[i][j] == CELL_MONSTERS]
    player_positions = [(i, j) for i in range(n) for j in range(m) if labyrinth[i][j] == CELL_PLAYER]
    init_i, init_j = player_positions[0]

    # special case
    if is_border_cell(init_i, init_j, n, m):
        print('YES')
        print('0')
        return

    # each turn, we allow player and monsters to expand their controlled area
    # player is not allowed to enter the cell under control of a monster
    player_moves_tracing = [-1] * (m * n)
    while len(player_positions) > 0:
        # monsters move first
        new_monsters_positions = []
        for i, j in monsters_positions:
            for di, dj, _ in DIRECTIONS:
                if is_valid_cell(i + di, j + dj, n, m) and labyrinth[i + di][j + dj] == CELL_EMPTY:
                    labyrinth[i + di][j + dj] = CELL_MONSTERS
                    new_monsters_positions.append((i + di, j + dj))
        monsters_positions = new_monsters_positions

        # player moves
        new_player_positions = []
        for i, j in player_positions:
            for di, dj, move in DIRECTIONS:
                if not is_valid_cell(i + di, j + dj, n, m) or labyrinth[i + di][j + dj] != CELL_EMPTY:
                    continue

                # if reaching the border
                if is_border_cell(i + di, j + dj, n, m):
                    player_moves_tracing[(i + di) * m + (j + dj)] = (i, j, move)
                    final_i, final_j = i + di, j + dj

                    print_result(final_i, final_j, init_i, init_j, player_moves_tracing, n, m)
                    return

                labyrinth[i][j] = CELL_MONSTERS
                labyrinth[i + di][j + dj] = CELL_MONSTERS
                new_player_positions.append((i + di, j + dj))
                player_moves_tracing[(i + di) * m + (j + dj)] = (i, j, move)

            player_positions = new_player_positions

    print('NO')


if __name__ == "__main__":
    main()
