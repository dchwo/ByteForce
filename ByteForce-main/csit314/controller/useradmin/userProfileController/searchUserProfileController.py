from csit314.entity.userProfile import UserProfile

class SearchUserProfileController:
    def __init__(self):
        self.entity = UserProfile()
        
    def SearchUserProfile(self, id, status, uid, role, first_name, last_name, email):
        return self.entity.search_profiles(id=None, status=None, uid=None, role=None, first_name=None, last_name=None, email=None)
