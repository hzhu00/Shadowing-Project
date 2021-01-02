import PIL.Image as Image
import os
import random

# The current program is only for TP condition.

class array():
    def __init__(self):
        self.foilnum = int(input("How many foils? (5/9/15)\n"))
        self.row = 2
        if self.foilnum == 5:
            self.col = 3
        elif self.foilnum == 9:
            self.col = 5
        elif self.foilnum == 15:
            self.col = 8
        # self.arraynum = int(input("How many arrays for this foil number?\n"))
        self.impath = "C:\\Users\\haoze\\Desktop\\Images for experiment\\"
        self.target = random.randint(1, 200)
        self.targetpath = self.impath + str(self.target) + ".png"
        self.imheight = 1200
        self.imwidth = 512
        self.resultname = "Array" + str(self.foilnum) + ".png"

    def getimnames(self):   
        imlist = []
        for j in range(self.foilnum):
            imlist.append(str(random.choice([i for i in range(1, 201) if i not in [self.target]])))
        tarindex = random.randint(0, self.foilnum + 1)
        imlist.insert(tarindex, str(self.target))
        return imlist

    def change_bg(self, im):
        x, y = im.size
        p = Image.new('RGBA', im.size, "white")
        p.paste(im, (0, 0, x, y), im)
        return p

    def image_compose(self, resultname):
        image_names = self.getimnames()
        to_image = Image.new('RGB', (self.col * self.imwidth, self.row * self.imheight), "white")
        for y in range(1, self.row + 1):
            for x in range(1, self.col + 1):
                from_image = Image.open(self.impath + image_names[self.col * (y - 1) + x - 1] + ".png").resize(
                    (self.imwidth, self.imheight), Image.ANTIALIAS)
                to_image.paste(self.change_bg(from_image), ((x - 1) * self.imwidth, (y - 1) * self.imheight))
        return to_image.save(resultname)

def main():
    a = array()
    arraynum = int(input("How many arrays needed?\n"))
    for n in range(arraynum):
        a.image_compose(str(n+1) + ".png")

main()