import symbol
import time
from symbol import try_stmt

def welcome():
    print('欢迎来到现实世界')
import  numpy as np

if __name__ == '__main__':
    py_lit = list(range(1000))
    np_arr = np.arange(10000000)
    start = time.time()
    np.sum(np_arr**2)
    print(f"NumPy数组耗时: {time.time()-start:.4f}s")
    # name = input("你的名字：" )
    # age = input("你的年龄：")
    # print('你的年龄%s,你的姓名%s' % (age,name))
    # print(type(np_arr))
    welcome()

    arr = {0,1,2,3,4,5,6,7,8,9}
    arr.add(1)
    for e in  range(0,20):
        print(e)

    list = list()
    for e in range(0,20):
        list.append(e)

    print(list)
