from csit314.entity.userProfile import UserProfile

class ViewUserProfileController:
    def ViewUserProfile(self, id):
        return self.entity.get_profile_by_user_id(id)

    def ViewAllProfiles(self):
        """Get all user profiles"""
        return self.entity.get_all_profiles()
