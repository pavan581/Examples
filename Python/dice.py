from PIL import Image
import random

a = random.randrange(1,7)

print(a)

x = {
    1:Image.open(r"dice_1 image address"),
    2:Image.open(r"dice_2 image address"),
    3:Image.open(r"dice_3 image address"),
    4:Image.open(r"dice_4 image address"),
    5:Image.open(r"dice_5 image address"),
    6:Image.open(r"dice_6 image address")
    }

im = x.get(a)


im.show()
