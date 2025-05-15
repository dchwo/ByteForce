from csit314.entity.cleanerListing import CleanerListing

class CreateCleanerListingController:
    def __init__(self):
        self.entity = CleanerListing()

    # createCleanerListingController
    def createCleanerListing(self, user_id, name, price, type, description):
        self.entity.add(user_id, name, price, type, description)
