import os
from time import sleep
from vectors import Vector2

class Display:
    _pixels = list()
    columns = 0
    lines = 0
    background = " "

    def __init__(self, width: int, height: int, background: str = " "):
        self.columns = width
        self.lines = height
        self.background = background
        self._pixels.clear()
        for i in range(height):
            self._pixels.insert(i, list())
            for j in range(width):
                self._pixels[i].insert(j, background)
    
    def render(self):
        os.system('cls||clear')
        for pixelrow in self._pixels:
            for pixel in pixelrow:
                pixel: str
                if pixel.strip() == "":
                    print(" ", end="")
                else:
                    print(pixel.strip(), end="")
            print()

    def set_pixel(self, vector2, symbol, rerender: bool = False) -> bool:
        try:
            if type(symbol) is str:
                # print(vector2, symbol)
                self._pixels[round(vector2[1])][round(vector2[0])] = symbol
                if rerender:
                    self.render()
                return True
            else:
                return False
        except:
            return False
    
    def add_text(self, vector2, text: str, rerender: bool = False) -> bool:
        try:
            if type(text) is str:
                res = True
                x = vector2[0]
                y = vector2[1]
                for i in range(len(text)):
                    if not self.set_pixel(Vector2(x + i, y), text[i]):
                        res = False
                if rerender:
                    self.render()
                return res
            else:
                return False
        except:
            return False

    def clear(self, start = None, end = None):
        self.draw_block(start, end, self.background)

    def draw_block(self, start, end, symbol):
        try:
            x1 = start[0]
            y1 = start[1]
            x2 = end[0]
            y2 = end[1]
        except:
            x1, x2, y1, y2 = (None, None, None, None)
        if not x1:
            x1 = 0
        if not y1:
            y1 = 0
        if not x2:
            x2 = self.columns
        if not y2:
            y2 = self.lines
        if x1 < 0:
            x1 = 0
        if y1 < 0:
            y1 = 0
        if x2 > self.columns:
            x2 = self.columns
        if y2 > self.lines:
            y2 = self.lines
        for i in range(y1, y2):
            for j in range(x1, x2):
                self._pixels[i][j] = symbol

if __name__ == "__main__":
    display = Display(100, 15, "-")
    display.add_text(Vector2(10, 3), "Test")
    vect = Vector2(10, 3)
    display.render()
    sleep(2)
    display.draw_block(Vector2(1, 1), Vector2(120, 120), "lol")
    display.render()