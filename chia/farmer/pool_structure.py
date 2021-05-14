import logging
log = logging.getLogger(__name__)
class pool_structure:
    def __init__(self,diff):
        self.harvesters:dict={}
        self.works={}
        self.pool_diff=diff
        self.log=log
    
class pool_harvester:
    def __init__(self):
        self.harvester_id=""
        self.plots={}

class pool_plot:
    def __init__(self):
        self.pk=None
        self.harvester_id=""
