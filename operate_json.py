import json


def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


# 保存 JSON 文件
def save_json(filename, data, is_data_changed):
    if is_data_changed:
        while True:
            user_input = input("数据已更改，是否确认保存？ (y/n): ").strip().lower()
            if user_input in ['y', 'n']:
                if user_input == 'y':
                    with open(filename, 'w', encoding='utf-8') as file:
                        json.dump(data, file, indent=4, ensure_ascii=False)
                break
            else:
                print("无效的输入，请输入 'y' 或 'n'。")
    else:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)