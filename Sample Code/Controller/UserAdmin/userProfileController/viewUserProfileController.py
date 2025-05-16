from csit314.entity.userProfile import UserProfile

class ViewUserProfileController:
    def ViewUserProfile(self, id):
        return self.entity.getDetails(id)
