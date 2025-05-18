from csit314.entity.userProfile import UserProfile

class UpdateUserProfileController:
    def __init__(self):
        self.entity = UserProfile()

    def UpdateUserProfile(self, id, bio, avatar):
        return self.entity.update_profile(id, bio, avatar)
