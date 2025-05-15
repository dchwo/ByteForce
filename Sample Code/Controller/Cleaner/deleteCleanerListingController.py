from csit314.entity.cleanerListing import CleanerListing

class DeleteCleanerListingController:
    def __init__(self):
        self.entity = CleanerListing()

    # deleteCleanerListingController
    def deleteCleanerListing(self, service_id, user_id):
        self.entity.delete(service_id, user_id)
