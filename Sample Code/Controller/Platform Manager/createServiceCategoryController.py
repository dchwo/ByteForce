from csit314.entity.serviceCategory import ServiceCategory

class CreateServiceCategoryController:
    def __init__(self):
        self.entity = ServiceCategory()
    
    def createServiceCategory(self, name, description, min_price=None, max_price=None):
        return self.entity.create_category(name, description, min_price, max_price)