
from PIL import Image
import os


LOCATION = os.getcwd()
FACE_LOCATION = str(LOCATION + "/face-image/")
ALL_DATA_SET = set()

NEW_IMG = Image.new("RGB", (500,500), "white")
NEW_IMG_PIXEL = NEW_IMG.load()
IMAGE_LEN = 0

def Process(image):
    global FACE_LOCATION
    global ALL_DATA_SET
    global LOCATION
    global IMAGE_LEN

    img_open = Image.open(str(FACE_LOCATION + image))
    resized_image = img_open.resize((500, 500))
    pixel = resized_image.load()
    width, height = resized_image.size

    for x in range(width):
        for y in range(height):
            pixel_color = pixel[x, y]
            ALL_DATA_SET.add((x, y, pixel_color))

for face_image in os.listdir(FACE_LOCATION):
    Process(face_image)
    print("!len: " + str(IMAGE_LEN))
    IMAGE_LEN += 1


print("!Continue")
for set in ALL_DATA_SET:
    NEW_IMG.putpixel(
        (set[0], set[1]),
        (set[2][0], set[2][1], set[2][2]),
    )

print("!SUCCESFULY")
NEW_IMG.show()
