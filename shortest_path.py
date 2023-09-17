"""
Problem: Finding the shortest path weight using Dijkstra's algorithm
Author: Chanon Buathan
Example usage: python shortest_path.py {file_name} 
"""

import sys
import heapq


def find_shortest_path(grid):
    num_rows = len(grid)
    num_cols = len(grid[0])
    min_dist = [[sys.maxsize] * num_cols for _ in range(num_rows)]
    min_dist[0][0] = grid[0][0]

    heap = [(grid[0][0], 0, 0)]
    visited = set()

    while heap:
        (distance, row, col) = heapq.heappop(heap)

        if (row, col) in visited:
            continue

        visited.add((row, col))

        for neighbor_row, neighbor_col in [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1),
        ]:
            if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                next_distance = distance + grid[neighbor_row][neighbor_col]
                if next_distance < min_dist[neighbor_row][neighbor_col]:
                    min_dist[neighbor_row][neighbor_col] = next_distance
                    heapq.heappush(heap, (next_distance, neighbor_row, neighbor_col))

    return min_dist[num_rows - 1][num_cols - 1]


if __name__ == "__main__":
    filename = sys.argv[1]
    grid = []
    with open(filename, "r") as f:
        for line in f:
            row = list(map(int, line.split()))
            grid.append(row)

    shortest_path = find_shortest_path(grid)
    print(f"Shortest path for {filename}: {shortest_path}")
