from csit314.entity.cleanerListing import CleanerListing

class ViewCleanerListingController:
    def __init__(self):
        self.entity = CleanerListing()

    # viewCleanerListingController
    def getCleanerListing(self, service_id, user_id):
        return self.entity.get(service_id, user_id)        
