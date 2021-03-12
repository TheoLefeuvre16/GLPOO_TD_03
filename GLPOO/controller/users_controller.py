from model import users_model


class UsersController:

    def __init__(self, database_session):
        self._database_session = database_session

    def get(self, id):
        searched_user = users_model.Users(self._database_session).get(id)
        return searched_user
