from sqlalchemy import create_engine,text

engine = create_engine("mysql+pymysql://root:password@localhost/gamelist?charset=utf8mb4")

with engine.connect() as conn:
    result = conn.execute(text("select * from games"))
    print(result.all())