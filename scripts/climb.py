import actor
import platforming

def climb(cont):
    player = actor.Player(cont.owner)
    if player.own['Locked']:
        return

    if detect_ledge(player):
        player.own['on_blocked'] = False
        platforming.transform(
            player,
            player.get_ledge_empty(),
            'Climb Action',
            22
        )
       

def detect_ledge(player):
    is_blocked =  player.own['on_blocked']
    can_climb = player.get_ledge_empty()['on_ledge']
    return True if is_blocked and can_climb else False
