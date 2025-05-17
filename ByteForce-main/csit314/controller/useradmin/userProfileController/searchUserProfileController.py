from csit314.entity.userProfile import UserProfile

class SearchUserProfileController:
    def __init__(self):
        self.entity = UserProfile()

    def search_profiles(self, id, role):
        return self.entity.search_profiles(id, role)
