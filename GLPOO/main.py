from bdd import *

from view import users_view



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    session.add(User(name='lol', fullname='mdr', nickname=' nique'))
    session.add(User( name= "adrim", fullname="fury", nickname="road"))

    session.commit()
    first_user = users_view.UsersView(session)
    session.close()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
