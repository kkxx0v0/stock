import pymysql
import yaml
from sqlalchemy import create_engine
from db_table_struct import *

with open('../config.yaml', 'r') as file:
    config = yaml.safe_load(file)

engine = create_engine(
    f"mysql+pymysql://{config['mysql']['user']}:{config['mysql']['password']}@{config['mysql']['host']}/{config['mysql']['database']}")


def create_database(database_name):
    """
    创建数据库。
    :param database_name: 数据库名称
    """
    connection = pymysql.connect(
        host=config['mysql']['host'],
        user=config['mysql']['user'],
        password=config['mysql']['password'],
    )
    try:
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        connection.close()


def create_table():
    """
    创建一个数据库表
    :param table_name: 表的名称
    :param columns: 列的定义，格式为 [('列名', 数据类型, 是否主键, 是否允许为空, 注释)]
    """
    metadata.create_all(engine)
    print(f"所有表已创建！")


if __name__ == "__main__":
    create_database(config['mysql']['database'])
