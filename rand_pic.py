import PIL.Image as Image
import os
import matplotlib.pyplot as plt
 
IMAGES_PATH = 'C:\\Users\\haoze\\Desktop\\test\\' # 图片集地址
IMAGES_FORMAT = ['.png', '.PNG'] # 图片格式
IMAGE_HEIGHT = 1200 # 每张小图片的大小
IMAGE_WIDTH = 512
IMAGE_ROW = 2 # 图片间隔，也就是合并成一张图后，一共有几行
IMAGE_COLUMN = 10 # 图片间隔，也就是合并成一张图后，一共有几列
IMAGE_SAVE_PATH = 'final.jpg' # 图片转换后的地址
 
# 获取图片集地址下的所有图片名称
image_names = [name for name in os.listdir(IMAGES_PATH) for item in IMAGES_FORMAT if
        os.path.splitext(name)[1] == item]
 
# 简单的对于参数的设定和实际图片集的大小进行数量判断
if len(image_names) != IMAGE_ROW * IMAGE_COLUMN:
    raise ValueError("合成图片的参数和要求的数量不能匹配！")
 
def change_bg(im):
    x, y = im.size
    p = Image.new('RGBA', im.size, "white")
    p.paste(im, (0, 0, x, y), im)
    return p

# 定义图像拼接函数
def image_compose():
    to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_WIDTH, IMAGE_ROW * IMAGE_HEIGHT), "white") #创建一个新图
#   plt.imshow(to_image)
#   plt.show()
  # 循环遍历，把每张图片按顺序粘贴到对应位置上
    for y in range(1, IMAGE_ROW + 1):
        for x in range(1, IMAGE_COLUMN + 1):
            from_image = Image.open(IMAGES_PATH + image_names[IMAGE_COLUMN * (y - 1) + x - 1]).resize(
                (IMAGE_WIDTH, IMAGE_HEIGHT),Image.ANTIALIAS)
            # plt.imshow(to_image)
            # plt.show()
            to_image.paste(change_bg(from_image), ((x - 1) * IMAGE_WIDTH, (y - 1) * IMAGE_HEIGHT))
    return to_image.save(IMAGE_SAVE_PATH) # 保存新图

image_compose() #调用函数