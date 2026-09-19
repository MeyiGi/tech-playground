from PIL import Image

width  = 1600
height = 1200

pixels = [[0] * width for _ in range(height)]

center_x = width // 2
center_y = height // 2
radius = 500

for y in range(height):
    for x in range(width):
        circle_equation = (x - center_x) ** 2 + (y - center_y) ** 2 

        if circle_equation <= radius ** 2:
            pixels[y][x] = 255
        
        # if (circle_equation <= radius ** 2 + radius 
        #     and circle_equation >= radius ** 2 - radius):
        #     pixels[y][x] = 255

# img = Image.new("L", (width, height))
img = Image.open("data/cat_image.jpg").convert("RGB")
img = img.resize((width, height))

for y in range(height):
    for x in range(width):
        if pixels[y][x] == 255:
            r, g, b = img.getpixel((x, y))
            img.putpixel(
                (x, y), 
                (int(r * 100), 
                 int(g * 100), 
                 int(b * 100)))

            # тут ситуация такой что надо максимум найти так как все ихображеения проходит надо переводить в матрицу после так работать так как так удобнее потому что сразу с изображеним так себе надо находить максимум и после с ним нормировать что бы все не стао елым 


img.show()