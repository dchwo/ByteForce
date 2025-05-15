from csit314.entity.cleanerListing import CleanerListing

class UpdateCleanerListingController:
    def __init__(self):
        self.entity = CleanerListing()

    # updateCleanerListingController
    def updateCleanerListing(self, service_id, user_id, name, price, type, description):
        self.entity.update(service_id, user_id, name, price, type, description)

