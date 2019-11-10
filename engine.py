from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///tmp/test.db', echo=True)
Base.metadata.create_all(engine)

# https://docs.sqlalchemy.org/en/13/orm/tutorial.html
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    def __repr__(self):
        return '<User(first_name={self.first_name}, last_name={self.last_name})>'.format(self=self)

    def __str__(self):
        return 'User: {self.last_name}, {self.first_name}'.format(self=self)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
