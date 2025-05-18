from csit314.entity.userProfile import UserProfile

class CreateUserProfileController: 
    def __init__(self):
        self.entity = UserProfile()

    def createUserProfile(self, user_id, role, description):
        return self.entity.add(user_id, role, description)
