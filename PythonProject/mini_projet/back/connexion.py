from sqlalchemy import Table, MetaData, Integer,Column ,String, ForeignKey,create_engine , Enum
engine = create_engine('postgresql://postgres:12345@localhost:9999/restaurant_db')
metadata = MetaData()