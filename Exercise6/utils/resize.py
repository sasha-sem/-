from PIL import Image, ImageFont, ImageDraw
import os
from imutils import paths


def resize(image_path: str, target_size : tuple[int, int], suffix: str):
    image = Image.open(image_path)
    resized = image.copy()
    resized = image.resize(target_size)
    resized.save(os.path.splitext(image_path)[0]+f"_{suffix}.jpg")

if __name__ == '__main__':
    imagePaths = sorted(list(paths.list_images(r"C:\Users\User\Documents\GitHub\NeuralNetworkExercises\Exercise6\data\upscale\test\images")))
    for imagePath in imagePaths:
        resize(imagePath, (256, 256), "mini")