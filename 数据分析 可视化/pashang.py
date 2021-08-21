import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')     # 设置图片显示的主题样式

# 解决matplotlib显示中文问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

dataset_path = './dataset/Mountains.csv'   # 这个没有


def preview_data(data):
    """
        数据预览
    """
    # 数据预览
    print(data.head())

    # 数据信息
    print(data.info())


def proc_success(val):
    """
        处理 'Ascents bef. 2004' 列中的数据
    """
    if '>' in str(val):
        return 200
    elif 'Many' in str(val):
        return 160
    else:
        return val


def run_main():
    """
        主函数
    """
    data = pd.read_csv(dataset_path)

    preview_data(data)

    # 数据重构
    # 重命名列名
    data.rename(columns={'Height (m)': 'Height', 'Ascents bef. 2004': 'Success',
                         'Failed attempts bef. 2004': 'Failed'}, inplace=True)

    # 数据清洗
    data['Failed'] = data['Failed'].fillna(0).astype(int)  #空值补零并转换为int
    data['Success'] = data['Success'].apply(proc_success)  #给原始数据中的非数字值设置成指定数字
    data['Success'] = data['Success'].fillna(0).astype(int)  #空值补零并转换为int
    data = data[data['First ascent'] != 'unclimbed']  #过滤未登顶的数据
    data['First ascent'] = data['First ascent'].astype(int)  #转换类型

    # 可视化数据
    # 1. 登顶次数 vs 年份

    plt.hist(data['First ascent'].astype(int), bins=20)
    plt.ylabel('高峰数量')
    plt.xlabel('年份')
    plt.title('登顶次数')
    plt.savefig('./first_ascent_vs_year.png')
    plt.show()

    # 2. 高峰vs海拔
    data['Height'].plot.hist(color='steelblue', bins=20)
    plt.bar(data['Height'],
            (data['Height'] - data['Height'].min()) / (data['Height'].max() - data['Height'].min()) * 23,   # 按比例缩放
            color='red',
            width=30, alpha=0.2)
    plt.ylabel('高峰数量')
    plt.xlabel('海拔')
    plt.text(8750, 20, "海拔", color='red')
    plt.title('高峰vs海拔')
    plt.savefig('./mountain_vs_height.png')
    plt.show()

    # 3. 首次登顶
    data['Attempts'] = data['Failed'] + data['Success']  # 攀登尝试次数
    fig = plt.figure(figsize=(13, 7))
    fig.add_subplot(211)
    plt.scatter(data['First ascent'], data['Height'], c=data['Attempts'], alpha=0.8, s=50)
    plt.ylabel('海拔')
    plt.xlabel('登顶')

    fig.add_subplot(212)
    plt.scatter(data['First ascent'], data['Rank'].max() - data['Rank'], c=data['Attempts'], alpha=0.8, s=50)
    plt.ylabel('排名')
    plt.xlabel('登顶')
    plt.savefig('./mountain_vs_attempts.png')
    plt.show()


if __name__ == '__main__':
    run_main()
