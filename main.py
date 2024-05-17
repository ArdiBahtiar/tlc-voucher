from PIL import Image
import os

img1 = Image.open("voucher.png")
path = "gambar"
index_list = []
index_list = os.listdir(path)

awal = int(input("Print mulai dari Index ke berapa?"))
akhir = int(input("Sampe Index ke berapa?"))

for x in range (awal, akhir) :

    # img2 = Image.open("gambar/qr/image" + x + ".png")
    basename = os.path.basename(index_list[x])
    img2 = Image.open("gambar/" + str(basename))
    img_resize = img2.resize((1250, 1330))
    img1.paste(img_resize, (310,5580))
    img1.save("voucher2/hasil/" + str(basename))



# img1.show()