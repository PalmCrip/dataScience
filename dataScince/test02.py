
#数据容器

if __name__ == '__main__':

    # 列表及其方法
    #1.申请列表
    list1 =list()
    list2 = [0,1,2,3,4,5,6,7,8,9,10,
             11,12,13,14,15,16,17,18,19,20,
             21,22,23,24,25,26,27,28,29]

    ## 列表新增方法
    list1.append("dsc")
    list1.insert(1,"dsc01")
    print(list1)
    print(list2)

    ## 删除
    list1.pop(1)
    list2.remove(20)
    list1.clear()


