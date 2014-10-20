import numpy as np
__author__ = 'archlyx'

if __name__ == "__main__":
   # p = [0.04, 0.06, 0.08, 0.02, 0.10, 0.12, 0.14]
   # q = [0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05, 0.05]

    p = [0.14, 0.02, 0.12, 0.04, 0.06, 0.08, 0.10]
    q = [0.04, 0.08, 0.09, 0.03, 0.04, 0.06, 0.01, 0.09]

    n = len(p)

    # Extra row since len(q) is larger than len(p)
    w = [[0] * (n + 1) for i in range(0, n + 2)]
    e = [[0] * (n + 1) for i in range(0, n + 2)]
    root = [[0] * (n + 1) for i in range(0, n + 2)]

    for i in range(1, n + 2):
        e[i][i - 1] = q[i - 1]
        w[i][i - 1] = q[i - 1]

    for l in range(1, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            w[i][j] = w[i][j - 1] + p[j - 1] + q[j]
            e[i][j] = 1000
            for r in range(i, j + 1):
                t = e[i][r - 1] + e[r + 1][j] + w[i][j]
                if t < e[i][j]:
                    e[i][j] = t
                    root[i][j] = r

    print(np.array(w).T)
    print(np.array(e).T)
    print(np.array(root).T)
