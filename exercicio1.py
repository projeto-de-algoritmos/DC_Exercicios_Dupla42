class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False

        rows, cols = len(matrix), len(matrix[0])
        i, j = 0, cols - 1

        while i < rows and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1

        return False


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5

solution = Solution()
result = solution.searchMatrix(matrix, target)

print(result)

