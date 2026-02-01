import random
from collections import Counter 

def execute(N: int, dust: int = 9):
    mat: list[list[int]] = [[0] * N for _ in range(N)]

    def put_dust_random(room: list[list[int]], walls_count: int, size: int) -> list[list[int]]:
        while walls_count > 0:
            i, j = random.randint(0, size - 1), random.randint(0, size - 1)
            if room[i][j] == 0:
                walls_count -= 1
                room[i][j] = 1

        return room

    mat = put_dust_random(mat, dust, N)
    visited: set[tuple] = set() # (i, j)
    directions: list[tuple] = [(0, 1), (0, -1), (1, 0), (-1, 0)] 

    res = [0]
    temp_dust = [dust]

    def count_steps_to_clean_room(i, j):
        res[0] += 1
        if (i, j) in visited or i < 0 or i >= N or j < 0 or j >= N:
            return False
        
        visited.add((i, j))
        if mat[i][j] == 1:
            temp_dust[0] -= 1
            if temp_dust[0] == 0:
                return True

        for di, dj in directions:
            if count_steps_to_clean_room(i + di, j + dj):
                return True
        return False



    count_steps_to_clean_room(0, 0)
    return res[0]

res = []
for _ in range(100):
    res.append(execute(7))

print(Counter(res))