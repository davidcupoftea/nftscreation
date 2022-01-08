from PIL import Image
import random
import cv2
for w in range(13):
    background = Image.open(f"C:\\Users\\david\\Desktop\\David\\CREACION NFT'S - FALTA RESPALDAR DISCOS DUROS\\CEREBRO SOLO\\BACKGROUND\\{w+1}de.png")
    for x in range(13):
        text = Image.open(f"C:\\Users\\david\\Desktop\\David\\CREACION NFT'S - FALTA RESPALDAR DISCOS DUROS\\CEREBRO SOLO\\TEXTO\\{x+1}e.png")
        background.paste(text, (0, 0), text)
        for y in range(13):
            leftbrain = Image.open(f"C:\\Users\\david\\Desktop\\David\\CREACION NFT'S - FALTA RESPALDAR DISCOS DUROS\\CEREBRO SOLO\\IZQUIERDA\\{y+1}a.png")
            background.paste(leftbrain, (930,480), leftbrain)
            for z in range(13):
                plane = Image.open(f"C:\\Users\\david\\Desktop\\David\\CREACION NFT'S - FALTA RESPALDAR DISCOS DUROS\\CEREBRO SOLO\\AVION\\{z+1}c.png")
                background.paste(plane, (930,480), plane)
                rightbrain = Image.open(f"C:\\Users\\david\\Desktop\\David\\CREACION NFT'S - FALTA RESPALDAR DISCOS DUROS\\CEREBRO SOLO\\DERECHA\\{y+1}b.png")
                background.paste(rightbrain, (930,480), rightbrain)
                background.save(f"C:\\Users\\david\\Desktop\\David\\CREACION NFT'S - FALTA RESPALDAR DISCOS DUROS\\CEREBRO SOLO\\RESULTADO\\{w+1}-{x+1}-{y+1}-{z+1}.png")
