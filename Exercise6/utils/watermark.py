from PIL import Image, ImageFont, ImageDraw
import os
from imutils import paths

font = ImageFont.truetype(r'C:\Users\User\Documents\GitHub\NeuralNetworkExercises\Exercise6\Sans_Serif.ttf', size=15, encoding="utf-8")


def watermark(image_path, text):
    image = Image.open(image_path)

    rgba_image = image.convert('RGBA')

    margin = (int(rgba_image.size[0]/10),20)
    #Text Image Creation
    text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))
    image_draw = ImageDraw.Draw(text_overlay)
    text_size_x, text_size_y = image_draw.textsize(text, font=font)
    text_image = Image.new('RGBA', (text_size_x, text_size_y), (255, 255, 255, 0))
    image_draw = ImageDraw.Draw(text_image)
    text_xy = ((text_image.size[0] / 2) - (text_size_x / 2), (text_image.size[1] / 2) - (text_size_y / 2))
    image_draw.text(text_xy, text, font=font, fill=(255, 255, 255, 200))
    mark = text_image
    main = rgba_image
    
    watermarks_number = 4
    tmp_img = Image.new('RGBA', main.size)
    cell_x=main.size[0]//watermarks_number
    margin_x = int(text_size_x/2)
    
    cells_x = []    
    skip=False
    for i in range(-margin_x, main.size[0]+margin_x,cell_x):
        cells_x.append(i)

    for i,it in enumerate(cells_x):
        if i %2==0:
            skip=True
        else:
            skip=False
        for j in range(0+margin[1], tmp_img.size[1]-margin[1], mark.size[1]+margin[1]):
            if skip:
                skip=False
            else:
                main.paste(mark, (it, j), mark)
                skip=True

    main = main.convert('RGB')
    main.save(os.path.splitext(image_path)[0]+"_watermarked.jpg")

if __name__ == '__main__':
    imagePaths = sorted(list(paths.list_images(r"C:\Users\User\Documents\GitHub\NeuralNetworkExercises\Exercise6\data\colorize\test\images")))
    print(imagePaths)
    for imagePath in imagePaths:
        watermark(imagePath, "github.com/sasha-sem")