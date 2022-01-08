from PIL import Image
import random
import cv2

for x in range(13):
    print(x+1)
    img = cv2.imread(f"C:\\Users\\david\\Desktop\\David\\CREACION NFT'S - FALTA RESPALDAR DISCOS DUROS\\CEREBRO SOLO\\BACKGROUND\\{x+1}d.png", cv2.IMREAD_UNCHANGED)
    print(img)
    print('Original Dimensions : ', img.shape)

    scale_percent = 200  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    resized = cv2.resize(img, dim, interpolation=cv2.INTER_CUBIC)
    #cv2.imshow("Resized image", resized)
    cv2.imwrite(f"C:\\Users\\david\\Desktop\\David\\CREACION NFT'S - FALTA RESPALDAR DISCOS DUROS\\CEREBRO SOLO\\BACKGROUND\\{x+1}de.png", resized, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

