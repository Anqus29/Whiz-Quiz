import os
from terminaltexteffects.effects.effect_burn import Burn
from terminaltexteffects.effects.effect_expand import Expand

def intro():
    """
    Displays the intro animation using terminal text effects.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    
    effect = Burn(" █████╗      ██████╗ ██╗   ██╗██╗███████╗     ██████╗  █████╗ ███╗   ███╗███████╗\n██╔══██╗    ██╔═══██╗██║   ██║██║╚══███╔╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝\n███████║    ██║   ██║██║   ██║██║  ███╔╝     ██║  ███╗███████║██╔████╔██║█████╗  \n██╔══██║    ██║▄▄ ██║██║   ██║██║ ███╔╝      ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  \n██║  ██║    ╚██████╔╝╚██████╔╝██║███████╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗\n╚═╝  ╚═╝     ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝")
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)

    effect = Expand("██████╗ ██╗   ██╗     █████╗ ███╗   ██╗ ██████╗ ██╗   ██╗███████╗\n██╔══██╗╚██╗ ██╔╝    ██╔══██╗████╗  ██║██╔════╝ ██║   ██║██╔════╝\n██████╔╝ ╚████╔╝     ███████║██╔██╗ ██║██║  ███╗██║   ██║███████╗\n██╔══██╗  ╚██╔╝      ██╔══██║██║╚██╗██║██║   ██║██║   ██║╚════██║\n██████╔╝   ██║       ██║  ██║██║ ╚████║╚██████╔╝╚██████╔╝███████║\n╚═════╝    ╚═╝       ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝  ╚══════╝\n")                                                                 
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)