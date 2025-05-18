from csit314.entity.userProfile import UserProfile

class SearchUserProfileController:
    def __init__(self):
        self.entity = UserProfile()
        
    def SearchUserProfile(self, id=None, role=None):
        return self.entity.search_profiles(id=id, role=role, first_name=None, last_name=None, email=None, status=None)
