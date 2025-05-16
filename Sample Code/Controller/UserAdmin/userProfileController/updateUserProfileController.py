from csit314.entity.userProfile import UserProfile

class UpdateUserProfileController:
    def __init__(self):
        self.entity = UserProfile()

    def UpdateUserProfile(self, id):
        return self.entity.update(id)
