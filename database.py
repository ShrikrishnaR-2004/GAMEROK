from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://root:password@localhost/gamelist?charset=utf8mb4")

def load_games_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from games"))
        games = []
        for row in result.all():
            games.append(row._asdict())
        return games

def getresult(search):
    with engine.connect() as conn:
        result = conn.execute(text("select * from games where Game_Name like 'Overwatch'"))

        rows = result.all()
        if len(rows)==0:
            return None
        else:
            return rows[0]._asdict()