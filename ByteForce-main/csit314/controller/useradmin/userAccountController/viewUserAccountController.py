from csit314.entity.userAccount import UserAccount

class ViewUserAccountController:
    def __init__(self):
        self.entity = UserAccount()  
        
    def ViewUserAccount(self, id):
        return self.entity.getUserDetails(id)

    def getAllUsers(self):
        """Get all users"""
        return self.entity.getAllUsers() 
