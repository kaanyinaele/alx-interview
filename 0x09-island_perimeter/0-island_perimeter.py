#!/usr/bin/python3

def island_perimeter(grid):
    """ Get the dimensions of the grid
    """
    rows, cols = len(grid), len(grid[0])
    
    """ Create a visited matrix to keep track of explored cells
    """
    visited = [[False] * cols for _ in range(rows)]
    
    """ Initialize perimeter counter
    """
    perimeter = 0
    
    def bfs(row, col):
        """Check if the current cell is out of bounds or water.
        """
        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0 or visited[row][col]:
            return True
        
        """ Mark the cell as visited
        """
        visited[row][col] = True
        
        """ Define all possible directions to explore
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        """ Explore neighboring cells
        """
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if bfs(new_row, new_col):
                return True
        
        """ If no water cell found, return False
        """
        return False
    
    """ Traverse the grid and calculate perimeter
    """
    for r in range(rows):
        for c in range(cols):
            """ Check if current cell is land and not visited
            """
            if grid[r][c] == 1 and not visited[r][c]:
                """ Start BFS traversal from this cell
                """
                if bfs(r, c):
                    """Increment perimeter if BFS returns True
                    """
                    perimeter += 1
    
    """ Return the total calculated perimeter
    """
    return perimeter