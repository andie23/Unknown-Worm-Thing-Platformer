import bge
import pose_playback

class Player():
    def __init__(self, obj):
        self.own = obj
    
    @property
    def orientation(self):
        return self.own['own_orientation']
    
    def lock(self):
        self.own['Locked'] = True

    def unlock(self):
        self.own['Locked'] = False

    def __get_obj(self, prop_name):
        return bge.logic.getCurrentScene().objects[
                self.own[prop_name]
        ]
   
    def get_rig(self):
        return self.__get_obj('rig')
    
    def get_rig_empty(self):
        return self.__get_obj('rig_empty')
    
    def get_ledge_empty(self):
        return self.__get_obj('ledge_empty')

    def get_platform_probe_empty(self):
        return self.__get_obj('platform_probe_empty')

    def get_platform_surface_empty(self):
        return self.__get_obj('platform_surface_empty')

    def reset_collider_pos(self):
        collider_empty = self.get_rig_empty()
        self.own.worldPosition = collider_empty.worldPosition
        
    def is_facing_front(self):
        return self.orientation == 'Front'
    
    def face_to(self, direction):
        pose_playback.PosePlayback(self.own, direction).play()

    def face_front(self):
        self.face_to('Rotate.L')
        self.set_orientation('Front')

    def face_back(self):
        self.face_to('Rotate.R')
        self.set_orientation('Back')
    
    def set_orientation(self, name):
        self.own['own_orientation'] = name