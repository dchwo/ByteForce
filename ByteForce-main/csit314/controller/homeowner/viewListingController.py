from csit314.entity.cleanerListing import CleanerListing

class ViewListingController:
    def __init__(self):
        self.cleanerListing = CleanerListing()

    # viewListingController
    def viewListing(self, listing_id):
        return self.cleanerListing.get_service_listing_detail(listing_id)
