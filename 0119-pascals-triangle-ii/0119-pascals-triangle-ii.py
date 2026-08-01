class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # ans = []
        # for i in range(rowIndex+1):
        #     row = [1] * (i + 1)
        #     for j in range(1, i):
        #         row[j] = ans[i - 1][j - 1] + ans[i - 1][j]
        #     ans.append(row)
        # return ans[-1]

        row = [1]
        for i in range(1, rowIndex + 1):
            row.append(1)
            for j in range(i - 1, 0, -1):
                row[j] = row[j] + row[j - 1]
        return row