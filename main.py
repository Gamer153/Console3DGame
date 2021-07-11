import importlib
import os
from time import sleep

import pip

from camera import Camera
from display import Display
from game import Game
from kbhit import KBHit
from object import Object
from player import Player
from vectors import Vector2, Vector3
from world import World


def install(module):
    try:
        importlib.import_module(module)
    except ModuleNotFoundError:
        pip.main(["install", module])
        importlib.import_module(module)

install("colorama")
install("numpy")

from colorama import Fore, Style

if __name__ == "__main__":
    # tsize = os.get_terminal_size()
    # print(Vector3(100, 23)[2])
    display = Display(100, 15, f"{Fore.CYAN}█{Style.RESET_ALL}")
    display.add_text(Vector2(40, 14), "Press ESC to exit")
    display.add_text(Vector2(10, 3), "vlant.de")
    display.set_pixel(Vector2(50, 5), f"{Fore.CYAN}█{Style.RESET_ALL}")
    display.set_pixel(Vector2(51, 5), f"{Fore.RED}█{Style.RESET_ALL}")
    display.set_pixel(Vector2(52, 5), f"{Fore.YELLOW}█{Style.RESET_ALL}")
    display.set_pixel(Vector2(53, 5), f"{Fore.GREEN}█{Style.RESET_ALL}")
    camera = Camera(display, 60)
    world = World()
    obj1 = Object(Vector3(100, 0, 20), block=f"{Fore.GREEN}█{Style.RESET_ALL}")
    obj2 = Object(Vector3(1, 100, 50), block=f"{Fore.RED}█{Style.RESET_ALL}")
    obj3 = Object(Vector3(100, 100, 100), block=f"{Fore.YELLOW}█{Style.RESET_ALL}")
    obj4 = Object(Vector3(3, 5, 1), block=f"{Fore.BLACK}█{Style.RESET_ALL}")
    world.add_objects(obj1, obj2, obj3, obj4)
    player = Player(camera, world)
    def ex_draw(cam: Camera):
        cam.display.add_text(Vector2(40, 14), "Press ESC to exit")
    game = Game(camera, world, player, ex_draw)
    game.render()
    game.start()
    # os.system("cls||clear")
