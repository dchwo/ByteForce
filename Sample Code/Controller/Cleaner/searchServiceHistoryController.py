from csit314.entity.serviceHistory import ServiceHistory

class SearchServiceHistoryController:
    def __init__(self):
        self.entity = ServiceHistory()
    
    def searchCleanerServiceHistory(self, cleaner_id, service_type=None, start_date=None, end_date=None):
        return self.entity.get_cleaner_history(cleaner_id, service_type, start_date, end_date)