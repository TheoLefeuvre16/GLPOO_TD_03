from controller import users_controller


class UsersView:

    def __init__(self, database_session):
        self._database_session = database_session

    def get(self, id):
        wanted_user = users_controller.UsersController(self._database_session)
        wanted_user.get(id)
        return wanted_user
