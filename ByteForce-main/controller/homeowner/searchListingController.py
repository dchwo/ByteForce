from csit314.entity.cleanerListing import CleanerListing

class SearchListingController:
    def __init__(self):
        self.cleanerListing = CleanerListing()
       
    # searchListingController
    def searchListing(self, name, email, service_name, min_price, max_price, type):
        return self.cleanerListing.search_service_listings(name, email, service_name, min_price, max_price, type)
    
