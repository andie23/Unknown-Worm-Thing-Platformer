import bge
import component
import pose_playback

class AnimationBroadCast(component.Component):
    args = { 'Enabled' : True }

    def start(self, args):
        super().start(args)
    
    def update(self):
        super().update(self.broadcast_anim_to_listerners)
    
    def get_interruptions(self):
        return len(bge.logic.keyboard.active_events)

    def broadcast_anim_to_listerners(self):
        pose_playback.OnAnimationFrameChange(
            self.object, self.object.getActionName(0)
        ).onFrameChange(
            self.object.getActionFrame(0),
            self.object.isPlayingAction(0),
            self.get_interruptions()
        )