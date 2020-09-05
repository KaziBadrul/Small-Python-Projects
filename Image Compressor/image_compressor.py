from PIL import Image, ImageFilter, ImageFont, ImageDraw, ImageStat
from sys import argv, exit
from time import sleep

# USAGE
# USE python [imagefile] in command line to start the program {The imagefile's whole directory must be provided if image not in the current directory}
# CHOOSE which function to use {b for blur, c for compress, bc for blur and compress, s for stats}
# USE python [imagefile] no-mark FOR no watermark
# COMPRESS has 3 levels of compression 3 being the highest level
# BLUR takes in radius to set gausian blur to the picture
# BLUR AND COMPRESS has 2 levels of compression 2 being the highest level

mark = True
def start():
    if len(argv) < 2 or len(argv) > 3:
        print("python image_compressor.py [filename.extension]") 
        exit()
    global mark
    if len(argv) == 3 and argv[2]:
        if argv[2] != "no-mark":
            print("Wrong arguments!")
            exit()
        else:
            mark = False
    
    try:
        og_image = Image.open(argv[1])
    except:
        print("File cannot be opened!")
        exit()
    print()
    function = input("c for compression\nb for blur\nbc for compressed blur: ")
    print()
    if function == "c": compress(og_image)
    if function == "b": blur(og_image)
    if function == "bc": compressed_blur(og_image)
    if function == "s": stats(og_image)

def stats(og_image):
    stat = ImageStat.Stat(og_image)
    print(stat.count, stat.sum, stat.stddev)

def compressed_blur(og_image):
    blurRadius = int(input("Radius: "))
    print()
    im = og_image.filter(ImageFilter.GaussianBlur(radius=blurRadius))
    level = int(input("Compression Level(1-2): "))
    print()
    if level == 1: size = 1280, 600
    elif level == 2: size = 800, 400
    if mark:
        watermark(im)
    im.thumbnail(size)
    im.save("compressed_blur" + ".jpg", "JPEG")
    Image.open('compressed_blur.jpg').show()

def blur(og_image):
    blurRadius = int(input("Radius: "))
    print()
    im = og_image.filter(ImageFilter.GaussianBlur(radius=blurRadius))
    if mark:
        watermark(im)
    im.save("blurred" + ".jpg", "JPEG")
    Image.open('blurred.jpg').show()

def compress(og_image):
    level = int(input("Compression Level(1-3): "))
    print()

    if mark:
        watermark(og_image)
    if level == 1: size = 1280, 600
    elif level == 2: size = 800, 400
    elif level == 3: size = 300, 150

    og_image.thumbnail(size)
    og_image.save("compressed" + ".jpg", "JPEG")
    Image.open('compressed.jpg').show()

def watermark(og_image):
    draw = ImageDraw.Draw(og_image)
    font = ImageFont.truetype('siestha.otf', 30)
    draw.text((10,10), "Compressed by KB", font=font)

if __name__ == "__main__":
    start()