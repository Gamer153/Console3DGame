from player import Player
from time import sleep
from world import World
from vectors import Vector2
from camera import Camera
from kbhit import KBHit
from display import Display
import threading


class Game:
    _camera: Camera = None
    _world: World = None
    _player: Player = None
    _call_after_blanking = None # type: function[Camera]

    def __init__(self, camera, world, player, call_after_blanking = None) -> None:
        self._camera = camera
        self._world = world
        self._player = player
        self._call_after_blanking = call_after_blanking

    def start(self):
        self._camera.display.render()
        thread = threading.Thread(target=self.register_input)
        thread.start()
        while thread.is_alive():
            try:
                sleep(0.1)
            except:
                pass

    def render(self):
        self._camera.display.clear()
        self._call_after_blanking(self._camera)
        for obj in self._world.objects:
            obj.render(self._camera)
        self._camera.display.render()

    def register_input(self):
        kb = KBHit()
        while True:
            if kb.kbhit():
                c = kb.getch()
                # self._camera.display.clear(Vector2(), Vector2(0, 3))
                # self._camera.display.add_text(Vector2(), str(ord(c)), True)
                if ord(c) == 27: # ESC
                    break
                # self._camera.display.set_pixel(Vector2(), c)
                if c == "w":
                    self._player.walk(Vector2(1, 0))
                elif c == "s":
                    self._player.walk(Vector2(-1, 0))
                elif c == "a":
                    self._player.walk(Vector2(0, -1))
                elif c == "d":
                    self._player.walk(Vector2(0, 1))
                self.render()
        kb.set_normal_term()