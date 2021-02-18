import actor
import platforming

def jump(cont):
    player = actor.Player(cont.owner)
    if player.own['Locked']:
        return

    if detect_platform(player):
        platforming.transform(
            player,
            player.get_platform_surface_empty(),
            'Zip Jump Action',
            22
        )
  
def detect_platform(player):      
    on_obstacle_clear = player.get_platform_probe_empty()['on_player_sight']
    on_platform = player.get_platform_probe_empty()['on_platform_surface']
    
    return True if on_obstacle_clear and on_platform else False