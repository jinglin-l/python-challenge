from PIL import Image
import requests 
from io import BytesIO

# ok, i see a photo with a very suspicious strip of gray pixels. how can we possibly turn photo data into string data?

# oooh fun, google tells me pillow is a excellent library for image processing.
# https://pillow.readthedocs.io/en/stable/handbook/overview.html

# let's try to open the image and get the pixels

# response.content is type bytes
response = requests.get("http://www.pythonchallenge.com/pc/def/oxygen.png")

# use BytesIO to convert the bytes to an image object
image = Image.open(BytesIO(response.content))
print("image type: ", type(image))
# print("pixels type: ", type(pixels))
# print("pixels: ", pixels)

# woah, lots of rgba pixels. maybe we only care about the gray pixels in the photo, though.
# let's try to grab the middle row of pixels
height = image.height
width = image.width
middle_row = height // 2
start_idx = middle_row * width
end_idx = start_idx + width

print("start_idx: ", start_idx)
print("end_idx: ", end_idx)

middle_row_pixels = pixels[start_idx:end_idx]

# print("middle_row_pixels: ", middle_row_pixels)
# seems like each sqaure in the photo is 7 pixels wide from counting the number of repeated pixels

message = ""
for index, pixel in enumerate(middle_row_pixels):
    if index % 7 == 0 and pixel[0] == pixel[1] == pixel[2]:
        message += chr(pixel[0])

print("message: ", message)

next_level = [105, 110, 116, 101, 103, 114, 105, 116, 121]
next_level_message = ""
for num in next_level:
    next_level_message += chr(num)
print("next_level_message: ", next_level_message)