def knight_moves(x, y):
    return [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]

def king_moves(x, y):
    return [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def bfs():
    q = [(start_position, "K")]
    d = 0
    while q:
        d += 1
        for _ in range(len(q)):
            pos, state = q.pop(0)
            cur_i, cur_j = pos
            for di, dj in direction[state]:
                i, j = cur_i + di, cur_j + dj
                if i < 0 or i >= n or j < 0 or j >= n or (i, j) in visited[state]:
                    continue
                if (i, j) == end_position:
                    return d
                elif board[i][j] not in (".", "S"):
                    q.append(((i, j), board[i][j]))
                    visited[board[i][j]].add((i, j))
                else:
                    q.append(((i, j), state)) 
                    visited[state].add((i, j))
    return -1

n = int(input())
board = []
start_position = (-1, -1)
end_position = (-1, -1)

for i in range(n):
    row = input()
    if "S" in row:
        start_position = (i, row.index("S"))
    elif "F" in row:
        end_position = (i, row.index("F"))
    board.append(row)

q = [(start_position, "K")]
direction = {
    "K": knight_moves(start_position[0], start_position[1]),
    "G": king_moves(start_position[0], start_position[1])
}
visited = {
    "K": set([start_position]),
    "G": set()
}
print()
result = bfs()
print(result)
