from PIL import Image
image = Image.open('fractal.jfif')
print(image.mode)
print(image.size)
print(image.format)
image.thumbnail((128, 128))
image.show()
