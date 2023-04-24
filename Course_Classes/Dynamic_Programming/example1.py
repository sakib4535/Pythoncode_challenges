"""
Suppose you are given a grid of size n x n, and you need to find all the paths that go from the top left corner to the
bottom right corner, moving only down or right at each step. A path is represented as a list of n strings, each of length n,
where the character 'R' represents a rightward move, and 'D' represents a downward move. For example, for n=3, one possible
path is ['RRD', 'DRR', 'DDR'].

To find all possible paths from the top left corner to the bottom right corner, we can use a recursive backtracking algorithm.
Starting from the top left corner, we can try moving right and down recursively until we reach the bottom right corner.
At each step, we can append either an R or D to our path list.

"""

def find_paths(row, col, path, n, solutions):
    if row == n-1 and col == n-1:
        solutions.append([''.join(row) for row in path])
    else:
        if row < n-1:
            path[row+1][col] = 'D'
            find_paths(row+1, col, path, n, solutions)
            path[row+1][col] = '-'
        if col < n-1:
            path[row][col+1] = 'R'
            find_paths(row, col+1, path, n, solutions)
            path[row][col+1] = '-'

def print_paths(paths):
    for path in paths:
        print('\n'.join(path))
        print()

n = 3
solutions = []
path = [['-']*n for _ in range(n)]
find_paths(0, 0, path, n, solutions)
print_paths(solutions)
