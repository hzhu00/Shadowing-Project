import PIL.Image as Image
import os
import random
import numpy as np

# The current program is only for TP condition.

class array():
    def __init__(self):
        self.foilnum = int(input("How many foils? (5/10/15)\n"))
        self.usedfoils = []
        self.row = 2
        self.col = 8
        self.arraynum = int(input("How many arrays for this foil number?\n"))
        self.impath = "C:\\Users\\haoze\\Desktop\\Images for experiment\\"
        self.target = random.randint(1, 200)
        self.targetpath = self.impath + str(self.target) + ".png"
        self.imheight = 1200
        self.imwidth = 512
        self.resultname = "Array" + str(self.foilnum) + ".png"

    def change_imheight(self, new_height):
        self.imheight = new_height
        self.imwidth = int((512 / 1200) * self.imheight)

    def get_foils(self):
        foils = []
        for j in range(self.foilnum):
            foil = random.choice([i for i in range(1, 201) if i not in [self.target]+self.usedfoils])
            self.usedfoils.append(foil)
            foils.append(str(foil))
        return foils

    def list_image_names(self):   
        imlist = self.get_foils()
        tarindex = random.randint(0, self.foilnum + 1)
        imlist.insert(tarindex, str(self.target))
        if len(imlist) != 16:
            whitenum = 16 - len(imlist)
            lst = np.random.randint(16, size=whitenum).tolist()
            for n in lst:
                imlist.insert(n, str(0))
        return imlist

    def change_bg(self, im):
        x, y = im.size
        p = Image.new('RGBA', (self.imwidth, self.imheight), "white")
        p.paste(im, (0, 0, x, y), im)
        return p

    def image_compose(self, resultname):
        image_names = self.list_image_names()
        print(image_names)
        to_image = Image.new('RGB', (self.col * self.imwidth, self.row * self.imheight), "white")
        for y in range(1, self.row + 1):
            for x in range(1, self.col + 1):
                image_index = self.col * (y - 1) + x - 1
                from_image = Image.open(self.impath + image_names[image_index] + ".png")
                a, b = from_image.size
                from_image = from_image.resize((int((a/b)*self.imheight), self.imheight), Image.ANTIALIAS)
                if image_names[image_index] != 0:
                    to_image.paste(self.change_bg(from_image.convert("RGBA")), ((x - 1) * self.imwidth, (y - 1) * self.imheight))
                else:
                    to_image.paste(from_image, ((x - 1) * self.imwidth, (y - 1) * self.imheight))
        return to_image.save(resultname)

    def repeat_compose(self):
        for n in range(self.arraynum):
            a.image_compose(str(n+1) + ".png")

a = array()
a.repeat_compose()