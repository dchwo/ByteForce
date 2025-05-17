from csit314.entity.userProfile import UserProfile

class CreateUserProfileController: 
    def __init__(self):
        self.entity = UserProfile()

    def createUserProfile(self, role, description):
        return self.entity.add(role, description)
