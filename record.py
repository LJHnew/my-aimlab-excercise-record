from operate_json import *
from operate_record import *
from datetime import datetime
import matplotlib.pyplot as plt
import colorama


# 计算平均值
def calculate_average(data, option, year=None, month=None, day=None):
    if option == 0:
        total_score = 0
        total_rating = 0
        total_react_time = 0
        total_target_number = 0
        count = 0
        for year_data in data['records'].values():
            for month_data in year_data.values():
                for day_data in month_data.values():
                    for record in day_data.values():
                        total_score += record['score']
                        total_rating += float(record['rating'])
                        total_react_time += record['react_time']
                        total_target_number += record['target_number']
                        count += 1
        return (total_score / count, total_rating / count, total_react_time / count, total_target_number / count)
    elif option == 1:
        if year in data['records']:
            total_score = 0
            total_rating = 0
            total_react_time = 0
            total_target_number = 0
            count = 0
            for month_data in data['records'][year].values():
                for day_data in month_data.values():
                    for record in day_data.values():
                        total_score += record['score']
                        total_rating += float(record['rating'])
                        total_react_time += record['react_time']
                        total_target_number += record['target_number']
                        count += 1
            return (total_score / count, total_rating / count, total_react_time / count, total_target_number / count)
        else:
            return "该年份没有记录"
    elif option == 2:
        if year in data['records'] and month in data['records'][year]:
            total_score = 0
            total_rating = 0
            total_react_time = 0
            total_target_number = 0
            count = 0
            for day_data in data['records'][year][month].values():
                for record in day_data.values():
                    total_score += record['score']
                    total_rating += float(record['rating'])
                    total_react_time += record['react_time']
                    total_target_number += record['target_number']
                    count += 1
            return (total_score / count, total_rating / count, total_react_time / count, total_target_number / count)
        else:
            return "该月份没有记录"
    elif option == 3:
        if year in data['records'] and month in data['records'][year] and day in data['records'][year][month]:
            total_score = 0
            total_rating = 0
            total_react_time = 0
            total_target_number = 0
            count = 0
            for record in data['records'][year][month][day].values():
                total_score += record['score']
                total_rating += float(record['rating'])
                total_react_time += record['react_time']
                total_target_number += record['target_number']
                count += 1
            return (total_score / count, total_rating / count, total_react_time / count, total_target_number / count)
        else:
            return "该日期没有记录"
    elif option == 4:
        now = datetime.now()
        today = now.strftime('%Y-%m-%d')
        year, month, day = today.split('-')
        if year in data['records'] and month in data['records'][year] and day in data['records'][year][month]:
            total_score = 0
            total_rating = 0
            total_react_time = 0
            total_target_number = 0
            count = 0
            for record in data['records'][year][month][day].values():
                total_score += record['score']
                total_rating += float(record['rating'])
                total_react_time += record['react_time']
                total_target_number += record['target_number']
                count += 1
            return (total_score / count, total_rating / count, total_react_time / count, total_target_number / count)
        else:
            return "今天没有记录"


