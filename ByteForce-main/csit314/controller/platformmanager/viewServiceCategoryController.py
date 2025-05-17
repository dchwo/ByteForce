from csit314.entity.serviceCategory import ServiceCategory

class ViewServiceCategoryController:
    def __init__(self):
        self.entity = ServiceCategory()
    
    def getAllCategories(self):
        return self.entity.get_all_categories()
    
    def getCategory(self, category_id):
        return self.entity.get_category(category_id)