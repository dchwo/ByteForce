from csit314.entity.serviceCategory import ServiceCategory

class SearchServiceCategoryController:
    def __init__(self):
        self.entity = ServiceCategory()
    
    def searchServiceCategories(self, query=None, status=None):
        return self.entity.search_categories(query, status)