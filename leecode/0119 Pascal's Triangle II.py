class Solution(object):
    def getRow(self,rowIndex : int):
        row=[1]*(rowIndex+1)
        for i in range(1,rowIndex):
            for j in range(i):
                row[i-j]+=row[i-j-1]
        print(row)
        return row
if __name__ == '__main__':
    sl=Solution()
    sl.getRow(5)



