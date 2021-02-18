import bge
import listerner
import pose_lib

class PosePlayback():
    def __init__(self, rig, action):
        action_dict = pose_lib.LIB[action]
        self.rig = rig
        self.action = action_dict['action']
        self.fstart = action_dict['fstart']
        self.fstop = action_dict['fstop']
        self.blendin = action_dict['blending']
    
    def play(self):
        self.pose(bge.logic.KX_ACTION_MODE_PLAY)
    
    def playLoop(self):
        self.pose(bge.logic.KX_ACTION_MODE_LOOP)
    
    def pose(self, mode):
        self.rig.playAction(
            self.action, 
            start_frame=self.fstart, 
            end_frame=self.fstop,
            play_mode=mode,
            blendin=self.blendin
        )
        
class OnAnimationFrameChange(listerner.Listerner):
    def __init__(self, playing_object, action_name):
        channel = 'anim_for_%s_%s' % (str(playing_object), action_name)
        super(OnAnimationFrameChange, self).__init__(channel)
        self.obj = playing_object
        self.action_name = action_name

    def onFrameChange(self, frame, is_playing, interruptions):
        self.update_listerners(
            lambda listerner: listerner(
               self.obj, 
               self.action_name, 
               frame, 
               is_playing,
               interruptions
            )
        )
