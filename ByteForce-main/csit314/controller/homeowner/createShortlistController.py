from csit314.entity.homeownerShortlist import HomeownerShortlist
from csit314.entity.cleanerListing import CleanerListing

class CreateShortlistController:
    def __init__(self):
        self.homeownerShortlist = HomeownerShortlist()
        self.cleanerListing = CleanerListing()

    # createShortlistController
    def createShortlist(self, user_id, listing_id):
        print(f"Controller - add shortlist: user_id={user_id}, listing_id={listing_id}")
        self.cleanerListing.increment_shortlisted(listing_id)
        self.homeownerShortlist.add_shortlist(user_id, listing_id)        
    

