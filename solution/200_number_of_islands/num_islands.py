class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        if not grid:
            return 0
        num = 0
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid = []
        for i in range(0, self.rows):
            row = [c for c in grid[i]]
            self.grid.append(row)
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                if self.grid[i][j] == '1':
                    num += 1
                    self.bfs(i, j)
        return num

    def bfs(self, i, j):
        queue = [(i, j)]
        while queue:
            i, j = queue.pop(0)
            self.grid[i][j] = '2'           # mark this point has been visted.
            if i-1 >= 0 and self.grid[i-1][j] == '1':
                queue.append((i-1, j))
                self.grid[i-1][j] = '2'     #@ avoiding adding this point to queue again.
            if i+1 < self.rows and self.grid[i+1][j] == '1':
                queue.append((i+1, j))
                self.grid[i+1][j] = '2'
            if j-1 >= 0 and self.grid[i][j-1] == '1':
                queue.append((i, j-1))
                self.grid[i][j-1] = '2'
            if j+1 < self.cols and self.grid[i][j+1] == '1':
                queue.append((i, j+1))
                self.grid[i][j+1] = '2'


def main():
    s = Solution()
    grid = ['11110',
            '11010',
            '11000',
            '00000']
    print s.numIslands(grid)
    grid2 = ['11000',
             '11000',
             '00100',
             '00011']
    print s.numIslands(grid2)

if __name__ == '__main__':
    main()
