def part1():
    grid = []
    with open('day4.txt', 'r') as fp:
        for line in fp:
            row = [ch for ch in line if ch != '\n']
            grid.append(row)
    n = len(grid)
    def scan(i, j, next_i, next_j) -> bool:
        for k in range(3):
            i, j = next_i(i), next_j(j)
            if not (0 <= i < n and 0 <= j < n):
                return False

            if k == 0 and grid[i][j] != 'M':
                return False
            if k == 1 and grid[i][j] != 'A':
                return False
            if k == 2 and grid[i][j] != 'S':
                return False

        return True

    res = 0
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 'X':
                # top left
                if scan(r, c, lambda i: i - 1, lambda j: j - 1):
                    res += 1

                # top
                if scan(r, c, lambda i: i - 1, lambda j: j):
                    res += 1

                # top right
                if scan(r, c, lambda i: i - 1, lambda j: j + 1):
                    res += 1

                # middle left
                if scan(r, c, lambda i: i, lambda j: j - 1):
                    res += 1

                # middle right
                if scan(r, c, lambda i: i, lambda j: j + 1):
                    res += 1

                # bottom left
                if scan(r, c, lambda i: i + 1, lambda j: j - 1):
                    res += 1

                # bottom
                if scan(r, c, lambda i: i + 1, lambda j: j):
                    res += 1

                # bottom right
                if scan(r, c, lambda i: i + 1, lambda j: j + 1):
                    res += 1
    print(res)

def part2():
    grid = []
    with open('day4.txt', 'r') as fp:
        for line in fp:
            row = [ch for ch in line if ch != '\n']
            grid.append(row)
    n = len(grid)
    res = 0
    for r in range(1, n-1):
        for c in range(1, n-1):
            if grid[r][c] == 'A':
                # top
                if grid[r-1][c-1] == 'M' and grid[r-1][c+1] == 'M':
                    if grid[r+1][c-1] == 'S' and grid[r+1][c+1] == 'S':
                        res += 1

                # left
                if grid[r-1][c-1] == 'M' and grid[r+1][c-1] == 'M':
                    if grid[r-1][c+1] == 'S' and grid[r+1][c+1] == 'S':
                        res += 1

                # right
                if grid[r-1][c+1] == 'M' and grid[r+1][c+1] == 'M':
                    if grid[r-1][c-1] == 'S' and grid[r+1][c-1] == 'S':
                        res += 1

                # bottom
                if grid[r+1][c-1] == 'M' and grid[r+1][c+1] == 'M':
                    if grid[r-1][c-1] == 'S' and grid[r-1][c+1] == 'S':
                        res += 1
    print(res)


if __name__ == "__main__":
    part2()
