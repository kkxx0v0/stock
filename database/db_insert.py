from sqlalchemy import insert
from db_create import engine

def insert_data_into_table(table, data: list):
    """
    插入数据到表中。
    :param engine: SQLAlchemy 数据库引擎
    :param table: 表对象
    :param data: 要插入的数据列表，数据为字典形式
    """
    with engine.connect() as conn:
        insert_stmt = insert(table).values(data)
        conn.execute(insert_stmt)
    print(f"插入 {len(data)} 条记录到表 {table.name} 成功！")
