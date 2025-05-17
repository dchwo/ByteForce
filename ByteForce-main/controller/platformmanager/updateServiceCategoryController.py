from csit314.entity.serviceCategory import ServiceCategory

class UpdateServiceCategoryController:
    def __init__(self):
        self.entity = ServiceCategory()
    
    def updateServiceCategory(self, category_id, name, description, min_price=None, max_price=None):
        self.entity.update_category(category_id, name, description, min_price, max_price)