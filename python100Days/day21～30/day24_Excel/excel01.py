import xlrd
from anyio import value

# 使用xlrd模块的open_workbook函数打开指定对象
wb =  xlrd.open_workbook('test.xls')
# 获取所有sheet
sheetName = wb.sheet_names()
print('sheet页',sheetName)
#获取指定的sheet对象(工作表)
sheet = wb.sheet_by_name(sheetName[0])
#获取行数和列数
print("行数"+sheet.nrows,"列数"+sheet.ncols)
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        value = sheet.cell(row,col).value
        # 对除首行外的其他行进行梳处理
        if row > 0:
            #将第一列的xldate类型转换为年月日的形式
            if col ==0:
                #xldate_as_tuple
                value = xlrd.xldate_as_tuple(value,0)
                value = f'{value[0]}年{value[1]:>02d}月{value[2]:>02d}日'
                # 其他列的number类型处理成小数点后保留两位有效数字的浮点数
            else:
                value = f'{value:.2f}'
            print(value,end='\t')
        print()
    #获取最后一个单元格的数据类型
    last_cell_type = sheet.cell_type(sheet.nrows-1,sheet.nrows-1,sheet.ncols-1)
    print(last_cell_type)
    # 获取第一行的值
    print(sheet.row_values(0))
    # 获取指定行指定列范围的数据（列表）
    # 第一个参数代表行索引，第二个和第三个参数代表列的开始（含）和结束（不含）索引
    print(sheet.row_slice(3,0,5))
