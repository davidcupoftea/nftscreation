from PIL import Image
import random
import cv2

background = Image.open(f"C:\\Users\\david\\Desktop\\David\\CREACION NFT'S - FALTA RESPALDAR DISCOS DUROS\\CEREBRO SOLO\\BACKGROUND\\13de.png")
text = Image.open(f"C:\\Users\\david\\Desktop\\David\\CREACION NFT'S - FALTA RESPALDAR DISCOS DUROS\\CEREBRO SOLO\\TEXTO\\1e.png")
background.paste(text, (0, 0), text)
leftbrain = Image.open(f"C:\\Users\\david\\Desktop\\David\\CREACION NFT'S - FALTA RESPALDAR DISCOS DUROS\\CEREBRO SOLO\\IZQUIERDA\\1a.png")
background.paste(leftbrain, (930, 480), leftbrain)
plane = Image.open(f"C:\\Users\\david\\Desktop\\David\\CREACION NFT'S - FALTA RESPALDAR DISCOS DUROS\\CEREBRO SOLO\\AVION\\1c.png")
background.paste(plane, (930, 480), plane)
rightbrain = Image.open(f"C:\\Users\\david\\Desktop\\David\\CREACION NFT'S - FALTA RESPALDAR DISCOS DUROS\\CEREBRO SOLO\\DERECHA\\1b.png")
background.paste(rightbrain, (930, 480), rightbrain)
background.save(f"C:\\Users\\david\\Desktop\\David\\CREACION NFT'S - FALTA RESPALDAR DISCOS DUROS\\CEREBRO SOLO\\RESULTADO\\1.png")
