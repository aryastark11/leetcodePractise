# optimised solution
class Solution:
    def solve(self, matrix):
        result = []
        res = list(zip(*matrix))  # Interchanging rows and columns so that it is easy to sort
        for i in res:
            l = list(i)
            l.sort()
            result.append(l)
        return list(zip(*result))  # Interchanging the rows and columns back


##
class Solution:
    def solve(self, matrix):
        #col Elements --> [0,0], [1,0], [2,0]
        # print(matrix[0])
        # print(matrix[0][1])
        newMatrix = []

        cols = len(matrix[0])
        rows = len(matrix)

        for col in range(0, cols):
            aList = []
            for row in range(0, rows):
                aList.append(matrix[row][col])
            newMatrix.append(sorted(aList))
        print(newMatrix)
        transposeMatrix = []
        for row in range(0, rows):
            aList = []
            for col in range(0, cols):
                aList.append(newMatrix[col][row])
            transposeMatrix.append(aList)
        return transposeMatrix
