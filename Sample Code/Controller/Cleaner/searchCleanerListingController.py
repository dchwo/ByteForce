from csit314.entity.cleanerListing import CleanerListing

class SearchCleanerListingController:
    def __init__(self):
        self.entity = CleanerListing()

    # searchCleanerListingController
    def searchCleanerListing(self, user_id, query=None):
        return self.entity.get_by_user(user_id, query)

