from PIL import Image
import numpy as np
from enum import IntEnum
from define import Color, Rgb

class ImageProcess:
    def gray_scale(self, src):
        Width, Height = src.size

        ArrayImage = np.array(src)
        ArrayImage.flags.writeable = True
        for y in range(Height):
            for x in range(Width):
                ArrayImage[y, x][Color.RED] = Rgb.MAX - ArrayImage[y, x][Color.RED]
                ArrayImage[y, x][Color.GREEN] = Rgb.MAX - ArrayImage[y, x][Color.GREEN]
                ArrayImage[y, x][Color.BLUE] = Rgb.MAX - ArrayImage[y, x][Color.BLUE]

        return Image.fromarray(np.uint8(ArrayImage))