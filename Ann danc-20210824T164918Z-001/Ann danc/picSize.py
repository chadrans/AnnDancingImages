from PIL import Image
#import Image
import numpy as np



#pixels = img.load()

# width, height = img.size

# for i in range(img.size[0]): # for every pixel:
#     if(pixels[i, round(img.size[1] / 2)][0] < 10 and pixels[i, round(img.size[1] / 2)][1] < 10 and pixels[i, round(img.size[1] / 2)][2] < 10):
#         print('yo')
#         print(i)
#         break

# for i in range(img.size[1]): # for every pixel:
#     if(pixels[round(img.size[0] / 2), i][0] < 3 and pixels[round(img.size[0] / 2), i][1] < 3 and pixels[round(img.size[0] / 2), i][2] < 3):
#         print('eh')
#         print(i)
#         break

# # im1 = im.crop(left, top, right, bottom)
# im1 = img.crop(img.size)
# im1.show((width / 4, height / 4, width * 3 / 4, height * 3 / 4))


for num in range(62, 82):
    # Size of the image in pixels (size of original image)
    # (This is not mandatory)
    im = Image.open('IMG_00' + str(num) + '.jpg')

    width, height = im.size
    
    # Setting the points for cropped image
    left = width / 4 + 30
    top = height / 3 + 50
    right = width * 3 / 4 + 100
    bottom = 2 * height / 3 + 20
    
    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))
    
    # Shows the image in image viewer
    im1.save('Ann' + str(num - 62) + '.jpg')