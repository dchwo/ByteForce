from csit314.entity.userAccount import UserAccount

class SuspendUserAccountController:
    def __init__(self):
        self.entity = UserAccount()

    def SuspendUserAccount(self, id):
        return self.entity.suspendUser(id)
