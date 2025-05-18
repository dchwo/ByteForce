from csit314.entity.cleanerListing import CleanerListing
from csit314.entity.serviceCategory import ServiceCategory

class CreateCleanerListingController:
    def __init__(self):
        self.entity = CleanerListing()
        self.category_entity = ServiceCategory()

    def getAllCategories(self):
        """Get all active categories for selection"""
        return self.category_entity.get_active_categories()
        
    def createCleanerListing(self, user_id, name, price, type, description, category_id=None):
        self.entity.add(user_id, name, price, type, description, category_id)
