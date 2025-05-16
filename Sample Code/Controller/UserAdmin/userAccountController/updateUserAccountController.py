from csit314.entity.UserAccount import UserAccount

class UpdateUserAccountController:
    def __init__(self):
        self.entity = UserAccount()

    def UpdateUserAccount(self, id):
        return self.entity.updateUser(id)