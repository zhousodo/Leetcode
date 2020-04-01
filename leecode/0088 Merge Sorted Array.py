""":raise
假定num1 的空间能够容纳下nums2
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""
class Solution():
    # def merge(self,nums1,n1, nums2,n2):
    #     if len(nums1)>= n1+n2:## 确保有足够的空间容纳插入的元素
    #       # 插入几个元素
    #         #for i in range(n2-1):
    #         i=0
    #         if i <= n2-1:
    #         # 在何处插入
    #             for j in range(n1,n1+n2):
    #                 #nums1[j].append(nums2[i])
    #                 nums1[j]=nums2[i]
    #                 i+=1
    #
    #         print(nums1)
    #         return sorted(nums1)
    #     else:
    #         print('error')
    #         return

    def merge(self,nums1,m, nums2,n):
        res= nums1[:m]
        nums1.clear()
        nums1.extend(res)
        nums1.extend(nums2[:n])
        x=sorted(nums1)
        return x

if __name__ == '__main__':
    nums1= [1,2,3,0,0,0,0]
    nums2=[2,5,6,7]
    m=3
    n=4
    s=Solution()
    x=s.merge(nums1,m,nums2,n)
    print(x)





