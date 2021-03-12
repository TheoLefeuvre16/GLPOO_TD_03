from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
import bdd


class Users:
    def __init__(self, database_session):
        self._database_session = database_session

    def get(self, id):
        try:
            return self._database_session.query(bdd.User).filter_by(id=id).one()

        except NoResultFound:
            print("error")
