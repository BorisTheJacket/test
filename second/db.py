from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine


database_url = 'postgresql://admin:root@db:5432/admin'

print(database_url)

engine = create_engine(
    database_url,
    echo=True)


Base=declarative_base()


SessionLocal=sessionmaker(bind=engine)
