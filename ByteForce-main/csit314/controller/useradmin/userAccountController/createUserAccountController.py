from csit314.entity.userAccount import UserAccount

class CreateUserAccountController:
    def __init__(self):
        self.entity = UserAccount()

    def createUserAccount(self, role, first_name, last_name, email, password):
        return self.entity.addUser(role, first_name, last_name, email, password)
