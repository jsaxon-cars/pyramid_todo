from sqlalchemy import (
    Column,
    Integer,
    Text,
    Boolean,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class ToDo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    title = Column(Text, unique=True)
    completed = Column(Boolean, unique=False)

    def __init__(self, title, completed):
        self.title = title
        self.completed = completed

