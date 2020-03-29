"""
 基数排序 基数排序的原理就是按照将每个元素的从低到高的顺序依次取出各位上的元素
 然后每次按照取出的元素进行归类和重整。直到所有的位数都排完。
 简单的将就是先拆分后整合。
 看到有一个非常好的答案， 在这里给出链接， 代码也参考该答案
 https://www.qingtingip.com/h_382475.html

"""


def js_sort(numbs):
    i=0
    max_num= max(numbs)
    # j为 最大值的位数
    j= len(str(max_num))

    while  i<j :
        #初始化 水桶的大小取决于元素的多少
        bucket_list=[[] for i in range(numbs.__len__())]
        for x in numbs:
            # 找到位置 然后添加
            bucket_list[int(x/(10**i)%10)].append(x)
        print(bucket_list)
        # 清空原来的数据 重新放置 第i轮排列好的数组
        numbs.clear()
        # 排列好后，然后按照队列的方式重新放入到队列中去
        for x in bucket_list:
            for y in x :
                numbs.append(y)

        i+=1

if __name__ == '__main__':
    a = [334, 5, 67, 345, 7, 345345, 99, 4, 23, 78, 45, 1, 3453, 23424]
    js_sort(a)
    print(a)


