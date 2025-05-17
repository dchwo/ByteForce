from csit314.entity.cleanerListing import CleanerListing

class ViewListingViewsController:
    def __init__(self):
        self.entity = CleanerListing()

    def getListingViewsById(self, listing_id, user_id):
        """Get view stats for a specific listing"""
        return self.entity.get_listing_views_by_id(listing_id, user_id)
