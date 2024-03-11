from PIL import Image
import pytesseract

# Path to the Tesseract executable (change this if necessary)
#pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
image_path = '050224/-001470_Немченко_Л.Н._ЛичнРеквизиты.jpg'
def ocr_image(image_path):
    # Open the image file
    image = Image.open(image_path)

    # Perform OCR on the image
    text = pytesseract.image_to_string(image, lang='rus')

    return text

# Path to the image file
# image_path = '050224/ямангулова втб.jpg'

# # Perform OCR on the image and print the extracted text
extracted_text = ocr_image(image_path)
print(extracted_text)
