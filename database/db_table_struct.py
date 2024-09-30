from sqlalchemy import MetaData, Table, Column, String, Date, DECIMAL

metadata = MetaData()

stock_basic_table = Table(
    'stock_basic', metadata,
    Column('st_code', String(20), primary_key=True, nullable=False, comment='股票代码'),
    Column('st_name', String(100), nullable=False, comment='股票名称'),
    Column('industry', String(100), nullable=True, comment='所处行业'),
    Column('bk_code', String(50), nullable=True, comment='板块编号')
)

index_table = Table(
    'index', metadata,
    Column('index_code', String(15), primary_key=True, nullable=False, comment='指数代码'),
    Column('date', Date, primary_key=True, nullable=False, comment='日期'),
    Column('open_price', DECIMAL(8, 2), nullable=True, comment='开盘'),
    Column('high', DECIMAL(8, 2), nullable=True, comment='最高'),
    Column('low', DECIMAL(8, 2), nullable=True, comment='最低'),
    Column('latest', DECIMAL(8, 2), nullable=True, comment='最新价')
)

stock_table = Table(
    'stock', metadata,
    Column('st_code', String(5), primary_key=True, nullable=False, comment='股票代码'),
    Column('date', Date, primary_key=True, nullable=False, comment='日期'),
    Column('open_price', DECIMAL(8, 2), nullable=True, comment='开盘'),
    Column('close_price', DECIMAL(8, 2), nullable=True, comment='收盘'),
    Column('high', DECIMAL(8, 2), nullable=True, comment='最高'),
    Column('low', DECIMAL(8, 2), nullable=True, comment='最低'),
    Column('vol', DECIMAL(15, 1), nullable=True, comment='成交量'),
    Column('amount', DECIMAL(18, 1), nullable=True, comment='成交额'),
    Column('amplitude', DECIMAL(8, 2), nullable=True, comment='振幅'),
    Column('chg_per', DECIMAL(10, 2), nullable=True, comment='涨跌幅'),
    Column('chg_amount', DECIMAL(10, 2), nullable=True, comment='涨跌额'),
    Column('turnover', DECIMAL(8, 2), nullable=True, comment='换手率')
)
