from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    m = len(matrix)
    n = len(matrix[0])
    k = l = 0

    result = []
    while k < m and l < n:
        result.extend(matrix[k][l:n])
        k += 1

        n -= 1
        result.extend(matrix[i][n] for i in range(k, m))

        if k < m:
            m -= 1
            result.extend(reversed(matrix[m][l:n]))

        if l < n:
            result.extend(matrix[i][l] for i in range(m - 1, k - 1, -1))
            l += 1

    return result
