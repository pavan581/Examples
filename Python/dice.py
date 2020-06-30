from PIL import Image
import random

a = random.randrange(1,6)

print(a)

if(a == 1):
    im = Image.open(r"D:\pavan\Android\XML files\dice XML\dice_1.jpg")
elif(a == 2):
    im = Image.open(r"D:\pavan\Android\XML files\dice XML\dice_2.jpg")
elif(a == 3):
    im = Image.open(r"D:\pavan\Android\XML files\dice XML\dice_3.jpg")
elif(a == 4):
    im = Image.open(r"D:\pavan\Android\XML files\dice XML\dice_4.jpg")
elif(a == 5):
    im = Image.open(r"D:\pavan\Android\XML files\dice XML\dice_5.jpg")
elif(a == 6):
    im = Image.open(r"D:\pavan\Android\XML files\dice XML\dice_6.jpg")
    
im.show()
