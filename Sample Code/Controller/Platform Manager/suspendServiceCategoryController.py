from csit314.entity.serviceCategory import ServiceCategory

class SuspendServiceCategoryController:
    def __init__(self):
        self.entity = ServiceCategory()
    
    def suspendCategoryStatus(self, category_id):
        """Toggle category status and return whether it was suspended (True) or activated (False)"""
        return self.entity.suspend_category_status(category_id)