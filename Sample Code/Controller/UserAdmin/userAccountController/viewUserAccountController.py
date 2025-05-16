from csit314.entity.userAccount import UserAccount

class ViewUserAccountController:
    def __init__(self):
        self.entity = UserAccount()

    def ViewUserAccount(self, id):
        return self.entity.getUserDetails(self, id)
