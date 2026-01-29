import random

from rich import Console
from rich.table import Table

# 创建控制台
console=Console()
# 创建表格并添加标题头
n=int(input('生成几注号码:'))
read_bull = [i for i in range(1,34)]
blue_ball  = [i for i in range(1,17)]
table = Table(show_header=True)
for col_name in ('序号','红球','蓝球'):
    table.add_column(col_name,justify='center')
for i in range(n):
    selected_balls = random.sample(read_bull,6)
    selected_balls.sort()
    blue_ball  =random.choice(blue_ball)
# 通过控制台输出表格
table.add_row(
    str(i+1),
    f'[red]{" ".join([f"{ball:0>2d}" for ball in selected_balls])}[/red]',
        f'[blue]{blue_ball:0>2d}[/blue]')