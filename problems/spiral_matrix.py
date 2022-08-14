from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    m = len(matrix)
    n = len(matrix[0])
    k = l = 0
    result = []
    while k < m and l < n:
        for i in range(l, n):
            result.append(matrix[k][i])
        k += 1
        for i in range(k, m):
            result.append(matrix[i][n - 1])
        n -= 1
        if k < m:
            for i in range(n - 1, l - 1, -1):
                result.append(matrix[m - 1][i])
            m -= 1
        if l < n:
            for i in range(m - 1, k - 1, -1):
                result.append(matrix[i][l])
            l += 1
    return result
