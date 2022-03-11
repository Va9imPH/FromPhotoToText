import pytesseract
from PIL import Image

# load image
img = Image.open("images\images.png")
# tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

custom_config = r'--oem 3 --psm 6'
# convert to text
text = pytesseract.image_to_string(img, config=custom_config)

# user file name
file_name = input("Type file name: ")
# save as .txt
with open(f'{file_name}.txt', "w") as text_file:
    text_file.write(text)