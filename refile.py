from PIL import Image
import os
from pathlib import Path

path = "voucher2/fixxx"
index_list = []
index_list = os.listdir(path)

awal = int(input("Ubah mulai dari Index ke berapa?"))
akhir = int(input("Sampe Index ke berapa?"))

for x in range (awal, akhir) :


    basename = os.path.basename(index_list[x])
    basename_path = Path(basename).stem
    img_png = Image.open("voucher2/fixxx/" + str(basename_path) + ".png")
    # img_resize = img2.resize((1250, 1330))
    # img1.paste(img_resize, (310,5580))
    img_png.save("voucher2/hasil/" + str(basename_path) + ".jpg")


# im_png = Image.open(r'voucher2/fixxx/00afa2dd-8ce3-4995-b238-d096a61b642e.png')
# im_jpg = im_png.save(r'voucher2/hasil/00afa2dd-8ce3-4995-b238-d096a61b642e.jpg')