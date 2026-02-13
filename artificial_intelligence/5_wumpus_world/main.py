import random

# ==========================================
# WORLD
# ==========================================

def create_board(n):
    return [[[] for _ in range(n)] for _ in range(n)]


def get_neighbors(n, r, c):
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    result = []
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n:
            result.append((nr, nc))
    return result


def add_adjacent(board, n, r, c, symbol):
    for nr, nc in get_neighbors(n, r, c):
        if symbol not in board[nr][nc]:
            board[nr][nc].append(symbol)


def generate_world(n, pit_count):
    board = create_board(n)

    positions = [(i,j) for i in range(n) for j in range(n)]
    positions.remove((0,0))

    pits = random.sample(positions, pit_count)
    for r, c in pits:
        board[r][c].append("P")
        add_adjacent(board, n, r, c, "B")

    remaining = [p for p in positions if p not in pits]

    wr, wc = random.choice(remaining)
    board[wr][wc].append("W")
    add_adjacent(board, n, wr, wc, "S")

    remaining.remove((wr, wc))

    gr, gc = random.choice(remaining)
    board[gr][gc].append("G")

    return board


def print_board(board):
    for row in board:
        print(["".join(cell) if cell else "." for cell in row])
    print()


# ==========================================
# KNOWLEDGE
# ==========================================

def create_knowledge(n):
    return [["UNKNOWN" for _ in range(n)] for _ in range(n)]


def update_knowledge(board, knowledge, n, pos):
    r, c = pos
    percepts = board[r][c]
    knowledge[r][c] = "VISITED"

    neighbors = get_neighbors(n, r, c)

    if "B" not in percepts and "S" not in percepts:
        for nr, nc in neighbors:
            if knowledge[nr][nc] == "UNKNOWN":
                knowledge[nr][nc] = "SAFE"

    if "B" in percepts:
        for nr, nc in neighbors:
            if knowledge[nr][nc] == "UNKNOWN":
                knowledge[nr][nc] = "P?"

    if "S" in percepts:
        for nr, nc in neighbors:
            if knowledge[nr][nc] == "UNKNOWN":
                knowledge[nr][nc] = "W?"


def advanced_inference(board, knowledge, n):
    for _ in range(5):  # limit iterations (prevents freeze)

        changed = False

        for r in range(n):
            for c in range(n):

                if knowledge[r][c] != "VISITED":
                    continue

                percepts = board[r][c]
                neighbors = get_neighbors(n, r, c)

                unknown = []
                for nr, nc in neighbors:
                    if knowledge[nr][nc] in ["UNKNOWN", "P?", "W?"]:
                        unknown.append((nr, nc))

                # If Breeze and only 1 possible cell
                if "B" in percepts and len(unknown) == 1:
                    nr, nc = unknown[0]
                    if knowledge[nr][nc] != "PIT":
                        knowledge[nr][nc] = "PIT"
                        changed = True

                # If no Breeze -> safe
                if "B" not in percepts:
                    for nr, nc in neighbors:
                        if knowledge[nr][nc] in ["UNKNOWN", "P?"]:
                            knowledge[nr][nc] = "SAFE"
                            changed = True

                # If no Stench -> safe from Wumpus
                if "S" not in percepts:
                    for nr, nc in neighbors:
                        if knowledge[nr][nc] in ["UNKNOWN", "W?"]:
                            knowledge[nr][nc] = "SAFE"
                            changed = True

        if not changed:
            break


# ==========================================
# MOVE SELECTION
# ==========================================

def choose_next_move(board, knowledge, n, visited_stack):

    # 1️⃣ Prefer SAFE unexplored
    for i in range(n):
        for j in range(n):
            if knowledge[i][j] == "SAFE":
                return (i, j)

    # 2️⃣ If stuck → choose least risky cell (guess)
    candidates = []
    for i in range(n):
        for j in range(n):
            if knowledge[i][j] in ["UNKNOWN", "P?", "W?"]:
                candidates.append((i, j))

    if candidates:
        print("⚠️ Guessing...")
        return random.choice(candidates)

    # 3️⃣ Backtrack
    if visited_stack:
        return visited_stack.pop()

    return None


# ==========================================
# SOLVER
# ==========================================

def solve_wumpus(n=4, pit_count=3):

    board = generate_world(n, pit_count)
    knowledge = create_knowledge(n)

    pos = (0,0)
    visited_stack = []

    print("=== REAL BOARD (DEBUG) ===")
    print_board(board)

    while True:

        r, c = pos
        cell = board[r][c]

        if "P" in cell:
            print("💀 Fell into PIT!")
            break

        if "W" in cell:
            print("👹 Killed by WUMPUS!")
            break

        if "G" in cell:
            print("🏆 GOLD FOUND! Agent wins!")
            break

        update_knowledge(board, knowledge, n, pos)
        advanced_inference(board, knowledge, n)

        next_move = choose_next_move(board, knowledge, n, visited_stack)

        if not next_move:
            print("No moves left.")
            break

        visited_stack.append(pos)
        pos = next_move

    print("\n=== AGENT KNOWLEDGE ===")
    for row in knowledge:
        print(row)


# ==========================================
# RUN
# ==========================================

if __name__ == "__main__":
    solve_wumpus(n=4, pit_count=3)
