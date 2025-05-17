from csit314.entity.serviceHistory import ServiceHistory

class ViewHomeownerHistoryController:
    def __init__(self):
        self.entity = ServiceHistory()
    
    def getHomeownerServiceHistory(self, homeowner_id, service_type=None, start_date=None, end_date=None):
        return self.entity.get_homeowner_history(homeowner_id, service_type, start_date, end_date)
    
    def getServiceHistoryDetail(self, history_id):
        return self.entity.get_history_detail(history_id)