def main():
    filename = '六目标射击.json'
    data = load_json(filename)
    is_data_changed = False

    while True:
        print("\n操作选项：")
        print("1. 增加记录")
        print("2. 删除记录")
        print("3. 修改记录")
        print("4. 查找记录")
        print("5. 记录计算")
        print("6. 绘制折线图")
        print("0. 保存并退出")

        try:
            option = int(input("请输入操作选项："))
            if option < 0 or option > 6:
                raise ValueError
        except ValueError:
            print(colorama.Fore.RED + '==================')
            print('输入错误，请重新输入！')
            print('==================' + colorama.Fore.RESET)
            continue

        if option == 0:
            save_json(filename, data, is_data_changed)
            print("数据已保存，程序退出")
            break
        elif option == 1:
            obj = int(input("请输入分数："))
            rating = float(input("请输入命中率："))
            react_time = int(input("请输入反应时间："))
            target_number = int(input("请输入靶数："))
            add_record(data, obj, rating, react_time, target_number)
            is_data_changed = True
            print("记录已添加")
        elif option == 2:
            date = input("请输入要删除的日期（年-月-日）或者输入0表示今天：")
            if date == '0':
                now = datetime.now()
                year = now.strftime('%Y')
                month = now.strftime('%m')
                day = now.strftime('%d')
            else:
                year, month, day = date.split('-')
            if year in data['records'] and month in data['records'][year] and day in data['records'][year][month]:
                print("记录如下：")
                records = data['records'][year][month][day]
                for index, (time, record) in enumerate(records.items(), 1):
                    print(
                        f"{index}. {time} 得分：{record['score']} 命中率:{record['rating']} 反应时间：{record['react_time']} 命中目标：{record['target_number']}")
                index_to_delete = int(input("请输入要删除的记录序号："))
                if 1 <= index_to_delete <= len(records):
                    del data['records'][year][month][day][list(records.keys())[index_to_delete - 1]]
                    if not data['records'][year][month][day]:
                        del data['records'][year][month][day]
                        if not data['records'][year][month]:
                            del data['records'][year][month]
                            if not data['records'][year]:
                                del data['records'][year]
                                print("该年份所有记录已删除")
                            else:
                                print("该月份所有记录已删除")
                        else:
                            print("该日期所有记录已删除")
                    else:
                        print("记录已删除")
                else:
                    print("输入的序号无效")
                is_data_changed = True
            else:
                print("该日期没有记录")
        elif option == 3:
            date = input("请输入要修改的日期（年-月-日）：")
            year, month, day = date.split('-')
            if year in data['records'] and month in data['records'][year] and day in data['records'][year][month]:
                print("记录如下：")
                records = data['records'][year][month][day]
                for index, (time, record) in enumerate(records.items(), 1):
                    print(
                        f"{index}. {time} 得分：{record['score']} 命中率:{record['rating']} 反应时间：{record['react_time']} 命中目标：{record['target_number']}")
                index_to_modify = int(input("请输入要修改的记录序号："))
                if 1 <= index_to_modify <= len(records):
                    obj = int(input("请输入新的分数："))
                    rating = float(input("请输入新的命中率："))
                    react_time = int(input("请输入新的反应时间："))
                    target_number = int(input("请输入新的靶数："))
                    modify_record(data, date, list(records.keys())[index_to_modify - 1], obj, rating, react_time,
                                  target_number)
                    print("记录已修改")
                    is_data_changed = True
                else:
                    print("输入的序号无效")
            else:
                print("该日期没有记录")
        elif option == 4:
            search_option = int(input("请输入查找选项（0-年，1-年-月，2-年-月-日，3-今天）："))
            if search_option == 0:
                year = input("请输入年份：")
                if year in data['records']:
                    print(f"{year}年的所有记录如下：")
                    for month in sorted(data['records'][year].keys()):
                        for day in sorted(data['records'][year][month].keys()):
                            for time, record in data['records'][year][month][day].items():
                                print(
                                    f"{year}-{month}-{day} {time} 得分：{record['score']} 命中率：{record['rating']} 反应时间：{record['react_time']} 命中目标：{record['target_number']}")
                else:
                    print("该年份没有记录")
            elif search_option == 1:
                year_month = input("请输入年-月（例如：2024-03）：")
                year, month = year_month.split('-')
                if year in data['records'] and month in data['records'][year]:
                    print(f"{year_month}的所有记录如下：")
                    for day in sorted(data['records'][year][month].keys()):
                        for time, record in data['records'][year][month][day].items():
                            print(
                                f"{year}-{month}-{day} {time} 得分：{record['score']} 命中率：{record['rating']} 反应时间：{record['react_time']} 命中目标：{record['target_number']}")
                else:
                    print("该月份没有记录")
            elif search_option == 2:
                date = input("请输入年-月-日（例如：2024-03-18）：")
                year, month, day = date.split('-')
                if year in data['records'] and month in data['records'][year] and day in data['records'][year][month]:
                    print(f"{date}的所有记录如下：")
                    for time, record in data['records'][year][month][day].items():
                        print(
                            f"{year}-{month}-{day} {time} 得分：{record['score']} 命中率：{record['rating']} 反应时间：{record['react_time']} 命中目标：{record['target_number']}")
                else:
                    print("该日期没有记录")
            elif search_option == 3:
                now = datetime.now()
                today = now.strftime('%Y-%m-%d')
                year, month, day = today.split('-')
                if year in data['records'] and month in data['records'][year] and day in data['records'][year][month]:
                    print(f"今天的所有记录如下：")
                    for time, record in data['records'][year][month][day].items():
                        print(
                            f"{today} {time} 得分：{record['score']} 命中率：{record['rating']} 反应时间：{record['react_time']} 命中目标：{record['target_number']}")
                else:
                    print("今天没有记录")
        elif option == 5:
            calculate_option = int(input("请输入计算选项（0-全部，1-年，2-年-月，3-年-月-日，4-今天）："))
            if calculate_option == 0:
                print("全部最小基本记录平均值为：")
                average_score, average_rating, average_react_time, average_target_number = calculate_average(data, 0)
                print("得分：%.2f 命中率：%.2f%% 反应时间：%.2f 命中目标：%.2f" % (
                    average_score, average_rating * 100, average_react_time, average_target_number))
            elif calculate_option == 1:
                year = input("请输入年份：")
                print(f"{year}年最小基本记录平均值为：")
                average_score, average_rating, average_react_time, average_target_number = calculate_average(data, 1,
                                                                                                             year=year)
                print("得分：%.2f 命中率：%.2f%% 反应时间：%.2f 命中目标：%.2f" % (
                    average_score, average_rating * 100, average_react_time, average_target_number))
            elif calculate_option == 2:
                year_month = input("请输入年-月（例如：2024-03）：")
                year, month = year_month.split('-')
                print(f"{year_month}最小基本记录平均值为：")
                average_score, average_rating, average_react_time, average_target_number = calculate_average(data, 2,
                                                                                                             year=year,
                                                                                                             month=month)
                print("得分：%.2f 命中率：%.2f%% 反应时间：%.2f 命中目标：%.2f" % (
                    average_score, average_rating * 100, average_react_time, average_target_number))
            elif calculate_option == 3:
                date = input("请输入年-月-日（例如：2024-03-18）：")
                year, month, day = date.split('-')
                print(f"{date}最小基本记录平均值为：")
                average_score, average_rating, average_react_time, average_target_number = calculate_average(data, 3,
                                                                                                             year=year,
                                                                                                             month=month,
                                                                                                             day=day)
                print("得分：%.2f 命中率：%.2f%% 反应时间：%.2f 命中目标：%.2f" % (
                    average_score, average_rating * 100, average_react_time, average_target_number))
            elif calculate_option == 4:
                print("今天最小基本记录平均值为：")
                now = datetime.now()
                year = now.strftime('%Y')
                month = now.strftime('%m')
                day = now.strftime('%d')
                average_score, average_rating, average_react_time, average_target_number = calculate_average(data, 3,
                                                                                                             year=year,
                                                                                                             month=month,
                                                                                                             day=day)
                print("得分：%.2f 命中率：%.2f%% 反应时间：%.2f 命中目标：%.2f" % (
                    average_score, average_rating * 100, average_react_time, average_target_number))
        elif option == 6:
            sub_option = int(input("请输入绘制单位（0-得分，1-命中率，2-反应时间，3-命中目标）："))
            option2key = {
                0: ['score', '得分'],
                1: ['rating', '命中率'],
                2: ['react_time', '反应时间'],
                3: ['target_number', '命中目标'],
            }
            key_eng = option2key[sub_option][0]
            key_chi = option2key[sub_option][1]
            timestamps = []
            objs = []

            for year in sorted(data['records'].keys()):
                for month in sorted(data['records'][year].keys()):
                    for day in sorted(data['records'][year][month].keys()):
                        for time, time_data in data['records'][year][month][day].items():
                            timestamps.append(f'{year}-{month}-{day} {time}')
                            objs.append(time_data[key_eng])

            # 取最后50条记录
            timestamps_last_50 = timestamps[-50:]
            objs_last_50 = objs[-50:]
            average_obj = sum(objs_last_50) / len(objs_last_50)
            today = datetime.now().date()

            # 创建折线图
            plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为SimHei
            plt.plot(timestamps_last_50, objs_last_50, marker='o')
            for timestamp, obj in zip(timestamps_last_50, objs_last_50):
                datestamp = datetime.strptime(timestamp.split()[0], '%Y-%m-%d')
                if datestamp.date() == today:
                    plt.plot(timestamp, obj, marker='o', color='red')  # 如果是今天的记录，绘制红色点
                else:
                    plt.plot(timestamp, obj, marker='o', color='blue')  # 如果是以往的记录，绘制蓝色点
            plt.axhline(average_obj, color='r', linestyle='--', label=f'平均{key_chi}：{average_obj:.4f}')  # 添加平均值水平线
            plt.title(f'最近50场{key_chi}折线图')
            plt.xlabel('时间')
            plt.ylabel(f'{key_chi}')
            plt.xticks(rotation=45)
            plt.grid(True)
            plt.legend()  # 显示图例
            plt.tight_layout()

            for i, (timestamp, obj) in enumerate(zip(timestamps_last_50, objs_last_50)):
                plt.text(timestamp, obj, str(obj), ha='right', va='bottom', rotation=45, fontsize=8)

            plt.savefig(f'最近50场{key_chi}折线图.png')

            # 显示图
            plt.show()


if __name__ == "__main__":
    colorama.init()
    main()
