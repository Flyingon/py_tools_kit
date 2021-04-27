import whatimage
import pyheif
from PIL import Image
import os


def decodeImage(bytesIo, index, compress, sub_file):
    with open(bytesIo, 'rb') as f:
        data = f.read()
    fmt = whatimage.identify_image(data)
    if fmt in ['heic', 'avif']:
        i = pyheif.read_heif(data)
        pi = Image.frombytes(mode=i.mode, size=i.size, data=i.data)
        width = pi.size[0]  # 获取宽度
        height = pi.size[1]  # 获取高度
        out = pi.resize((int(width * compress), int(height * compress)), Image.ANTIALIAS)
        out.save(source + "/../" + sub_file + "/" + "new" + str(index) + ".jpg", format="jpeg")


if __name__ == '__main__':
    source = "/Users/yuanzhaoyi/Documents/gua"
    pic_list = os.listdir(source)
    pic_list.sort()
    for index, file in enumerate(pic_list):
        file = source + "/" + file
        print(index, file)
        # decodeImage(file, index, 0.3, "sgua")
        decodeImage(file, index, 1, "bgua")
