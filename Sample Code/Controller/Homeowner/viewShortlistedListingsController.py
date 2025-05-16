from csit314.entity.homeownerShortlist import HomeownerShortlist

class ViewShortlistedListingsController:
    def __init__(self):
        self.homeownerShortlist = HomeownerShortlist()
    
    def getShortlistedListings(self, user_id):
        """Get all shortlisted listings for a homeowner"""
        return self.homeownerShortlist.get_shortlisted_listings(user_id)
