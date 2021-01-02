import PIL.Image as Image

path = r"C:/Users/haoze/Desktop/test/F1.png"  
im = Image.open(path)
x, y = im.size

p = Image.new('RGBA', im.size, "red")
p.paste(im, (0, 0, x, y), im)

p.save("C:\\Users\\haoze\\Desktop\\test.png")