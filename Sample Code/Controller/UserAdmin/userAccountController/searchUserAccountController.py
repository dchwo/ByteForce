from csit314.entity.UserAccount import UserAccount

class SearchUserAccountController:
    def __init__(self):
        self.entity = UserAccount()

    def SearchUserAccount(self, id, first_name, last_name, email, role):
        return self.entity.searchUser(id, first_name, last_name, email, role)