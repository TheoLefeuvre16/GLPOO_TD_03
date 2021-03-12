
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from controller import users_controller
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (

            self.name, self.fullname, self.nickname)


engine = create_engine('sqlite:///users.db', echo=True)
Base.metadata.create_all(bind=engine)  # creer le user.db !!!!!!!!!!!!!!!!!!!!!!!!
Session = sessionmaker(bind=engine)
session = Session()
