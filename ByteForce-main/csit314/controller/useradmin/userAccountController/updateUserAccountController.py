from csit314.entity.userAccount import UserAccount

class UpdateUserAccountController:
    def __init__(self):
        self.entity = UserAccount()

    def UpdateUserAccount(self, id, role, first_name, last_name, email, password):
        return self.entity.updateUser(id, role, first_name, last_name, email, password)
