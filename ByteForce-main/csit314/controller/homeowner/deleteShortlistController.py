from csit314.entity.homeownerShortlist import HomeownerShortlist

class DeleteShortlistController:
    def __init__(self):
        self.homeownerShortlist = HomeownerShortlist()

    # deleteShortlistController    
    def deleteShortlist(self, user_id, listing_id):
        print(f"Controller - remove shortlist: user_id={user_id}, listing_id={listing_id}")
        self.homeownerShortlist.remove_shortlist(user_id, listing_id)

