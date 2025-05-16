from csit314.entity.UserProfile import UserProfile

class SuspendUserProfileController:
    def __init__(self):
        self.entity = UserProfile()

    def SuspendUserProfile(self, id):
        return self.entity.suspend(id)
