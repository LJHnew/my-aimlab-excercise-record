写一个python文件，它可以实现操作六目标射击.json的功能：
json分为三部分：第一部分是records部分，records中包括year，month，day部分，
year是一个数字，记录年份，month是一个数字，记录月份，day是一个字典，它的键是一个数字，表示第几天，值是一个字典，这里称为最小基本记录，
它的键是形如时：分：秒的字符串，值是一个字典，包括score,rating,react_time,target_number。records部分的年月日都是按照升序排列的。
操作一：增加记录
输入1表示增加记录，紧接着输入score,rating,react_time,target_number，程序能够根据当前时间添加记录，如果该记录对应的年、月、日不存在需要创建新的
输入2表示删除记录，输入年-月-日格式的字符串，程序识别出年月日后，输出对应日期的所有记录，格式为序号 时：分：秒 score rating react_time target_number，
用户输入序号，则删除序号对应的那一条记录，如果删除记录后那一天或者那一个月或者那一年没有记录，则需要把相应的day,month,year删除
输入3表示修改记录，输入年-月-日格式的字符串，程序识别出年月日后，输出对应日期的所有记录，格式为序号 时：分：秒 score rating react_time target_number，
用户输入序号 score new_rating new_react_time new_target_number，则修改序号对应的那一条记录的对应值。
输入4表示查找记录，
再输入年格式的字符串，程序输出对应年份的所有记录，格式为序号 年-月-日 时：分：秒 score rating react_time target_number，
再输入年-月格式的字符串，程序输出对应月份的所有记录，格式为序号 年-月-日 时：分：秒 score rating react_time target_number，
再输入年-月-日格式的字符串，程序输出对应日期的所有记录，格式为序号 年-月-日 时：分：秒 score rating react_time target_number，
输入5表示记录计算，
再输入0，输出全部最小基本记录score,rating,react_time,target_number的平均值，
再输入1，再输入年份，输出这一年最小基本记录score,rating,react_time,target_number的平均值，
再输入2，再输入年-月，输出这一个月最小基本记录score,rating,react_time,target_number的平均值，
再输入3，再输入年-月-日，输出这一天最小基本记录score,rating,react_time,target_number的平均值，
再输入4，输出现在这一天最小基本记录score,rating,react_time,target_number的平均值。
输入0表示结束操作，将当前修改后的json文件保存，程序结束