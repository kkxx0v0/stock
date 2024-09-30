import json
import os
from database.db_insert import insert_data_into_table

DATA_FILE_PATH = './data/data.json'


def save_data_to_file(data=None, file_path=DATA_FILE_PATH):
    """
    将数据保存到指定的文件中。
    :param data: 要保存的数据，格式为列表字典，默认为空列表
    :param file_path: 文件路径，默认为 DATA_FILE_PATH
    """
    if data is None:
        data = []

    if not os.path.exists(os.path.dirname(file_path)):
        print(f"目录 '{os.path.dirname(file_path)}' 不存在！正在创建新的目录。")
        os.makedirs(os.path.dirname(file_path))

    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"数据已保存到文件 '{file_path}'！")
    except (json.JSONDecodeError, OSError) as e:
        print(f"写入文件时发生错误: {e}")


def load_data_from_file(table_name, file_path=DATA_FILE_PATH):
    """
    从文件中读取数据并插入到数据库
    :param file_path:
    :param table_name: 要插入的表名
    """
    if not os.path.exists(file_path):
        save_data_to_file()

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            insert_data_into_table(table_name, data)
    except (json.JSONDecodeError, OSError) as e:
        print(f"读取文件时发生错误: {e}")
