from csit314.entity.serviceHistory import ServiceHistory
from csit314.entity.cleanerListing import CleanerListing

class BookServiceController:
    def __init__(self):
        self.service_history = ServiceHistory()
        self.cleaner_listing = CleanerListing()
    
    def getServiceDetail(self, listing_id):
        """Get service details for booking form"""
        return self.cleaner_listing.get_service_listing_detail(listing_id)
    
    def createBooking(self, listing_id, cleaner_id, homeowner_id, service_date, notes=None):
        """Create a new service booking"""
        service = self.cleaner_listing.get_service_listing_detail(listing_id)
        if not service:
            return False
            
        return self.service_history.create_booking(
            cleaner_id=cleaner_id,
            homeowner_id=homeowner_id,
            service_listing_id=listing_id,
            service_type=service['type'],
            service_date=service_date,
            price=service['price'],
            notes=notes
        )
