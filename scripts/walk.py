import pose_playback
import actor

def right(cont):
    player = actor.Player(cont.owner)
    if player.own['Locked']:
        return
    
    if not player.is_facing_front():
        player.face_front()

    apply_movement(player)    

def left(cont):
    player = actor.Player(cont.owner)
    if player.own['Locked']:
        return

    if  player.is_facing_front():
        player.face_back()

    apply_movement(player)

def apply_movement(player):
    walk(player, 'Walking Action', 4, 0.6)

def walk(player, animation, trigger_frame, speed):
    if player.own['on_ground'] and not player.own['on_blocked']:
        rig = player.get_rig()
        pose_playback.OnAnimationFrameChange(rig, animation).attach(
           'on_%s_walk' % str(rig), 
            lambda o, a, frame, isplayin, i: (
                __on_walk(
                    player, 
                    frame, 
                    trigger_frame, 
                    speed
                )
            )
        )
        pose_playback.PosePlayback(
            player.get_rig(), 
            animation
        ).play()

def __on_walk(player, frame, trigger_frame, speed):
    if round(frame) == trigger_frame:    
        player.own.applyMovement(
            __get_transform(player, speed)
        )

def __get_transform(player, speed):
    move = 0
    if not player.is_facing_front():
        move -= speed
    else:
        move += speed
    return [0.0, move, 0.0]