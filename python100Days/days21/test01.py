import random

if __name__ == '__main__':
    # 摇骰子
    counters=[0]*6
    print(counters)
    for k,v in range(6000):
        face = random.randrange(1,7)
        counters[face-1]+=1
        #输出每种点数出现的次数
    for face in range(1,7):
        print(f'{face}点出现了{counters[face-1]}次')