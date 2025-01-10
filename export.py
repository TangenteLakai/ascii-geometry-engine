from PIL import Image, ImageDraw

def warn() -> None:
    print("[Warning] Please run this script by importing it into another file and running the function export")

def export(bin: list[list[int]]):
    bin
    pixel_size, width, height = set_dimensions(bin)
    image, draw = (bin, width, height)
    draw_image(bin, draw, pixel_size)
    return image

def set_dimensions(bin):
    pixel_size: int = 20  # Size of each pixel in the image
    width = len(bin[0]) * pixel_size
    height = len(bin) * pixel_size
    return pixel_size, width, height

def create_image(bin, width, height):
    image = Image.new('1', (width, height), 1)  # '1' for 1-bit pixels, black and white
    draw = ImageDraw.Draw(image)
    return image, draw

def draw_image(bin, draw, pixel_size):
    # Loop through the binary matrix and draw each pixel
    for y, row in enumerate(bin_image):
        for x, pixel in enumerate(row):
            if pixel == 1:
                # Draw a filled rectangle where there is a 1
                draw.rectangle([x * pixel_size, y * pixel_size, (x + 1) * pixel_size, (y + 1) * pixel_size], fill=0)

if __name__ == "__main__":
    warn()
