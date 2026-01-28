

if __name__ == '__main__':
    print("你好")

# 列表元素反转
items = ['Python', 'Java', 'C++', 'Kotlin', 'Swift']
reverse_items = items.reverse()
print("反转后的列表",items)

# 列表生成
items_nums = []
for i in range(0,100):
    items= [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]

print(items)