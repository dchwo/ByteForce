from csit314.entity.homeownerShortlist import HomeownerShortlist

class SearchShortlistController:
    def __init__(self):
        self.homeownerShortlist = HomeownerShortlist()

    # searchShortlistController
    def isShortlisted(self, user_id, listing_id):
        print(f"Controller - Checking shortlist: user_id={user_id}, listing_id={listing_id}")
        return self.homeownerShortlist.is_shortlisted(user_id, listing_id)

    def searchShortlist(self, user_id):
        return self.homeownerShortlist.get_shortlisted_ids(user_id)    


