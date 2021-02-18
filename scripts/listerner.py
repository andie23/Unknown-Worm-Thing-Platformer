import bge
from collections import OrderedDict

class Listerner():
    def __init__(self, channel):
        self.channel = channel
        if 'listerners' not in bge.logic.globalDict:
            bge.logic.globalDict['listerners'] = {}        
        
        self._listerners = bge.logic.globalDict['listerners']
        
        if not self.is_channel_set():
            self.init_channel()
    
    def is_channel_set(self):
        return self.channel in self._listerners

    def is_id_set(self, id):
        return id in self.get_channel()

    def get_channel(self):
        return self._listerners[self.channel]
    
    def init_channel(self):
        self._listerners[self.channel] = OrderedDict()
     
    def add_listerner(self, id, listerner):
        self._listerners[self.channel][id] = listerner

    def remove_listerner(self, id):
        del self._listerners[self.channel][id]

    def remove_channel(self):
        del self._listerners[self.channel]
    
    def attach(self, id, listerner):
        if not self.is_id_set(id):
            self.add_listerner(id, listerner)

    def detach(self, id):
        if self.is_id_set(id): 
            self.remove_listerner(id)
        
    def get_listerners(self):
        return self.get_channel()

    def update_listerners(self, callback):
        listerners = self.get_channel()
        for id, listerner in listerners.items():
            callback(listerner)