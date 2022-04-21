import math
import PIL
import extcolors
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from matplotlib import gridspec
COLORS_TO_SHOW = 10
COLUMNS = 10
FILEPATH = 'images_color_palette/'
NAME = 'The Killing of the Sacred Deer'
FILETYPE =".jpg"

def visualize_image(image_path):
    image = PIL.Image.open(image_path)
    return image
'''
Extraction of colors from the image to produce the color palette.
Colors are extracted ordered.
Tolerance : Group colors to limit the output and give a
                        better visual representation. Based on a
                        scale from 0 to 100. Where 0 won't group any
                        color and 100 will group all colors into one.
                        Tolerance 0 will bypass all conversion.
                        Defaults to 32.
'''
def extract_colors(img):
    colors, pixel_count = extcolors.extract_from_image(img,tolerance=32)
    return colors

def create_color_palette(colors,img):
    MAX_COLORS = min(len(colors),COLORS_TO_SHOW)
    columns = COLUMNS
    width_img, height_img = img.size
    width = width_img
    height = int(math.floor(width_img / MAX_COLORS))
    size = width_img / MAX_COLORS
    result = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    canvas = ImageDraw.Draw(result)
    count_colors = 0
    for idx, color in enumerate(colors):
        x = (idx % columns) * size
        y = int(math.floor(idx / columns) * size)
        canvas.rectangle([(x, y), (x + size, y + size)], fill=color[0])
        count_colors+=1
        if count_colors == MAX_COLORS:
            break

    return result

def create_image(img, color_palette):
    nrow = 2
    ncol = 1
    width_img, height_img = img.size
    width_palette,height_palette = color_palette.size
    total_width = width_img / 100
    total_height = (height_palette+ height_img)/ 100
    f = plt.figure(figsize=(total_width,total_height), dpi=100)
    gs = gridspec.GridSpec(2, 1, height_ratios=[height_img, height_palette])
    ax0 = plt.subplot(gs[0])
    ax0.imshow(img)
    ax0.axis('off')
    ax1 = plt.subplot(gs[1])
    ax1.axis('off')
    ax1.imshow(color_palette)

    plt.tight_layout()

    plt.savefig(FILEPATH+""+NAME+"_palette.png", transparent=True,dpi=100)

allImages = ['Climax','Mandy','Donnie Darko','Suntan','Eternal Sunshine of the Spotless Mind','Joker']
for name in allImages:
    NAME = name
    image_path = FILEPATH+NAME+FILETYPE
    img = visualize_image(image_path)
    colors = extract_colors(img)
    color_palette = create_color_palette(colors,img)
    create_image(img, color_palette)
