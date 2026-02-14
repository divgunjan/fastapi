from sqlmodel import SQLModel, Field, Column
import uuid
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
from typing import ClassVar
from typing import ClassVar


class User(SQLModel, table=True): 
    __tablename__: ClassVar['str'] = "users"
    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable = False,
            primary_key = True,
            default = uuid.uuid4
        )
    )
    username: str
    email:str
    first_name: str
    last_name: str
    password_hash:str = Field(exclude=True)
    is_verified: bool = False
    role:str=Field(sa_column=Column(pg.VARCHAR, nullable=False, server_default="user"))
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default =datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now)) 

'''class User:
        uid: uuid.UUID
        username:str
        email:str
        first_name:str
        last_name: str
        is_verified: bool = false
        created_at: datetime
        updated_at: datetime  
     
class Book(SQLModel, table=True):
    __tablename__:ClassVar['str'] = "books"
    uid: uuid.UUID = Field(
        sa_column = Column(
            pg.UUID, 
            nullable = False,
            primary_key = True,
            default = uuid.uuid4() #new uuid function creator
        ) 
    )
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default = datetime.now))
    update_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default = datetime.now))
    title: st   r
    author: str
'''

#migration environment

