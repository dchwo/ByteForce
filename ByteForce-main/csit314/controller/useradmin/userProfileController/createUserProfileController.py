from csit314.entity.userProfile import UserProfile

class CreateUserAccountController:
    def __init__(self):
        self.entity = UserProfile()

    def createUserProfile(self, bio, avatar, status):
        return self.entity.add(bio, avatar, status)
