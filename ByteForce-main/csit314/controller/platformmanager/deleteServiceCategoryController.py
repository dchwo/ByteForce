from csit314.entity.serviceCategory import ServiceCategory

class DeleteServiceCategoryController:
    def __init__(self):
        self.entity = ServiceCategory()
    
    def deleteServiceCategory(self, category_id):
        self.entity.delete_category(category_id)