from csit314.entity.userProfile import UserProfile

class SearchUserProfileController:
    def __init__(self):
        self.entity = UserProfile()

    def SearchUserProfile(self, id, role):
        return self.entity.searchProfile(id, role)
