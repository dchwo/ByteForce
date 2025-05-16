from csit314.entity.userProfile import UserProfile

class CreateUserAccountController:
    def __init__(self):
        self.entity = UserProfile()

    def createUserProfile(self, role, descrpition):
        return self.entity.add(role, descrpition)
