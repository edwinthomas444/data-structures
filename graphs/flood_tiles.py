'''An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
'''

class Solution(object):
    def isvalid(self, rows, cols, i, j):
        if i<rows and j<cols and i>=0 and j>=0:
            return True
        return False
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        rows = len(image)
        columns = len(image[0])

        visited = []
        for i in range(rows):
            row = []
            for j in range(columns):
                row.append(False)
            visited.append(row)

        
        queue = []
        queue.append((sr, sc))
        start_color = image[sr][sc]
        
        while queue:
            row, col = queue.pop(0)
            visited[row][col] = True
            # update the color
            image[row][col] = color

            # all four directions
            four_dirs = [(row+1, col), (row, col+1), (row-1, col), (row, col-1)]
            for n_hop in four_dirs:
                valid = self.isvalid(rows, columns, n_hop[0], n_hop[1])
                
                if valid and (not visited[n_hop[0]][n_hop[1]]) and start_color==image[n_hop[0]][n_hop[1]]:
                    queue.append(n_hop)
                    
        return image