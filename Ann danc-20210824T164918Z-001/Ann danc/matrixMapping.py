from PIL import Image
import numpy as np

img = Image.open('AnnTrim.jpg')

pixels = img.load()

PixPerLEDW = img.size[0] / 32
PixPerLEDH = img.size[1] / 64


for i in range(img.size[0]): # for every pixel:
    for j in range(img.size[1]):
            # change to black if not red
        if pixels[i,j][0] > 175:
            pixels[i,j] = (255,0,0)
        else:
            pixels[i,j] = (0,0,0)


pixX = 0
pixY = 0
average = 0
ledMatrix = [[0]*64 for i in range(32)]
for x in range(32):
    for y in range(64):
        while(pixX < PixPerLEDW):
            while(pixY < PixPerLEDH):
                if(PixPerLEDH - pixY < 1):
                    average += (PixPerLEDH - pixY) * pixels[x*PixPerLEDW + pixX, y*PixPerLEDH + pixY][0]
                    pixY += PixPerLEDH - pixY
                else:
                    average += pixels[x*PixPerLEDW + pixX, y*PixPerLEDH + pixY][0]
                    pixY += 1
            pixY = 0
            if(PixPerLEDW - pixX  < 1):
                pixX += PixPerLEDW - pixX
            else:
                pixX += 1
        pixX = 0
        average /= PixPerLEDW * PixPerLEDH
        ledMatrix[x][y] = average
        average = 0

for x in range(img.size[0]): # for every pixel:
    for y in range(img.size[1]):
        if(ledMatrix[int(x / PixPerLEDW)][int(y / PixPerLEDH)] > 0):
            pixels[x,y] = (round(ledMatrix[int(x / PixPerLEDW)][int(y / PixPerLEDH)])+50, 0, 0)

        
print(ledMatrix)
    

img.save("New.jpg")