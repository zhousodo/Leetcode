"""
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

"""
思路：
从 第三行开始出现规律， 第三行总共有四个元素， 第一个和最后一个都是一
    第二个元素是第二行的第一个元素+第二个元素，
    row[3][1]=1
    row[3][2]=row[2][1]+row[2][2]
    row[3][3]=row[2][2]+row[2][3]
    row[3][3]=1
    第四行的元素也是这样累积的，
    所以这个就是规律


"""
class Solution():
    def generate(self,numRows):
        if numRows==1:
            print('[1]')
            return [[1]]
        elif numRows==2:
            print("[1,1]")
            return [[1],[1,1]]
        elif numRows==0:
            return []
        else:
            rows=[[1],[1,1]]
            for i in  range(2,numRows):
                x=[]
                x.append(1)
                for j in range(1,i):
                    x.append(rows[i-1][j-1]+rows[i-1][j])

                x.append(1)
                rows.append(x)
        print(rows)
        return rows

if __name__ == '__main__':
    sl= Solution()
    sl.generate(1)


