###这里使用python 特性实现
import  numpy as np
# f(x)= x^3-2x +1
a= np.array([1,0,-2,1])
f=np.poly1d(a)
print(type(f))
print('传入值得到的具体结果',f([1,2,3,4]))
