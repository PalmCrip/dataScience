import time
import  numpy as np

if __name__ == '__main__':
    py_lit = list(range(1000))
    np_arr = np.arange(10000000)
    start = time.time()
    np.sum(np_arr**2)
    print(f"NumPy数组耗时: {time.time()-start:.4f}s")