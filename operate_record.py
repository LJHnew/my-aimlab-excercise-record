from datetime import datetime


# 增加记录
def add_record(data, score, rating, react_time, target_number):
    now = datetime.now()
    year = str(now.year)
    month = '{:02d}'.format(now.month)
    day = '{:02d}'.format(now.day)
    hour_minute_second = now.strftime('%H:%M:%S')

    if year not in data['records']:
        data['records'][year] = {}
    if month not in data['records'][year]:
        data['records'][year][month] = {}
    if day not in data['records'][year][month]:
        data['records'][year][month][day] = {}

    data['records'][year][month][day][hour_minute_second] = {
        'score': score,
        'rating': rating,
        'react_time': react_time,
        'target_number': target_number
    }


# 修改记录
def modify_record(data, date, index, score, rating, react_time, target_number):
    year, month, day = date.split('-')
    if year in data['records'] and month in data['records'][year] and day in data['records'][year][month]:
        records = data['records'][year][month][day]
        if index in records:
            records[index] = {
                'score': score,
                'rating': rating,
                'react_time': react_time,
                'target_number': target_number
            }
        else:
            print("输入的序号无效")
    else:
        print("该日期没有记录")