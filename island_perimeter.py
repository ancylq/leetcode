# coding:utf-8
'''
You are given a map in form of a two-dimensional integer grid where 1 
represents land and 0 represents water. Grid cells are connected 
horizontally/vertically (not diagonally). The grid is completely 
surrounded by water, and there is exactly one island (i.e., one or more 
connected land cells). The island doesn't have "lakes" (water inside 
that isn't connected to the water around the island). One cell is a 
square with side length 1. The grid is rectangular, width and height 
don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
'''
class Solution(object):
    
    def __init__(self, grid):
        self.grid = grid
    
    def compareElement(self, x, y):
        if x<0 or x >=self.row_length:
            return 1
        if y<0 or y>=self.col_length:
            return 1
        if self.grid[x][y] != 1:
            return 1
        return 0
    
    def computePerimeter(self, x, y, element):
        '''计算值为1的元素边界，值相同的元素不为边界'''
        l = 0
        l += self.compareElement(x-1, y) # 上
        l += self.compareElement(x+1, y) # 下
        l += self.compareElement(x, y+1) # 右
        l += self.compareElement(x, y-1) # 左
        return l
    
    def islandPerimeter(self):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        l = 0
        self.row_length = len(self.grid)
        for x, row in enumerate(self.grid):
            self.col_length = len(row)
            for y, element in enumerate(row):
                if element == 1:
                    l += self.computePerimeter(x, y, element)
        return l
        
class SolutionBest(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h = len(grid)
        w = len(grid[0]) if h else 0
        ans = 0
        for x in range(h):
            for y in range(w):
                if grid[x][y] == 1:
                    ans += 4
                    if x > 0 and grid[x - 1][y]:
                        ans -= 2
                    if y > 0 and grid[x][y - 1]:
                        ans -= 2
        return ans
    
    
if __name__ == '__main__':
    grid = [[0,1,0,0],
            [1,1,1,0],
            [0,1,0,0],
            [1,1,0,0]]
    s = SolutionBest()
    print s.islandPerimeter(grid)