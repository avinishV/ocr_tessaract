try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text


if __name__ == "__main__":
	file_path = "/home/webwerks/Documents/backup_file/ocr-code-master/eurotext.png"
	txt_extract = ocr_core(file_path)
	print(ocr_core(file_path))
	print("\ntype:", type(txt_extract))