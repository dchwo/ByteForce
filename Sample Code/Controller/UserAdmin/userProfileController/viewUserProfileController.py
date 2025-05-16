from csit314.entity.UserProfile import UserProfile

class ViewUserProfileController:
    def __init__(self):
        self.entity = UserProfile()

    def ViewUserProfile(self, id):
        return self.entity.getDetails(self, id)