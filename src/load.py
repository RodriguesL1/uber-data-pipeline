from sqlalchemy import create_engine

def load_data(df):
    engine = create_engine("postgresql://user:password@localhost:5432/uber_db")
    df.to_sql("corridas", engine, if_exists="replace", index=False)
