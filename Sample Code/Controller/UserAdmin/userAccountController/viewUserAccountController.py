from csit314.entity.userAccount import UserAccount

class ViewUserAccountController:
    def ViewUserAccount(self, id):
        return self.entity.getUserDetails(id)
