from csit314.entity.cleanerListing import CleanerListing

class ViewListingShortlistsController:
    def __init__(self):
        self.entity = CleanerListing()
  
    def getListingShortlistsById(self, listing_id, user_id):
        """Get shortlist stats for a specific listing"""
        return self.entity.get_listing_shortlists_by_id(listing_id, user_id)
    
