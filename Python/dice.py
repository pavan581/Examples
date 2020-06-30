from PIL import Image
import random

a = random.randrange(1,6)

print(a)

x = {
    1:Image.open(r"D:\pavan\Android\XML files\dice XML\dice_1.jpg"),
    2:Image.open(r"D:\pavan\Android\XML files\dice XML\dice_2.jpg"),
    3:Image.open(r"D:\pavan\Android\XML files\dice XML\dice_3.jpg"),
    4:Image.open(r"D:\pavan\Android\XML files\dice XML\dice_4.jpg"),
    5:Image.open(r"D:\pavan\Android\XML files\dice XML\dice_5.jpg"),
    6:Image.open(r"D:\pavan\Android\XML files\dice XML\dice_6.jpg")
    }

im = x.get(a)


im.show()
