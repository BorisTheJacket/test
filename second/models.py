from db import Base
from sqlalchemy import String, Boolean, Integer, Column, Text


class NewUser(Base):
    __tablename__ = 'uid_user_table'
    id=Column('id',Text, primary_key=True)
    token=Column('token', Text)
    name=Column('name', String, nullable=False)

    def __repr__(self):
        return f'{self.id}'
    

class AudioFile(Base):
    __tablename__ = 'user_files'
    id=Column('id', Text, primary_key=True)
    uid=Column('uid', Text)
    file=Column('file', Text)
