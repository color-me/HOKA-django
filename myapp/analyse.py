import pandas as pd
import matplotlib.pyplot as plt
import os

path = 'D:\\PycharmProjects\\first\\data\\name'
os.chdir(path)
# 修改读取文件的路径

years = range(1960, 2000)
pieces = []
columns = ['name', 'sex', 'births']
for year in years:
    path = 'yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)
# 批量读取文件

names = pd.concat(pieces, ignore_index=True)
# 将所有的内容放进一个dataframe

total_births = names.pivot_table('births', index='year', columns='sex', aggfunc='sum')
# 按性别和年份划分的出生总数

total_births.plot(title='全国网约车、专车司机出生年份与性别关系图')


def add_prop(group):
    group['prop'] = group.births / group.births.sum()
    return group


# 创建一个添加prop列，以计算每个名字按照年份、性别的占比
names = names.groupby(['year', 'sex']).apply(add_prop)

names.groupby(['year', 'sex']).prop.sum()


# 验证所有组的prop列总计为1

def get_top1000(group):
    return group.sort_values(by='births', ascending=False)[:1000]


# 创建一个筛选出生数前1000名

grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)
top1000.reset_index(inplace=True, drop=True)

boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']
# 将top1000里的男孩和女孩分开

top1000.query('year==2017 & sex=="M"')
# 查找2017年出生的top1000的男孩名

total_births = top1000.pivot_table('births', index='year', columns='name', aggfunc=sum)

subset = total_births[['Samantha', 'Haley', 'Rahul', 'Sonny']]
subset.plot(subplots=True, figsize=(12, 10), grid=False, title='Number of births per year')
plt.show()
