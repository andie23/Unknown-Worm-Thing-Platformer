import pose_playback

def transform(player, location_point, animation, cutoff_frame):
     player.lock()
     rig = player.get_rig()
     rig.removeParent()
     rig.worldPosition = location_point.worldPosition
     
     pose_playback.OnAnimationFrameChange(rig, animation).attach(
        'on_%s_%s__platforming_action' % (str(rig), animation), 
         lambda r, a, frame, isplayin, interrupts: (
           __on_move(
                player, 
                frame, 
                isplayin, 
                interrupts,
                cutoff_frame
            )    
        )
     )
     pose_playback.PosePlayback(rig, animation).play()

def __on_move(player, frame, isplayin, interrupts, cutoff_frame):
    frame = round(frame)
    if (interrupts >= 1 and frame >= cutoff_frame or
         frame >= 1 and not isplayin):
        player.get_rig().stopAction(0)
        player.reset_collider_pos()
        player.get_rig().setParent(player.own)
        player.unlock()