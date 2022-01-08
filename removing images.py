import os

for w in range(13):
    for x in range(13):
        for y in range(13):
            for z in range(13):
                if w + 1 == x + 1 or w + 1 == y + 1 or w + 1 == z + 1:
                    if os.path.exists(f"C:\\Users\\david\\Desktop\\David\\CREACION NFT'S - FALTA RESPALDAR DISCOS DUROS\\CEREBRO SOLO\\RESULTADO PURGADO\\{w+1}-{x+1}-{y+1}-{z+1}.png"):
                        os.remove(f"C:\\Users\\david\\Desktop\\David\\CREACION NFT'S - FALTA RESPALDAR DISCOS DUROS\\CEREBRO SOLO\\RESULTADO PURGADO\\{w+1}-{x+1}-{y+1}-{z+1}.png")

